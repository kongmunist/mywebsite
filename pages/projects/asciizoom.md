title: AsciiZOOM
date: 2020-04-25
label: project
timespan: April 2020
pic: asciizoom.png
description: The first secure, text-based videoconferencing app, accessible from the safety of your terminal.


### Video
<div style="text-align:center;" class="d-block mx-auto"><iframe width="560" height="315" src="https://www.youtube.com/embed/g4YCxM5STj0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
<br><br>

<hr>
### Background
Because of security concerns over the use of Zoom ([here](https://theintercept.com/2020/03/31/zoom-meeting-encryption/) and [here](https://en.wikipedia.org/wiki/Zoom_Video_Communications#Security)) and its inability to be invoked from the commmand line, me and a friend decided to get together to make a more secure version. 

<hr>
### Video Encoding
Since we didn't want to eat up all the bandwidth on our server, we decided the most efficient way to send each frame of video was to pack it into a single TCP packet. You might be wondering how we fit a full image in under 50 kilobytes: with text! Through the magic of ascii art, we were able to re-encode a frame as pure text characters, packaging a single pixel into 8 bits instead of the traditional 24. Since we only used 4 unique "characters," we could have further reduced this down to 2 bits if we were really pressed for space, but the additional processing on either end would have led to additional latency.

<img class="d-block mx-auto" src="{{ url_for("static",filename="chickensidecomparison.jpeg") }}"/>

There's plenty of example code online for asciifying an image, but the code is [here](https://github.com/kongmunist/asciiZOOM) for both asciifization and transmitting. This text-based image sending also makes encryption easier, since we can just caesar cipher with a predetermined shift and the image is ruined. 

<hr>
### Networking
We used TCP sockets to transfer the frames of video. In hindsight, we probably should have used UDP, since we don't want dropped frames to accumulate latency. TCP's guaranteed packet delivery means that delays in sending one frame end up delaying every subsequent frame. We set up a server on our school's publicly exposed servers (it's exposed online if you can ssh into it even while not on school wifi) and both connected from our local terminals. The server then coordinates, sending one person's packets to the other person and vice versa. 

And if you want audio, use Discord or something :P
