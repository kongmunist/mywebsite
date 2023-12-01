import re

from flask import Flask, render_template, url_for, render_template_string, Markup, \
        redirect,make_response,send_from_directory
from flask_flatpages import FlatPages, pygmented_markdown
# from flask_bootstrap import Bootstrap
from flask_frozen import Freezer
from feedgen.feed import FeedGenerator

from datetime import datetime, timedelta
import pytz
import sys
import subprocess
import os
import time




# run "python sitebuilder.py build" in shell to build to the build folder
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FREEZER_IGNORE_404_NOT_FOUND = True

# FLATPAGES_ROOT ='/Users/andykong/Library/Mobile Documents/com~apple~CloudDocs/programming/personalwebsite/pages'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
#bootstrap = Bootstrap(app)


# FLATPAGES_EXTENSION = '.md'
# app.FLATPAGES_EXTENSION = '.md'
app.config['FLATPAGES_EXTENSION'] = '.md'
print(app.config['FLATPAGES_EXTENSION'])




# Allows markdown to do flask functions before the site's HTML renders. INTEGRAL. SO IMPORTANT.
def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    # print("PR Body", type(prerendered_body), prerendered_body)
    # pygmented_markdown converts the ~[]() syntax into actual html
    # print("pyg body", type(pygmented_markdown(prerendered_body)), pygmented_markdown(prerendered_body))
    return pygmented_markdown(prerendered_body)
app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja

def dateconvert(str):
    return str.strftime("%B %-d, %Y") # Andy, if you read this in the future, -d is said not to be portable between OSs, and on windows # might work instead. Otherwise we go back to dates with leading zeros
app.jinja_env.globals.update(dateconvert=dateconvert)

@app.context_processor
def utility_processor():
    def add_pic(filename, captionalt, center=True):
        # format for image:
        # < p class ="caption" > Desc < / p > ![Caption]({{url_for('static', filename='badglasses.png')}})

        overallString = ""
        mdstuff = "![%s]({{url_for(\"static\", filename=\"%s\")}})" % (captionalt, filename)

        # don't add caption if it's empty string
        if not len(captionalt.strip()) == 0:
            pstuff = "<p class =\"caption\"> %s </p>" % captionalt
            overallString += Markup(pstuff) + "\n" + render_template_string(mdstuff)
        else:
            overallString += render_template_string(mdstuff)

        # Cursed double conversion because I don't know how to add html attributes to a markdown string.
        if (center):
            pyg = pygmented_markdown(overallString)
            if ("<img" in pyg):
                # print("IMG, ", pyg)
                imgInd = pyg.find("<img") + 4
                centerHTML = ' style="display: block; margin-left: auto;margin-right: auto;" '
                overallString = Markup(pyg[:imgInd] + centerHTML + pyg[imgInd:])
                # print(pyg[:imgInd], "AIDNWIN", pyg[imgInd:])
        return overallString

    def add_vid(filename, width="75%", speed=1.0, autoplay=False):
        srcName = " src=\"{{url_for(\"static\", filename=\"%s\")}}\"" % filename
        srcName = render_template_string(srcName)
        fString = ""
        fString += "<video width=\"%s\" controls" % width
        fString += srcName
        fString += " style=\"display: block; margin-left: auto; margin-right: auto;\""
        if speed != 1.0:
            fString += " onloadstart=\"this.playbackRate=%s;\"" % speed
        if autoplay:
            fString += " autoplay"
        fString += ">" + "</video>"
        return Markup(fString)



    return dict(add_pic=add_pic, add_vid=add_vid)



###################### Flask setup functions ##############################
@app.route("/")
def index():
    # return redirect("projects") #render_template('index.html', pages=pages)
    print("about me + projects main page")
    projPages = [p for p in pages if "project" == p.meta.get('label')]
    projPages = [(x.meta.get('date'), x) for x in projPages]
    projPages.sort(reverse=True, key=lambda x: x[0])

    # filter out projects that are in the future
    today = datetime.date(datetime.now()) + timedelta(days=1)
    projPages = filter(lambda x: x[0] < today, projPages)

    # Extract out the pages only
    projPages = [x[1] for x in projPages]

    return render_template('main.html', pages = projPages)


@app.route("/sitemap.xml")
def sitemap():
    blogPosts = [p for p in pages if "blog" == p.meta.get('label')]
    projPosts = [p for p in pages if "project" == p.meta.get('label')]


    # Remove projects whose date is in the future
    today = datetime.date(datetime.now())
    projPosts = filter(lambda x: x['date'] < today, projPosts)
    # Remove blog posts whose tags have wip
    blogPosts = filter(lambda x: x.meta.get('label') == 'blog' and 'wip' not in x.meta.get('tags'), blogPosts)

    posts = list(blogPosts) + list(projPosts)
    posts.sort(reverse=True, key=lambda x: x['date'])


    print(posts[0], posts[0].meta, posts[0].meta.keys())
    print(posts[0].html)
    pa = '/<img.*?src="(.*?)"/g'
    pa2 = '<img.*?src\s*=\s*"?(.+?)"'
    print("REGEX:", re.findall(pa, posts[0].html))
    print("REGEX2:", re.findall(pa2, posts[0].html))

    for post in posts:
        ims = re.findall(pa2, post.html)
        ims = [x.split("/static/")[1] for x in ims if "static" in x]
        post.meta['images'] = ims
    return render_template("sitemap.xml", posts=posts)

