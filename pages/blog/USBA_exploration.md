title: Exploring USB-A breakout cables
date: 2020-12-04
label: blog
tags: [electronics]
snippet: The normal USB

Recently I had the need for a 5V battery to power a circuit. 

Lithium polymer/ion batteries are powerful and cheap because of the hobbyist drone market, but come in multiples of 3.7V-4.2V. NiMH (AA and AAA) batteries are plentiful and expensive, but only come in intervals of 1.5V (9V is also composed of 6 similar batteries wrapping together. Who knew?!). These would be fine, except I didn't want to deal with a voltage regulator since this was just a quick test. What to do?

The wall outputs 5V through a phone charger, but I (1) needed it to be wearable and (2) incapable of killing you if all the op amps and resistors shorted in just the right way. 

I had an extra portable phone charger battery I had gotten from a career fair, which output 5V at a capacity of 2200 mAh. Most importantly, I already had it. 

![Career fairs are good for something]({{ url_for('static', filename = 'ThanksIBM.jpg')}})
<p class="caption">Career fairs are good for something</p>

I destroyed a USB cable (the other end was this weird flat thing) and plugged it in after charging the battery. Voltmeter confirms, >5V. 

![A multimeter measuring my portable phone battery's voltage]({{ url_for('static', filename = 'USBA_realvoltage.jpg')}})
<p class="caption">A multimeter measuring my portable phone battery's voltage</p>

I expected these batteries to be more regulated, though I suppose there aren't many electronics parts that work at 5V that don't work also at 5.2V. 
