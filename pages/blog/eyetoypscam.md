title: Playstation Eye does not work for MacOS!
date: 2020-11-15
label: log
tags: [problems, hardware]
snippet: Mac doesn't play nice with weird USB webcams :(

I wasted like an hour and a half today trying to get this Playstation 3 camera working on my Mac:

<img src={{ url_for('static', filename = 'playstationeye.jpg')}} width="300" class="d-block mx-auto"/>

Let me tell you how I debugged it.

After plugging in, the USB name identifies it as a USB Webcam, but simply refuses to recognize its data like one. Apparently this is a problem with many USB webcams and Mac, necessitating the invention of the [macam project](http://webcam-osx.sourceforge.net/), which exists specifically for installing drivers for USB webcams. It was only maintained from 2006-2007, explaining why it doesn't have a github repo (git was invented 2005), but good thing those drivers don't change! 

Except I'm running Catalina, and they wrote their code in 32-bit :(. Someone has been kind enough to port it to GitHub as [macam64](https://github.com/smokris/macam64). 

I tried to follow their steps but my CMake version was out of date. I then tried to use homebrew to update my CMake. It took 20 minutes, updating and installing all sorts of other things, and even had the audacity to tell me it had agreed to qt's user agreement on my behalf (threatening that if I disagreed with its decision, I should uninstall QT immediately). When I ran CMake again, I found that the original CMake location was not the one Homebrew had updated. 

I stopped here. I hate dealing with pathing issues. If I have it, just go find it!!! Maybe one day I will muster the vernacular to venture forth, but today I sighed, and gave up on this webcam. 
