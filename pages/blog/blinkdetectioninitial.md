title: Blink Detection Using Infrared Reflective Sensors
date: 2021-02-12
label: blog
tags: [infrared, Arduino, sensing, blinkdetection]
snippet: Preliminary experiments in focus tracking.

Hello! 

Recently I found out that blink frequency is associated with focus — when shown a more engaging and interesting video, participants tended to blink less. Intuitively this makes sense; if you want to see something, you'll naturally spend less time closing your eyes. I wanted to apply this principle to something more general: living life. But I didn't want to use computer vision! First, face detection is hard to do well, and runs pretty slowly if you also include closed vs. open eyes. I also wouldn't be able to track my blink rate while doing things away from the computer (and believe it or not, much of my life *is* spent away from the computer). So CV was out. 

I had read from a few papers that skin absorbed infrared light super well, so it shows up dark under an infrared camera. I looked around, and sure enough people had been detecting blink with an IR LED and detector situated very closely to the eyes. Since the shiny part of your eyeball is not skin, it reflects a lot of infrared. When you blink, this gets blocked, and the signal you're reading will have a sharp drop. And that's exactly what I did!

## Setup
I ordered some of these IR reflective sensors off Amazon — these are usually used for line following robots or really terrible distance sensors (their output depends on the nearby material's reflectance). 

<p class="caption">IR reflectance sensors. 4 pin, one LED and one phototransistor with a light filter.</p>
![IR reflectance sensors. 4 pin, one LED and one phototransistor with a light filter.]({{ url_for('static', filename = 'blinktrack1_reflectancesensor.png')}})

I then wired it up. LED is current-limited by 100 ohms, phototransistor has 1KΩ in series. I think I can reduce this value to make it more sensitive, since it'll pull down to ground more easily.  

Here it is at work: (first time I've hosted a video locally on this site!)
<div style="text-align:center;">
<video width="320" height="240" controls>
  <source src="{{ url_for('static', filename = 'blinktrack1.mp4')}}" type="video/mp4">
Your browser does not support the video tag.
</video>
</div>

Anyway, signal is pretty clear (spans around 1.5V on the 5V ADC), and isn't too noisy. I have to figure out a way to stop my pupil from messing with the signal, but I'll mount it on some glasses first and see how stable it stays. 

Eventually, I want to push these blink timestamps constantly to a database, and have it ping me when it notices me slipping out of focus. I dunno, something can be done with this additional biometric data. 

That's all for now. Cya!