title: The MH290
date: 2020-11-30
label: blog
tags: [history, electronics, wip]
snippet: The first generation of handheld barcode scanners

These barcode scanners are hard to find, and fairly expensive when you do find them. They're all pretty bulky due to the laser tube, and fragile because of it. Usually you can find one for $40-$100. Luckily, I found a bulk sale of 17 MH290s and purchased them, and am reselling in individual quantities.

LS7000 barcode scanner — first one
History here:
http://www.scholarpedia.org/article/Bar_code_scanning

Power on for MH290 here
http://www.repairfaq.org/sam/sale/henemll1.htm

A few months ago, I became obsessed with finding these specific barcode scanners:

Why? They were the first ones! Back in the 1970s


Theoretically, [this guide](http://www.repairfaq.org/sam/sale/henemll1.htm) for the MH290 from Sam's Laser FAQ tells you everything you need to know. Practically there's a few considerations you need to think about, like the current draw being a few amp. A 15V wall adaptor will work, and only requires a bit of soldering to get a wire to trigger the PWM-on pin on the DIP IC that drives the laser. If you use an insufficient power supply or wall brick, you'll notice a slight flickering and buzzing to the laser which makes it look unstable but also *cool* at the same time.

WIP