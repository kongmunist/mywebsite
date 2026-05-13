from flask import Flask, render_template, request, url_for, send_from_directory
import re
import random, os
import datetime
import html
import shutil
from dataclasses import dataclass
from urllib.parse import unquote, urlparse
from werkzeug.utils import secure_filename
from flask_ckeditor import CKEditor, CKEditorField, upload_fail, upload_success
from bs4 import BeautifulSoup, NavigableString
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'
app.config['CKEDITOR_EXTRA_PLUGINS'] = []

app.secret_key = 'secret string'
app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')

ckeditor = CKEditor(app)

ALLOWED_IMAGE_EXTENSIONS = {'jpg', 'jpeg', 'gif', 'png', 'webp'}
IMAGE_MIME_EXTENSIONS = {
    'image/jpeg': 'jpg',
    'image/png': 'png',
    'image/gif': 'gif',
    'image/webp': 'webp',
}
BLOCK_TAGS = ('p', 'div', 'li', 'ul', 'ol', 'blockquote', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6')


@dataclass
class LocalImage:
    upload_filename: str
    output_filename: str


def get_image_extension(filename):
    extension = os.path.splitext(filename)[1].lstrip('.').lower()
    return 'jpg' if extension == 'jpeg' else extension


def extension_for_upload(filename, content_type):
    original_filename = filename or 'pasted-image'
    base_name = os.path.splitext(os.path.basename(original_filename))[0].lower()
    file_extension = get_image_extension(original_filename)
    mime_extension = IMAGE_MIME_EXTENSIONS.get((content_type or '').split(';')[0].lower())

    if mime_extension and (base_name.startswith('pasted-image') or not file_extension):
        return mime_extension
    return file_extension or mime_extension


def uploaded_filename_from_src(src):
    parsed = urlparse(src or '')
    if parsed.scheme or parsed.netloc:
        return None

    path = unquote(parsed.path)
    if not path.startswith('/files/'):
        return None
    return os.path.basename(path)


def normalize_body_text(body):
    body = body.replace("\r\n&nbsp;\r\n", "")
    body = body.replace("\r\n", "\n")
    body = html.unescape(body)
    body = body.replace("&nbsp;", " ")
    body = body.replace("\xa0", " ")
    body = body.replace("\u200b", "")
    body = re.sub(r'\n{3,}', '\n\n', body)
    return body.strip()


def process_body_html(raw_body, post_slug):
    soup = BeautifulSoup(raw_body or '', 'html.parser')
    local_images = []
    local_image_index = 0

    for br in soup.find_all('br'):
        br.replace_with(NavigableString('\n'))

    for tag in soup.find_all(BLOCK_TAGS):
        tag.insert_before(NavigableString('\n'))
        tag.append(NavigableString('\n'))

    for img in soup.find_all('img'):
        src = img.get('src', '')
        uploaded_filename = uploaded_filename_from_src(src)

        if uploaded_filename:
            extension = get_image_extension(uploaded_filename)
            if extension not in ALLOWED_IMAGE_EXTENSIONS:
                extension = 'png'

            output_filename = f'{post_slug}/{local_image_index}.{extension}'
            local_images.append(LocalImage(uploaded_filename, output_filename))
            replacement = f'\n{{{{ add_pic("{output_filename}", "") }}}}\n'
            local_image_index += 1
        else:
            replacement = f'\n![]({src})\n'

        img.replace_with(NavigableString(replacement))

    body = str(soup)
    pattern = re.compile(r'(?i)<(?!a|/a).*?>')
    body = pattern.sub('', body)
    return normalize_body_text(body), local_images


def copy_local_images(local_images, uploads_path, static_root):
    for local_image in local_images:
        source = os.path.join(uploads_path, local_image.upload_filename)
        destination = os.path.join(static_root, local_image.output_filename)
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        shutil.copy2(source, destination)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        title = request.form.get('title')
        blogPostName = request.form.get("postname")
        saveFilename = blogPostName + ".md"
        # titleStr = "".join(title.split(" ")[:2]).lower()
        date = str(datetime.date.today())
        tags = request.form.get('tags')
        snippet = request.form.get('snippet')
        posttype = request.form.get('posttype', 'blog')
        body = request.form.get('ckeditor')


        print("body:", repr(body))
        body, local_images = process_body_html(body, blogPostName)
        print("new body:", repr(body))
        # WARNING: use bleach or something similar to clean the data (escape JavaScript code)
        # You may need to store the data in database here

        # If any of the headers are empty we redirect to a page that says "Please fill in all the fields"
        if title == "" or blogPostName == "" or tags == "" or snippet == "" or body == "":
            return "You are missing some fields! Please go back and fill them in"

        # Generate the old blog post format .md file using the CK editor info
        with open(saveFilename, "w+") as f:
            f.write(f"title: \"{title}\"\n")
            f.write(f"date: {date}\n")
            f.write(f"label: {posttype}\n")
            f.write(f"tags: [{tags}]\n")
            f.write(f"snippet: \"{snippet}\"\n\n")
            f.write(f"{body}")

        # Move the .md file to the ../pages/blog/ dir, and then move the images
        if os.path.exists(f"../pages/blog/{saveFilename}"):
            # panic, stop doing stuff
            print("Blog post with the same filename already exists!! Not doing anything")
            return "Blog post with the same filename already exists!! Not doing anything until you go back and change it >:("
        else:
            print(os.getcwd())
            shutil.copy2(saveFilename, f"../pages/blog/{saveFilename}")
            copy_local_images(local_images, app.config['UPLOADED_PATH'], "../static")
        # Clear images folder
        # sp.run(["rm", "-r" "uploads/*"])
        # sp.run(["mkdir", "uploads"])


        return render_template('post.html', title=title, body=body)
    return render_template('index.html')


# t = """'<p>ada</p>\r\n\r\n<p><img src="/files/imageODMSKMHFXQ.png" style="height:196px; width:245px" /></p>\r\n\r\n<p>ao902</p>\r\n\r\n<p>ada<br />\r\n<img src="/files/imageHHAPGSQGED.png" style="height:138px; width:125px" /></p>\r\n\r\n<p>asda</p>\r\n'"""
# soup = BeautifulSoup(t)
# soup.replaceAll('(?i)<(?!img|/img).*?>', '');
#
# import re
# pattern = re.compile(r'(?i)<(?!img|/img).*?>')
# a = pattern.sub('', t)
#
#
# # This should be the wrapper that you are targeting
# container = soup.find('div')
# keep = []
#
# for node in container.descendants:
#   if not node.name or node.name == 'a' or node.name == 'img':
#     keep.append(node)
#





# def processBody(txt):
# # txt = """<p><img src="/files/imageIIQEHLZRTOpng" style="height:512px; width:512px" /></p>\r\n\r\n<p><img src="/files/imageBMETYHUOKTpng" style="height:1588px; width:1284px" /></p>\r\n"""
# # txt="""\r\n<p>adad<img src="/files/imageRVQILCBOOF.png" style="height:512px; width:512px" /></p>\r\n\r\n<p>yes</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>no no no on<img src="/files/imageGOXNJKOHWS.png" style="height:1588px; width:1284px" /></p>\r\n"""
#     a = BeautifulSoup(txt)
#     filtered = []
#     imgSrcList = []
#     for child in a.children:
#         t = child
#         # break
#         # If a line contains nada, we remove it. If it contains img, we add the img a md object to filtered. If it contains anything else, we get text contents and add to filtered
#
#         if len(t) > 1: # Passes if nonempty
#             imgList = t.findAll("img")
#             for img in imgList:
#                 imgsrc = img.get("src").split("/")[-1]
#                 imgSrcList.append(imgsrc)
#                 img.replaceWith("\n{{" + f"""add_pic("{imgsrc}", "")""" + "}}")
#             filtered.append(t.getText())
#     bodyStr = "\n".join(filtered)
#     return bodyStr, imgSrcList


#
# lines = txt.split("\r\n")
# lines = [x for x in lines if len(x)]

@app.route('/files/<filename>')
def uploaded_files(filename):
    path = app.config['UPLOADED_PATH']
    return send_from_directory(path, filename)

def getRandStr(ln=5):
    return "".join([chr(x) for x in random.choices(list(range(65,65+26)), k=ln)])

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    if f is None:
        return upload_fail(message='No image uploaded')

    original_filename = f.filename or 'pasted-image'
    extension = extension_for_upload(original_filename, f.content_type)

    if extension not in ALLOWED_IMAGE_EXTENSIONS:
        return upload_fail(message='Image only!')

    # Generate unique filename
    base_name = secure_filename(os.path.splitext(original_filename)[0]) or 'pasted-image'
    new_filename = base_name + getRandStr() + "." + extension
    print("uploaded file: ", new_filename)
    os.makedirs(app.config['UPLOADED_PATH'], exist_ok=True)
    f.save(os.path.join(app.config['UPLOADED_PATH'], new_filename))
    url = url_for('uploaded_files', filename=new_filename)
    return upload_success(url, filename=new_filename)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
@app.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run(debug=True, port=5001)
