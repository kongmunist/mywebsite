title: MacGyvering Electronics From Merch
date: 2021-05-31
label: log
tags: [electronics, macgyver]
snippet: TFW no batteries :( 

Hello! I moved into Chicago yesterday and needed to do some electronics. Specifically, I needed a battery. But I had left my LiPo bag at home, and my 9Vs with it! What to do?

## Merch to the rescue!

My friend had received a small, rechargeable ring light from a CMU thing. Since it had been made this year and not in 2008, I had figured it probably had a charging circuit and LiPo in it, which would be useful in the future. Today was that day!

<p class="caption">Ring light on, courtesy of CMU</p>
![Ring light on]({{ url_for('static', filename = 'mcg1_ringlight.jpg')}})

Sam, if you're reading this, sorry for what you're about to witness. 

<p class="caption">Cute little LiPo powering the ring light</p>
![Cute little LiPo in the ring light]({{ url_for('static', filename = 'mcg1_battery.jpg')}})

So I pried off the back hinge and spring, then broke my thumbnail on the front panel. Tried again with my nail clipper while fixing the rest of my thumbnail, and this revealed what I knew had to be in there: the tiniest little LiPo I had ever seen. 

Here's a better view of the circuit. I couldn't identify two of the chips here. 

<p class="caption">Cheapest way to charge the cheapest LiPo</p>
![Cheapest way to charge the cheapest LiPo]({{ url_for('static', filename = 'mcg1_circuit.jpg')}})

The top half is connected to the button which turns on the light. There's 3 levels of light + off, so maybe a 4-state... resistor? Another current limiting device? Not exactly sure. But the SOT-23 is a low-side MOSFET, and the battery's ground connection goes through the other chip before reaching the FET. 

Bottom half is the battery charger. Looking at the resistors, it appears they're using a resistor divider with 5100Ω and 1200Ω to step the USB's 5V down to 5 x 5100/(1200+5100) = 4.04V, with at least 0.8mA going across the 1200Ω. Astounding cost saving measure. I'm not sure how the resistor is handling this, since almost 1mA across 1200Ω is 1W wasted heat, but props to them.


And of course, I didn't even have a soldering iron. Two alligator clips saved the day, scavenged from another project.

<p class="caption">Alligator clips dangerously close to each other</p>
![Alligator clips dangerously close to each other]({{ url_for('static', filename = 'mcg1_alligator.jpg')}})

In the end, this worked for my purposes, except that it also let in current the other way. I had to add an LED to the path since I didn't have a real diode -.- but that's the last of my electronics adventure today.

## Did you learn anything?
In the middle of doing this whole janky process, I went to CVS to buy scissors to cut some wire and didn't think to just buy a 9V. Serves me right for trying to be clever, next time I'm going for pragmatic.

Cya next time!