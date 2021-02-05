title: Altered Perceptions
date: 2020-03-04
label: project
timespan: November 2019 - January 2020
pic: alteredbonsai.png
description: VR headset + POV camera + preprocessing => new way to see the world

<br>
<div style="text-align:center;" class="d-block mx-auto">
<iframe width="50%" height="100%" align="middle" src="https://www.youtube.com/embed/k4v0TsgcNes" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<br>

This is my first art project, sponsored by the Frank-Ratchye Studio for Creative Inquiry at CMU's School of Fine Arts. Here's the [code on GitHub](https://github.com/kongmunist/alteredperceptions)
<br>

### Motivation
People at my school are always complaining about how boring campus/Pittsburgh/real life looks. "Wean is too brutalist and all concrete" and "Gates smells like coffee and looks ugly." I think the real problem is that we get so used to the things we see every day that we stop really seeing them; that is to say, the beauty of the world is hidden in plain sight. 

So I wanted to build something to change the way we see things, to edit the way objects appear to us so we can see them as exciting new things instead of boring old things. I wanted to take our eyes, and alter their colors, shapes, and details in some way to make people take a good look at their surroundings. How cool would it be if everything you saw was altered like this ibis below?

<img class="d-block mx-auto" src="{{ url_for("static",filename="alteredibis.png") }}"/>

One way you could do this is to have an augmented reality helmet that overlays different filters onto your screen, for your viewing pleasure. But you'd be able to see through it to the real world, since AR is just glass. So I settled on the Playstation VR headset with a USB camera, to sort of approximate VR glasses. In addition, I chose to use an Nvidia Jetson Nano to power the camera and headset, so we could do mid-level processing at live speeds. 

<img class="d-block mx-auto" src="{{ url_for("static",filename="alteredpsvr.jpg") }}"/>

### Hardware Hacking
Usually headsets don't let you access their video streaming directly, however, PSVR's creators are nice/negligent enough to allow simple USB control. To hack into the PSVR's HDMI port to send a screen directly to it, someone wrote a nice Python [script](https://github.com/mungewell/pyPSVR) that accesses it like a monitor screen. Run that once on startup with the options you want and you're good to go. Just show the frames that you want the headset to see on the desktop's screen, and the headset will see the same thing.


### Programming
The code is written in Python. I actually tried C++ OpenCV at first because "real programmers" told me it was faster. However, the screen display was much slower, going at around 100 ms. Terrible latency, makes the whole thing sickening to wear. So I went with Python.

All I do is have multiple threads that run concurrently. One thread grabs the last frame from the camera and puts it in the first aliased list, the second thread pulls the frame from the first list, processes it according to the filter I choose, and puts it in a second aliased list. The third thread pulls an image from the 2nd list and displays it fullscreen. All this code is in complexcamera.py

Depending on the filter number, the processing thread uses a function from neweyes.py. These include thresholding, edge detection, and plain old color swapping. They look pretty cool, and I show off some of them in the video above. 

<img class="d-block mx-auto" src="{{ url_for("static",filename="alteredadaptivethresh.png") }}"/>
<p class="caption">Some neighborhood-aware adaptive thresholding, or NYC Line Profile Style</p>


### Future work

These are all pretty standard CV techniques that I've just modified to be neat to look at, instead of using them to gain more information about an image. I think they look really cool, but at the same time I understand I'm not playing with the shapes or lines or anything too major. The next step for this project is to make it capable of producing DeepDream images live:

<img class="d-block mx-auto" src="{{ url_for("static",filename="altereddeepdreamdog.jpg") }}"/>

DeepDream is sort of like inverting a neural network; you give it a photo, and tell it to make the photo look <i>more</i> like something, a dog or a dumbell or whatever, instead of asking it what the photo is of. But this inversion takes a long time. For even minor effects on shrunken images, it takes over half a second. I think this is because it's not what neural networks are meant for, so I'm going to work on a Convolutional Neural Network that produces DeepDream images going forwards, instead of going backwards. No more inverting and tracing back. Just propogate forward once and you're done. 

But that's a project for later. If you're interested in collaborating on adding more filters or new kinds (I wanted to use Haar Cascades for eye and mouth detection in order to really mess with how people's faces looked), let me know! I'm always down to work on cool image edits (especially if they run LIVE).



