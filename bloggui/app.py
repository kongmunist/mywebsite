# from flask import Flask, render_template, request
from flask import Flask, render_template, request, url_for, send_from_directory
import re
import random, os
import datetime
from copy import copy
# from flask_ckeditor import CKEditor
from flask_ckeditor import CKEditor, CKEditorField, upload_fail, upload_success
basedir = os.path.abspath(os.path.dirname(__file__))

from html.parser import HTMLParser
parser = HTMLParser()

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
        blogPostName = request.form.get("postname")
        saveFilename = blogPostName + ".md"
        # titleStr = "".join(title.split(" ")[:2]).lower()
        date = str(datetime.date.today())
        tags = request.form.get('tags')
        snippet = request.form.get('snippet')
        body = request.form.get('ckeditor')


        print("body:", repr(body))
        # pattern = re.compile(r'(?i)<(?!img|/img).*?>')
        pattern = re.compile(r'(?i)<(?!img|a|/a).*?>') # Remove all html tags except <img> and <a>
        body = pattern.sub('', body)

        # Get all the image names and extensions
        imgs = re.findall(r'src="([^"]+)"', body)
        imgs = [img.split("/")[-1] for img in imgs]
        imgexts = [img.split(".")[-1] for img in imgs]

        # Remove all "\r\n&nbsp;\r\n" from the body
        body = body.replace("\r\n&nbsp;\r\n", "")
        body = body.replace("\r\n", "\n")

        # Replace HTML chars with normal chars
        body = parser.unescape(body)
        body = body.replace("&nbsp;", " ") # non-breaking space
        body = body.replace("\xa0", " ") # other non-breaking space
        body = body.replace("\u200b", "") # zero width space



        # Replace all <img> tags with {{ add_pic("file", "caption") }}
        print("back1: ", body)
        newLines = []
        imIndex = 0
        for line in body.split("\n"):
            if line.startswith("<img"):
                # imFile = imgs[imIndex]
                newLines.append("{{ add_pic(\"" + f"{blogPostName}/{imIndex}." + imgexts[imIndex] + "\", \"\") }}")
                imIndex += 1
            else:
                newLines.append(line)
        body = "\n".join(newLines)
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
            f.write(f"label: blog\n")
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
            import subprocess as sp
            # Move .md file
            sp.run(["cp", saveFilename, f"../pages/blog/{saveFilename}"])
            # move images
            if len(imgs) > 0:
                os.makedirs(f"../static/{blogPostName}", exist_ok=True)
                for i,im in enumerate(imgs):
                    if os.path.exists(f"../static/{blogPostName}/{i}.{imgexts[i]}"):
                        print("Image already exists, moving it but doubling the name")
                        sp.run(["cp", f"uploads/{im}", f"../static/{blogPostName}/{i}_2.{imgexts[i]}"])
                    else:
                        sp.run(["cp", f"uploads/{im}", f"../static/{blogPostName}/{i}.{imgexts[i]}"])
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
    extension = f.filename.split('.')[-1].lower()

    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    f.filename = f.filename.rsplit(".", 1)[0] + getRandStr() + "." + extension
    print("uploaded file: ", f.filename)
    f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    url = url_for('uploaded_files', filename=f.filename)
    return upload_success(url, filename=f.filename)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