@app.route("/rss.xml")
def rss():
    print("rss page")

    # Get blog pages
    blogPages = [p for p in pages if "blog" == p.meta.get('label')]
    blogPages = [(x.meta.get('date'), x) for x in blogPages if
                 'wip' not in x.meta.get('tags')]
    blogPages.sort(reverse=True, key=lambda x: x[0])
    blogPages = [x[1] for x in blogPages]

    # Create Feed generator
    fg = FeedGenerator()
    fg.title("Andy Kong's Blog")
    fg.description('Thoughts and Work')
    fg.link(href='https://andykong.org')

    for article in blogPages:  # get_news() returns a list of articles from somewhere
        if 'wip' not in article.meta.get('tags'):
            fe = fg.add_entry()
            fe.title(article.meta['title'])
            fe.link(href=article.path)
            fe.content(article.body)
            fe.description(article.meta['snippet'], isSummary=True)
            fe.author(name="Andy Kong", email="andyking99@gmail.com")
            dt = datetime.combine(article.meta['date'], datetime.min.time())
            timezone = pytz.timezone('America/New_York')
            fe.pubDate(timezone.localize(dt))

    response = make_response(fg.rss_str(pretty=True))
    response.headers.set('Content-Type', 'application/rss+xml')

    return response


@app.route("/about/")
def about():
    # print("about page")
    # return render_template('about.html')
    return redirect("/")


@app.route("/blog/")
def mainblog():
    print("main blog page")
    blogPages = [p for p in pages if "blog"==p.meta.get('label')]
    blogPages = [(x.meta.get('date'), x) for x in blogPages if 'wip' not in x.meta.get('tags')]

    blogPages.sort(reverse=True, key= lambda x: x[0])
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
    numPages = dict()

    allTag = []
    # For all blog posts,
    for p in pages:
        if ("blog"==p.meta.get('label')):
            for t in p.meta.get('tags', []):
                tl = t.lower()
                listPages.add(tl)
                numPages[tl] = numPages.get(tl, 0) + 1
                allTag.append(tl)

    listPages = sorted(list(listPages))
    numPages = [numPages[x] for x in listPages]
    return render_template('tagmain.html', pages=listPages, num_per_tag=numPages)

@app.route('/tagged/<string:tag>/')
def tag(tag):
    print("tag " + tag)
    tl = tag.lower()
    tagged = [p for p in pages if tl in [x.lower() for x in p.meta.get('tags', [])]]

    if len(tagged) == 0:
        return maintag()
    return render_template('tag.html', pages=tagged, tag=tl)


@app.route('/projects/')
def mainproject():
    print("main project page")
    projPages = [p for p in pages if "project" == p.meta.get('label')]
    projPages = [(x.meta.get('date'), x) for x in projPages]
    projPages.sort(reverse=True, key=lambda x: x[0])

    # filter out projects that are in the future
    today = datetime.date(datetime.now()) + timedelta(days=1)
    projPages = filter(lambda x: x[0] < today, projPages)

    # take just page
    projPages = [x[1] for x in projPages]

    return render_template('projectsmain.html', pages = projPages)

@app.route('/projects/<string:project>/')
def project(project):
    print("project " + project)
    # if project == "facemeshdemos":
    #     return redirect(url_for("static", filename="FaceMeshMedium/index.html"))

    page = [pages.get("projects/" + project)]
    if page[0] is None:
        return mainproject()
    return render_template('projects.html', page = page[0])


# Serving another website as a suburl from flask
@app.route("/tester/")
def tester():
    print("tester")
    # url =
    # return render_template(url_for("static", filename=url)) # template not found
    # return send_from_directory("static", url) # url_for("static", filename=url)) # static resources not loaded properly
    return redirect(url_for("static", filename="FaceMeshMedium/index.html")) # works, but now I have to add index.html to the url

@app.route("/friends/")
def friends():
    # print("friends" + friend)
    print("friends")
    return render_template("friends.html")

@app.route("/vday2020/")
def vday2020():
    print("vday2020")
    return render_template("vday2020.html")

@app.route('/<path:path>/')
def page(path):
    print("page " + path)
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        # Builds the website into a static site and runs "firebase deploy" to update the site
        if len(sys.argv) > 2 and sys.argv[2] == "local":
            # turn off DEBUG
            DEBUG = False

            # Download all files in the static folder
            for icloud_file in [x for x in os.listdir("static/") if ".icloud" in x]:
                os.system("brctl download static/" + icloud_file)

            # wait for them to download
            print("waiting for static resources to download from icloud", end="")
            while (len([x for x in os.listdir("static/") if ".icloud" in x]) > 0):
                time.sleep(2)
                print(".", end="")


            # PLEASE DO NOT RUN "python sitebuilder.py build local" IF YOU ARE NOT ON ANDY'S MAC
            app.config["FREEZER_DESTINATION"] = "andykong.org/public"
            freezer.freeze()

            # Push everything to github
            os.system("git stage -A")
            os.system("git commit -m \"blog update " + time.ctime() + "\"")
            os.system("git push origin master")

            # Deploy build file to firebase — effective 10/4 no more firebase.
            # os.system("(cd andykong.org && firebase deploy)")
        else:
            freezer.freeze()
    else:
        app.run(port=8001)













