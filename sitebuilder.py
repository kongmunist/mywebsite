from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from flask_bootstrap import Bootstrap

import sys
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'



# run "python sitebuilder.py build" in shell to build to the build folder



app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html', pages=pages)

@app.route("/about/")
def about():
    print("about page")
    return render_template('about.html')


@app.route("/blog/")
def mainblog():
    print("main blog page")
    blogPages = [p for p in pages if "blog"==p.meta.get('label')]
    return render_template('blogmain.html', page=[], pages=blogPages)

@app.route("/about/")
def about():
    print("aboutme")
    return render_template('about.html', pages=pages)


# need to make individual redirects for the rest of the tabs too (tagged, projects)

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

# TODO: add blog posts for each tag - list tags and pages
@app.route('/tagged/<string:tag>/')
def tag(tag):
    print("tag " + tag)
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    if len(tagged) == 0:
        return maintag()
    return render_template('tag.html', pages=tagged, tag=tag)

# There is a problem. I'm using logic to handle unknown tag pages and unknown blog entries, but its not gonna work when uploaded

@app.route('/projects/')
def mainproject():
    print("main project page")
    projPages = [p for p in pages if "project" == p.meta.get('label')]
    # projPages = [x.path[9:] for x in projPages]
    return render_template('projectsmain.html', pages = projPages)

@app.route('/projects/<string:project>/')
def project(project):
    print("project " + project)
    page = [pages.get("projects/" + project)]
    if page[0] is None:
        return mainproject()
    return render_template('projects.html', page = page[0])


@app.route('/<path:path>/')
def page(path):
    print("page " + path)

    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)

