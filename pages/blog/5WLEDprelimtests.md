title: Preliminary 5W LED Tests
date: 2021-01-06
label: blog
tags: [projector, projectlog, LED]
snippet: Projecting 5W of light onto a wall — DIY Projector

I show you tests of some 5W LEDs I bought off Amazon, and how they look projected onto a wall that's far away.

## Setup
I got 10 of these yellow LEDs with legs in the mail, along with some aluminum backing plates. It's inordinately hard to find high power LEDs with the backing plates attached, but they're so cheap I just caved and bought them separately. 

<p class="caption">Setup of the 5W LEDs. Each LED has a drop of 6-7V, so I am using two in series to test them with my 12V power supply</p>
![Setup of the 5W LEDs. Each LED has a drop of 6-7V, so I am using two in series to test them with my 12V power supply, which is just a laptop wall brick.]({{ url_for('static', filename = '5Watters.jpg')}})

I'm using a laptop wall brick, which outputs 5V and 12V at 1.5A each. Kinda cool, high output current bricks are a little hard to find. I always feel bad cutting the plug to get to the wires too... 

Anyway. I soldered on the two LEDs, no thermal paste just mechanical contact for now. I'll probably mount it on a larger heatsink, because this thing gets HOT. The circular indents around the edge look like they're for screws to hold in place. 


## Projection
You remember those [Fresnel lenses](../fresnellens) I bought a while back? This is what they were for. Here I got my brother to hold the sheet above the LEDs, and as he moved it up and down, the projected spot on the ceiling changed size and brightness. 

<p class="caption">5W LED (very bright) being held under a Fresnel lens from my last post. I'm holding by the alligator clip since it's very hot.</p>
![5W LED (very bright) being held under a Fresnel lens from my last post. I'm holding by the alligator clip since it's very hot.]({{ url_for('static', filename = '5W_setup.jpg')}})

<p class="caption">Far from the LEDs</p>
![Fresnel lens held far]({{ url_for('static', filename = '5W_tightcircles.jpg')}})

<p class="caption">Middle far</p>
![Fresnel lens held in the middle]({{ url_for('static', filename = '5W_circles.jpg')}})

<p class="caption">Close to the LEDs</p>
![Fresnel lens held close]({{ url_for('static', filename = '5W_bigcircle.jpg')}})

We only turned them on for about a minute, but the backplate hurt immediately to the touch. Definitely need to heatsink them, and I may even have some thermal paste from a computer build a while ago.

The projected spot is massive just from the floor to ceiling, not to mention one wall to another. It could be even brighter if I funnel the light using some aluminum foil or some mirrors. 

One problem is that the Fresnel lens has distortion issues, and doesn't focus very well at all. The edges of shadows projected are all blurry, probably partially because of diffraction around my finger. Maybe I should collimate the light somehow before I shine it through the screen (I want this to show text eventually), but we'll see what problems I run into with the lens I currently have before I come up with new solutions.

Hopefully it'll be alright. Cya next time!