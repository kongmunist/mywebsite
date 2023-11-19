from flask import Flask, render_template, request
from flask import Flask, render_template, request, url_for, send_from_directory

import random, os
import datetime
from flask_ckeditor import CKEditor
from flask_ckeditor import CKEditor, CKEditorField, upload_fail, upload_success
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'

app.secret_key = 'secret string'
app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')

ckeditor = CKEditor(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':


        title = request.form.get('title')
        date = str(datetime.date.today())
        tags = request.form.get('tags')
        snippet = request.form.get('snippet')
        body = request.form.get('ckeditor')

        print("title: ", title)
        print("date: ", date)
        print("tags: ", tags)
        print("snip: ", snippet)
        print("body: ", body)
        # WARNING: use bleach or something similar to clean the data (escape JavaScript code)
        # You may need to store the data in database here

        # Generate the old blog post format .md file using the CK editor info
        saveFilename = "".join(title.split(' ')) + ".md"
        with open(saveFilename, "w+") as f:
            f.write(f"title: {title}\n")
            f.write(f"date: {date}\n")
            f.write(f"tags: [{tags}]\n")
            f.write(f"snippet: [{snippet}]\n")
            f.write(f"{body}")

        # return render_template('post.html', title=title, body=body)
        return
    return render_template('index.html')


@app.route('/files/<filename>')
def uploaded_files(filename):
    path = app.config['UPLOADED_PATH']
    return send_from_directory(path, filename)

def getRandStr(ln=10):
    return "".join([chr(x) for x in random.choices(list(range(65,65+26)), k=ln)])

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    extension = f.filename.split('.')[-1].lower()

    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    f.filename = f.filename.rsplit(".", 1)[0] + getRandStr() + extension
    print("uploaded file: ", f.filename)
    f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    url = url_for('uploaded_files', filename=f.filename)
    return upload_success(url, filename=f.filename)



if __name__ == '__main__':
    app.run(debug=True, port=5001)
