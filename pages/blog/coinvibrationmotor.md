title: Coin vibration motors arrived!
date: 2020-12-14
label: log
tags: [hardware, motor, haptic]
snippet: "Now I can do \"haptic feedback\""

We were going over a [paper by Disney Research](https://la.disneyresearch.com/publication/surround-haptics-sending-shivers-down-your-spine/) in class last week that said two sufficiently close vibration motors on someone's skin created a sensation in a single spot in between them. Then, you could just vary the power to one or the other and "move" the phantom dot back and forth between the two, essentially creating a vibrating line for the price of two motors!


<p class="caption">Image from the Disney Paper "Surround Haptics: Sending Shivers Down Your Spine"</p>
![Image from the Disney Paper "Surround Haptics: Sending Shivers Down Your Spine"]({{ url_for('static', filename = 'surroundhaptics.png')}})

This even extends to two 'virtual' spots, which can create a second phantom vibration spot in their centroid. How cool!

### I had to try it!
So I ordered these tiny coin cell haptics motors off Amazon. 10 for $6, smaller than my pinky fingernail, and powered off 3 volts. Adhesive side and a foamy side. Nominal resistance is 36Ω, I powered them off my Arduino's 3.3V and it worked well. Not insane vibration, but very noticeable! 

The thing started warming up pretty quickly, so I may have to deal with that, but it could just be a lack of current limiting hardware in the way. It also might self-regulate when it gets hot enough, but I don't want it strapped to my arm when I find that out. I'm probably pulling too much current from the Arduino as-is. 

<p class="caption">Me holding one of the tiny coin vibration motors I ordered, foamy side up</p>
![Me holding one of the tiny coin vibration motors I ordered, foamy side up]({{ url_for('static', filename = 'coinvibrationmotors.png')}})

I'm gonna try it and let you know how it goes! Be safe!