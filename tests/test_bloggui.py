import io
import tempfile
import unittest
from pathlib import Path

from bloggui.app import app, process_body_html


class BlogGuiImagePasteTests(unittest.TestCase):
    def test_pasted_jpeg_keeps_jpg_extension_even_with_generic_png_name(self):
        old_upload_path = app.config['UPLOADED_PATH']
        try:
            with tempfile.TemporaryDirectory() as upload_path:
                app.config['UPLOADED_PATH'] = upload_path

                response = app.test_client().post(
                    '/upload',
                    data={
                        'upload': (
                            io.BytesIO(b'\xff\xd8\xff\xe0jpeg-data'),
                            'pasted-image.png',
                            'image/jpeg',
                        )
                    },
                    content_type='multipart/form-data',
                )

                self.assertEqual(response.status_code, 200)
                filename = response.get_json()['filename']
                self.assertTrue(filename.startswith('pasted-image'))
                self.assertTrue(filename.endswith('.jpg'))
                self.assertTrue((Path(upload_path) / filename).exists())
        finally:
            app.config['UPLOADED_PATH'] = old_upload_path

    def test_inline_local_image_is_converted_and_queued_for_copy(self):
        body, local_images = process_body_html(
            '<p>before<img src="/files/pasted-imageABCDE.jpg" /></p>'
            '<p><a href="https://example.com">after</a></p>',
            'new-post',
        )

        self.assertIn('before', body)
        self.assertIn('{{ add_pic("new-post/0.jpg", "") }}', body)
        self.assertIn('<a href="https://example.com">after</a>', body)
        self.assertNotIn('/files/', body)
        self.assertNotIn('<img', body)
        self.assertEqual(local_images[0].upload_filename, 'pasted-imageABCDE.jpg')
        self.assertEqual(local_images[0].output_filename, 'new-post/0.jpg')

    def test_external_image_with_query_string_is_not_treated_as_local_upload(self):
        src = 'https://example.com/image.jpg?format=png&width=512'
        body, local_images = process_body_html(f'<p><img src="{src}" /></p>', 'new-post')

        self.assertEqual(local_images, [])
        self.assertIn(f'![]({src})', body)
        self.assertNotIn('new-post/0.', body)

    def test_native_ckeditor_uploadimage_plugin_is_disabled(self):
        self.assertNotIn('uploadimage', app.config.get('CKEDITOR_EXTRA_PLUGINS', []))


if __name__ == '__main__':
    unittest.main()
