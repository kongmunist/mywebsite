from flask import Flask, render_template, url_for, render_template_string, Markup, redirect
from flask_flatpages import FlatPages, pygmented_markdown
from flask_bootstrap import Bootstrap
from flask_frozen import Freezer

from datetime import datetime
import sys
import subprocess
import os
import time


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'


# run "python sitebuilder.py build" in shell to build to the build folder


app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
#bootstrap = Bootstrap(app)

def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)
app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja

def dateconvert(str):
    return str.strftime("%B %d, %Y")
app.jinja_env.globals.update(dateconvert=dateconvert)



@app.route("/")
def index():
    return redirect("projects") #render_template('index.html', pages=pages)

@app.route("/about/")
def about():
    print("about page")
    return render_template('about.html')


@app.route("/blog/")
def mainblog():
    print("main blog page")
    blogPages = [p for p in pages if "blog"==p.meta.get('label')]
    blogPages = [(x.meta.get('date'), x) for x in blogPages]

    blogPages.sort(reverse=True)
    blogPages=[x[1] for x in blogPages]
    return render_template('blogmain.html', page=[], pages=blogPages)

@app.route("/blog/<string:title>/")
def blog(title):
    print("blog page " + title)
    page = [pages.get("blog/" + title)]
    blogPages = [p for p in pages if "blog"==p.meta.get('label')]
    if page[0] is None:
        return mainblog()
    return render_template('blog.html', page=page, pages = blogPages)


@app.route('/tagged/')
def maintag():
    print("main tagged page")
    listPages = set()
    for p in pages:
        for t in p.meta.get('tags', []):
            listPages.add(t)
    return render_template('tagmain.html', page = [], pages=listPages)

@app.route('/tagged/<string:tag>/')
def tag(tag):
    print("tag " + tag)
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    if len(tagged) == 0:
        return maintag()
    return render_template('tag.html', pages=tagged, tag=tag)


@app.route('/projects/')
def mainproject():
    print("main project page")
    projPages = [p for p in pages if "project" == p.meta.get('label')]
    projPages = [(x.meta.get('date'), x) for x in projPages]
    # print(projPages)
    projPages.sort(reverse=True)
    projPages = [x[1] for x in projPages]

    # projPages = [x.path[9:] for x in projPages]
    return render_template('projectsmain.html', pages = projPages)

@app.route('/projects/<string:project>/')
def project(project):
    print("project " + project)
    page = [pages.get("projects/" + project)]
    if page[0] is None:
        return mainproject()
    return render_template('projects.html', page = page[0])


@app.route("/friends/")
def friends():
    # print("friends" + friend)
    print("friends")
    return render_template("friends.html")

@app.route('/<path:path>/')
def page(path):
    print("page " + path)
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        # Builds the website into a static site and runs "firebase deploy" to update the site
        if len(sys.argv) > 2 and sys.argv[2] == "local":
            # PLEASE DO NOT RUN "python sitebuilder.py build local" IF YOU ARE NOT ON ANDY'S MAC
            app.config["FREEZER_DESTINATION"] = "andykong.org/public"
            freezer.freeze()

            # Push everything to github
            os.system("git stage -A")
            os.system("git commit -m \"blog update " + time.ctime() + "\"")
            os.system("git push origin master")

            # Deploy build file to firebase
            os.system("(cd ../andykong.org && firebase deploy)")
        else:
            freezer.freeze()
    else:
        app.run(port=8000)

