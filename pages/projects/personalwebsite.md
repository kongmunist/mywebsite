title: Personal Website
date: 2019-06-26
label: project
pic: websitev2.png
description: Static website generator built with Flask and hosted on Firebase. You're looking right at it!

Hello! I made a website for showing off my project portfolio, posting "sorry for not posting" blog posts, and hosting an About Me page to make it easier for recruiters to find and ignore links to my Github, Youtube, and food blog.

### 7/2
Lots has been done! The project display page has some neat animations I stole from [this guy](https://miketricking.github.io/bootstrap-image-hover/) and hacked to pieces. Blog list page is also legible now, with lines and stuff separating all the info
<img class="d-block mx-auto" src="{{ url_for("static",filename="websitev3.png") }}"/>
<p class="caption">Rendering the "Date Published" as legible text was inordinately hard given how minor it looks...</p>

Projects also no longer fill your entire FOV (I tried to add a picture to show this but I realize you're also looking right at the changes I am talking about -.-)! The images also scale, but that's more easily demonstrable by just moving the browser's bounds. Need to add sorting by date for the blog and project pages, then those are done!


### 6/29

Writing this update sucked cause of my hacky implementation. Weird workaround in jinja allows the url_for from Flask-FlatPages to work and find the pathnames for images, but it meant there was a lot of shifting and reorganizing of words and images on the page. Real headache. 
<img src={{ url_for('static', filename = 'websitev2.png')}} class="d-block mx-auto img-thumbnail"/>
Anyway, got the color scheme sorted out now so it's less of an eyesore. Using the a variant of [Dream Magnet](https://www.colourlovers.com/palette/482774/dream_magnet) and [Terra](https://www.colourlovers.com/palette/292482/Terra) from this website where people just post nice color aesthetics. Very wholesome site, and quite beautiful. I've never considered that one could "discover" a color, but these people do it just for fun of arranging them. 

###6/27

<img src={{ url_for('static', filename = 'websitev1.png')}} class="d-block mx-auto"/>

Here's what it used to look like. Function before fashion, as they say. I'm working on the projects tab and header, after that I can make it pretty (I say that now, but I might get lazy and rationalize that it won't change anyone's opinion of me considering I don't value my web dev skills very high on my list of capabilities (That was a really long aside, you must be tired of this sentence by now)). 



