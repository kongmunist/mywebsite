"""Reserve existing images' space and defer media without producing new assets."""
import copy
import os
import re
import struct
from functools import lru_cache
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

from bs4 import BeautifulSoup


def _orientation(exif):
    if not exif.startswith(b'Exif\0\0'):
        return 1
    data = exif[6:]
    endian = '<' if data[:2] == b'II' else '>'
    offset = struct.unpack_from(endian + 'I', data, 4)[0]
    count = struct.unpack_from(endian + 'H', data, offset)[0]
    for index in range(count):
        entry = offset + 2 + index * 12
        tag, kind, length = struct.unpack_from(endian + 'HHI', data, entry)
        if tag == 274 and kind == 3 and length == 1:
            return struct.unpack_from(endian + 'H', data, entry + 8)[0]
    return 1


@lru_cache(maxsize=2048)
def image_dimensions(filename):
    """Read headers only; account for rotated JPEGs without an image dependency."""
    try:
        with open(filename, 'rb') as file:
            header = file.read(24)
            if header.startswith(b'\x89PNG\r\n\x1a\n'):
                return struct.unpack('>II', header[16:24])
            if header[:6] in (b'GIF87a', b'GIF89a'):
                return struct.unpack('<HH', header[6:10])
            if header[:4] == b'RIFF' and header[8:12] == b'WEBP':
                file.seek(20)
                payload = file.read(10)
                if header[12:16] == b'VP8X':
                    return (1 + int.from_bytes(payload[4:7], 'little'),
                            1 + int.from_bytes(payload[7:10], 'little'))
                if header[12:16] == b'VP8L' and payload[0] == 0x2f:
                    bits = int.from_bytes(payload[1:5], 'little')
                    return (1 + (bits & 0x3fff), 1 + ((bits >> 14) & 0x3fff))
                if header[12:16] == b'VP8 ' and payload[3:6] == b'\x9d\x01\x2a':
                    return tuple(value & 0x3fff for value in struct.unpack('<HH', payload[6:10]))
            if header[:2] == b'\xff\xd8':
                file.seek(2)
                dimensions, orientation = None, 1
                while True:
                    marker = file.read(1)
                    if not marker:
                        break
                    if marker != b'\xff':
                        continue
                    marker = file.read(1)
                    while marker == b'\xff':
                        marker = file.read(1)
                    if marker in (b'\xda', b'\xd9', b''):
                        break
                    if marker == b'\x00' or marker == b'\x01' or 0xd0 <= marker[0] <= 0xd7:
                        continue
                    length = struct.unpack('>H', file.read(2))[0] - 2
                    if marker == b'\xe1':
                        segment = file.read(length)
                        try:
                            if segment.startswith(b'Exif\0\0'):
                                orientation = _orientation(segment)
                        except (struct.error, IndexError):
                            pass
                    elif marker[0] in (0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7,
                                      0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf):
                        segment = file.read(length)
                        height, width = struct.unpack('>HH', segment[1:5])
                        dimensions = (width, height)
                    else:
                        file.seek(length, 1)
                if dimensions and orientation in (5, 6, 7, 8):
                    dimensions = dimensions[::-1]
                return dimensions
            if filename.lower().endswith('.svg'):
                file.seek(0)
                root = ElementTree.parse(file).getroot()
                viewbox = root.get('viewBox', '').replace(',', ' ').split()
                if len(viewbox) == 4:
                    return tuple(float(value) for value in viewbox[2:])
                return (float(root.get('width', '').removesuffix('px')),
                        float(root.get('height', '').removesuffix('px')))
    except (OSError, ValueError, struct.error, ElementTree.ParseError):
        return None


def prepare_media(html, static_folder, base_url):
    def image_or_frame(match):
        tag = BeautifulSoup(match.group(), 'html.parser').find(['img', 'iframe'])
        if tag.name == 'iframe':
            tag.attrs.setdefault('loading', 'lazy')
            return str(tag).split('>', 1)[0] + '>'

        eager = bool({'hero-photo', 'profile-pic'} & set(tag.get('class', [])))
        source = urlsplit(tag.get('src', ''))
        eager = eager or source.path == '/static/aklogo.png'
        tag.attrs.setdefault('loading', 'eager' if eager else 'lazy')
        if (not source.netloc or source.netloc == urlsplit(base_url).netloc) and source.path.startswith('/static/'):
            relative_path = unquote(source.path[len('/static/'):])
            filename = os.path.realpath(os.path.join(static_folder, relative_path))
            if os.path.commonpath([filename, os.path.realpath(static_folder)]) == os.path.realpath(static_folder):
                dimensions = image_dimensions(filename)
                if dimensions and all(value > 0 for value in dimensions):
                    width, height = dimensions
                    if not tag.get('width') and not tag.get('height'):
                        tag['width'], tag['height'] = str(int(width)), str(int(height))
                    style = tag.get('style', '')
                    if 'aspect-ratio' not in style:
                        tag['style'] = (style.rstrip('; ') + '; ' if style else '') + f'aspect-ratio: auto {width:g} / {height:g};'
        return str(tag)

    def video(match):
        tag = BeautifulSoup(match.group(), 'html.parser').video
        sources = [tag] + tag.find_all('source')
        if not any(source.get('src') for source in sources):
            return match.group()
        fallback = copy.deepcopy(tag)
        fallback['preload'] = 'none'
        fallback['controls'] = ''
        fallback.attrs.pop('autoplay', None)
        tag['preload'] = 'none'
        tag['loading'] = 'lazy'
        tag['class'] = tag.get('class', []) + ['deferred-video']
        for source in sources:
            if source.get('src'):
                source['data-src'] = source.attrs.pop('src')
        return str(tag) + '<noscript>' + str(fallback) + '</noscript>'

    # Leave scripts and inline examples untouched. Only serialize the media tags.
    protected = r'(<script\b[^>]*>.*?</script>|<!--.*?-->)'
    chunks = re.split(protected, html, flags=re.IGNORECASE | re.DOTALL)
    start_tag = r'<(?:img|iframe)\b(?:[^>\"\']|\"[^\"]*\"|\'[^\']*\')*>'
    for index in range(0, len(chunks), 2):
        chunks[index] = re.sub(start_tag, image_or_frame, chunks[index], flags=re.IGNORECASE)
        chunks[index] = re.sub(r'<video\b[^>]*>.*?</video>', video, chunks[index],
                               flags=re.IGNORECASE | re.DOTALL)
    return ''.join(chunks)
