title: Variable resistance tests of Velostat/Linqstat 
date: 2020-05-17
label: blog
tags: [wearables, conductivefabric, velostat]
snippet: Testing the effects of bending, twisting, and touch on the conductive plastic Velostat.

This is [Velostat](https://en.wikipedia.org/wiki/Velostat):

<img src={{ url_for("static", filename = 'velostat.jpg') }} width="400" class="d-block mx-auto"/>

It's a conductive sheet that's sometimes used for packaging ESD-sensitive electronics, but is commonly used by wearables hobbyists since it changes resistance when <i>anything</i> happens to it. Wrinkling. Heating. Bending. Twisting. Pressing. Anything that touches it is detectable!

However, there's not a ton of information about it online, like how much change in resistance is visible for bending vs. twisting, etc. So I decide to do some testing and show y'all the results so you wouldn't have to!

All tests were done on a 6.0 x 1.2 cm piece of the material, which I got from Adafruit. I held it in contact using some alligator clips, which weren't super precise contacts. This is probably why the baseline resistances were so variable, around 55 kΩ ± 5 kΩ. 

<img src={{ url_for("static", filename = 'velostatnormal2.jpg') }} width="400" class="d-block mx-auto"/>

<p class="caption">Basic experimental setup</p>

### Twisting

<img src={{ url_for("static", filename = 'velostat180.jpg') }} width="400" class="d-block mx-auto"/>

For these tests, I simply flipped one alligator clip and held the strip taut on the table. Best results came from twisting the strip so much that it curled into a tube, around 360 degrees for this width of strip.

<img src={{ url_for("static", filename = 'velostattwist.png') }} width="400" class="d-block mx-auto"/>


### Bending 

<img src={{ url_for("static", filename = 'velostatbend.jpg') }} width="400" class="d-block mx-auto"/>

I bent the strip into a bit of an omega shape, which didn't change it much. When I pinched it, the overall distance of the strip changed so the resistance went down instead of up.

<img src={{ url_for("static", filename = 'velostatbend.png') }} width="400" class="d-block mx-auto"/>


### Pulling

The resistance increased "linearly" from not pulling to maximum pull strength. This test was a bit tricky since my resistance would change the strips if I touched both alligator clips, so I carefully pulled both ends of the plastic without contacting the clips. 

<img src={{ url_for("static", filename = 'velostatpull.png') }} width="400" class="d-block mx-auto"/>

### Touching/Pressure

When it comes to pressure, Velostat is not that great of a sensor without modification. I found that surface area of the finger touch affects the resistance more than pressing on it, and that non-finger touching with a plastic scissor's handle did not affect it much at at all. 

<img src={{ url_for("static", filename = 'velostattouch.png') }} width="400" class="d-block mx-auto"/>


### Touching (Bent sheet)

Since I wanted to use this as a pressure sensor, I tried folding the sheet in the middle then pressing on that. This worked much better, but required securing by tape or some other adhesive. 

<img src={{ url_for("static", filename = 'velostatfoldtouch.png') }} width="400" class="d-block mx-auto"/>

### Heating

[This](https://electronics.stackexchange.com/questions/452291/velostat-sensitivity-to-temperature) site I visited claimed that heat did not affect the sheet's resistance, but I decided to test it out. I held a soldering iron near my test strip without touching it, and found the biggest changes yet! It took a few seconds to heat to the max resistance, and about a minute to cool back to baseline. 

<img src={{ url_for("static", filename = 'velostatheating.png') }} width="400" class="d-block mx-auto"/>

### Connections and Conclusions

I wanted to connect some wire to this stuff, but [some people](https://www.kobakant.at/DIY/?p=381) online were using copper tape with conductive adhesive and conductive thread, which I didn't have. I tried soldering to it, but it just melted :(. Since alligator clips worked, I tried "crimping" some metal wire onto it, and that seemed to work well. Seems like it just needs to be in tight contact with metal to conduct. 

<img src={{ url_for("static", filename = 'velostatcrimp.jpg') }} width="400" class="d-block mx-auto"/>


That's all! I'm probably going to stick with pressure sensing with my folded sheet, it seems to produce pretty drastic resistance changes. 



