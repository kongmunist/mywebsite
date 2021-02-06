title: Direction-of-Voice
date: 2020-12-18
label: project
timespan: January-May 2020
pic: dov_thumbnail.png
description: A novel method for estimating speaker head direction from a single microphone array

<h1 style="text-align:center;"> First paper! </h1>

<h3 style="text-align:center; margin-bottom:0px;" >
	Direction-of-Voice (DoV) Estimation for Intuitive Speech Interaction with Smart Device Ecosystems
	<a href="{{ url_for('static',filename='dov.pdf') }}" target="_blank">(PDF)</a> 
</h3>
<img style="margin-top:10px;" class="d-block mx-auto" src="{{ url_for('static',filename='dov_hero.png') }}"/>
<hr>

Welcome to my first paper! 

If you've perused my page at all, you'll know that I've always worked on human interface type things. However, this research was the first time I was able to put a name to the type of things that interested me, and I learned a ton of other stuff in the process as well. 

Earlier this year (2020), I started working with PhD student [Karan Ahuja](https://karan-ahuja.com/) at Figlab on an audio paper. While previous researchers had determined a sound's direction-of-arrival from a microphone array, nobody had been able to determine if the sound's speaker was facing the mic array without adding multiple microphones around a room. 

Application-wise, if this were your smart home device, and it could know where you were speaking from, it’d be able to respond directly when it knew you were speaking to it. This could remove wakewords like “Hey assistant,” allowing users to just speak to their smart devices as if it were just another person in the room.

If you want to find out more about how we did it, just check out the paper [here]({{ url_for('static',filename='dov.pdf') }})!

In the process, I learned a lot: audio data, Processing, data processing, Tkinter, PyQT, sockets, FFTs, scipy, UI design, data collection, data cleaning, running user studies, and the basics of HCI research. Wow! Truly a great project, and the first major one I've finished.



