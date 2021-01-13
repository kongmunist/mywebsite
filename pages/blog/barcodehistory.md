title: The first generation of handheld barcode scanners — with laser tubes
date: 2021-01-13
label: blog
tags: [history, electronics]
snippet: History of the LS1000 and MH290, and a demo of the 2nd!

Hi! Today we have a history lesson! I'm going to tell you the history of the handheld barcode scanner, and how to use one if you have one lying around. 

## History
All but ubiquitous today, the first barcode scanners were stationary and built into the checkout counter. This made it difficult to scan large items, which couldn't easily be passed above the desk. Though laser diodes were invented shortly after the laser (1962, 1960), they were not mass produced until the late 1980s, so these early barcode scanners had to make do with laser tubes — big, fragile, bulky things that are usually around a foot long. So how did they make them handheld?

<p class="caption">Original LS1000 barcode scanner versus modern day barcode scanners. The laser tube in the LS1000 is horizontal and takes up most of the length, while the laser diode powering the 2nd is smaller than your pinky.</p>
![Original LS1000 barcode scanner versus modern day barcode scanners. The laser tube in the LS1000 is horizontal and takes up most of the length, while the laser diode powering the 2nd is smaller than your pinky.]({{ url_for('static', filename='barcodescannerls1000.jpg')}})

With Symbol Technologies, Dr. Jerry Swartz performed calculations in the late 70s and believed that the laser tubes could be miniaturized to 5-6 inches, which were short enough to fit into a handheld scanner. The first company he asked to manufacture them laughed him out of the room, but the second company, Uniphase, believed it could be done. Uniphase later overtook that first company, Spectra-Physics, as the largest manufacture of HeNe laser tubes. The barcode scanner that they created with the shortened laser tube was the LS1000, pictured above. 

Metrologic followed shortly after and released their handheld barcode scanner. They mounted the laser tube along the handle instead along the top shaft, and achieved a much more compact size. 

<p class="caption">The Metrologic 290 handheld barcode scanner. The laser tube is hidden in the handle</p>
![The Metrologic 290 handheld barcode scanner. The laser tube is hidden in the handle]({{ url_for('static', filename='mh290.jpg')}})

After some fundamental problems of room-temperature lasing and stable output were solved, Japan began mass-manufacture of compact laser diodes in the early 80s. Symbol began incorporating these diodes into their products, producing much smaller barcode scanners due to the lack of massive HeNe tube to produce the laser. These lead to the kinds of barcode scanners today, pictured above next to the LS1000.

## Where do you find them now?
Today, these early barcode scanners are hard to find and fairly expensive when you do find them. They're all pretty bulky due to the laser tube, and fragile because of it. Nobody manufactures them anymore, so you'll have to look on resale markets — usually you can find one for $40-$100 on eBay. You can tell it has a tube because of the size — smaller, compact models can't possibly house the 5 inch laser tube that the earlier barcode scanners housed. 

In the past, I found a bulk sale of 17 MH290s and purchased them, and am currently reselling in individual quantities on eBay [here](https://www.ebay.com/itm/Metrologic-MH290-Barcode-Scanner-HeNe-Laser-inside/363080135269). I think everyone who buys old barcode scanners also knows there's a laser tube inside them, because why else would you be buying such an old barcode scanner? It works the same as a new barcode scanner, just bigger and dirtier. 

## What do you do with them?
I guess you could open a vintage grocery if you really wanted, but I wanted the laser tube from within! While reading Sam's Laser FAQ, I found out about the MH290 for the first time and that's what started this whole obsession.

<p class="caption">The laser tube from the MH290 lasing.</p>
![The laser tube from the MH290 lasing.]({{ url_for('static', filename='barcodescannerlaseron.png')}})

Theoretically, [this guide](http://www.repairfaq.org/sam/sale/henemll1.htm) for the MH290 from Sam's Laser FAQ tells you everything you need to know. Practically there's a few considerations you need to think about, like the current draw being a few amp. A 15V wall adaptor will work, and only requires a bit of soldering to get a wire to trigger the PWM-on pin on the DIP IC that drives the laser. If you use an weak power supply or wall brick which can't supply enough current, you'll notice a slight flickering and buzzing to the laser which makes it look unstable but also *cool* at the same time.

This is the first HeNe laser I've owned, and it's probably useful for science. Let me know if you know of anything cool I can do with one!

<br><br><br><br><hr>
### References
[1] [Sam's Repair FAQ guide to powering on MH290](http://www.repairfaq.org/sam/sale/henemll1.htm)

[2] [Scholarpedia entry for bar code scanning](http://www.scholarpedia.org/article/Bar_code_scanning)

