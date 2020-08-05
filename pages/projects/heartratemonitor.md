title: Web Heartrate Monitor
date: 2020-08-05
label: project
timespan: July-August 2020
pic: heartratemainpage.png
description: Website that can determine your heartrate using ambient lighting and a camera.

Hey! This is Andy. Here's the link to the [website that can find your heartrate](http://heartrateleaderboard.netlify.app/).

I recently came across this app that used a smartphone camera and flashlight to calculate your heartrate. This relies on the fact that oxygenated blood and deoxygenated blood have different colors, and it's noticeable on a smartphone camera. In fact, one of my favorite party tricks is to start recording a video on my phone while pressing my finger on the camera, and show people how you can <i>see</i> my pulse as the color on the video pulses a darker color occasionally. Try it yourself!

<img src={{ url_for('static', filename = 'heartratebloodcolor.jpeg')}} class="d-block mx-auto img-thumbnail"/>
<p class="caption">And no, it's not blue when deoxygenated.</p>

Anyway, I thought to myself that it must be a simple matter to move this app's functionality onto a website. So I did. Using HTML webcam access, I even found out that ambient light is often enough to see the pulse against (especially if you have the help of a computer). 

<a href="http://heartrateleaderboard.netlify.app/" target="_blank"><img src={{ url_for('static', filename = 'heartratemainpage.png')}} class="d-block mx-auto img-thumbnail"/></a>

Once I had the array of webcam brightnesses, I just had to take the FFT of it in order to find the actual frequency I wanted. This is easier said than done, since there are no native Javascript FFT libraries. I converted one using browserify, and had to figure out how to turn the FFT output into frequency bins. Overall, an enjoyable experience. I had never made sense of the FFT output myself before, libraries usually give the frequency bins for you. 

After that, it was pretty much done! Just added some instructions and graph for the FFT to help me do the bin-to-frequency conversion. 

