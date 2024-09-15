title: MPR121 Touch Sensing Across Barriers
date: 2021-03-13
label: log
tags: [mpr121, touchsensitive, sensor, hardware]
snippet: Testing capacitive coupling across various barriers

Hello! Today I received the MPR121, a nifty little 12-channel touch sensor:

<p class="caption">Glamour shot of the MPR121 touch sensor</p>
![Glamour shot of the MPR121 touch sensor]({{ url_for('static', filename = 'mpr121glamour.png')}})

The chip is pretty simple, uses I2C to measure each pin's capacitance using the charge then discharge trick I used [here](../touchreactiveLEDs/). It gives a touch/no touch output, or the raw sensor values per each pin (ranges from 0-400ish). Also has a built-in filtered output that provides smoother data if you want it. 

The setup is easy and not very interesting since the chip is so single-purpose. I'm much more interested in showing you how well the sensor detects touch through a barrier. 

## Testing materials
I used what I had near me, and those were: saran wrap, masking tape, and two kinds of Scotch tape. Here's the table.

<p class="caption"></p>
![Table of sensor outputs for the MPR121]({{ url_for('static', filename = 'mpr121chart.png')}})

As mentioned before, the sensor values range from 0-400. On the bare surface I was able to get down to 48, which is a big SNR! None of the others even came close to that, only dipping 10% of the max value for the Saran wrap. This was probably the thinnest barrier I tried, and even that was too much. Despite the low SNR, the sensor still detected my touches consistently when separated by most of the materials I tried. Works great! :)

The capacititance didn't drift that much across my trials (~15 minutes), so I'm not so worried about needing to recalibrate very frequently. These types of biosensors are usually pretty finicky in that regard, so I'm glad. I also didn't try fabric or any porous material because I needed this to be waterproof, but it'd be cool if YOU (dear reader) did, and then told me about it!

That's all for now! Cya!

<p class="caption">MPR121 wrapped in saran wrap during testing</p>
![MPR121 wrapped in saran wrap during testing]({{ url_for('static', filename = 'mpr121saran.png')}})



