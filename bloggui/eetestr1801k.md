title: "Solar energy harvesting"
date: 2024-08-25
label: blog
tags: [electronics, solar, energyharvesting]
snippet: "Testing out the R1801K"

Hello!

I want to build devices which can charge themselves using energy sources present in the environment. Currently I'm trying out solar.

# Background on solar

Even though a solar cell generates its max voltage in the presence of almost any light, they are high-resistance sources i.e. you can't just connect them directly into your battery. For maximum power, you need to pull just enough current to reduce the solar cell's output to ~80% of its peak voltage, as shown in the chart below. Chips that intelligently track this peak call it MPPT (maximum power point tracking). 

{{ add_pic("eetestr1801k/0.png", "") }}

For my device, the TI BQ25570 is nearly perfect — it offers MPPT and starts from only 600 mV. However, it requires a certain amount of power to start up, around 15 uW. Since I'm expecting almost no light on my device, I wanted to find a chip which starts from even less power. This is where the R1801K comes in — this is a chip made by Nisshinbo that claims to begin harvesting at only 1 uW!

{{ add_pic("eetestr1801k/1.png", "") }}

The only catch is that it requires 4 V, but I think the voltage will be easier to get than the power. So I bought the chip, and my friend Injoo made a little breakout board for me which pulls charge from solar cell into a storage capacitor. 

{{ add_pic("eetestr1801k/2.jpg", "") }}

To simulate a constrained power source, I'm passing 4 V across a 1 MΩ resistor, resulting in an output power of 16 uW. Then I connected my board.

{{ add_pic("eetestr1801k/3.jpeg", "") }}

Initially, the storage capacitor filled up steadily, but at some point my capacitor voltage was just holding still. To compensate, I increased my power supply voltage and the charging started again. Again, after a bit the charging would stop. 

{{ add_pic("eetestr1801k/4.jpeg", "") }}

I was powering the device on 4.8V, and the output voltage could go no further than 1.5V. I realized at this point that my capacitor was probably leaking, and checked out the datasheet. Lo and behold, a leakage current of 12.6 uA! Assuming this happens at the rated voltage (6.3 V), then the capacitor's resistance is 500kΩ. This meant the R1801K was desperately pumping in charge which was being leaked out at the same rate by the capacitor, and at 1.5V, that rate was 3uA. 

{{ add_pic("eetestr1801k/5.png", "") }}

Because this is pretty close to the max current that the R1801K has access to (4.8V/1MΩ = 4.8uA), I'm pretty happy with the performance of this chip even though it couldn't overcome the leakiness of my capacitor. I now also have to think about alternative energy storage methods like SMD solid-state batteries, which are a lot less straightforward to buy. But hey, limitation breeds creativity. 

# Big picture

I'm currently working on an energy harvesting device for my Hackaday talk coming up in November, and in the process I need to evaluate a bunch of the elements of an energy harvesting device (solar/RF/thermal, harvesting chips, storage methods, low-powered microcontrollers, communication methods). I don't think it'll be worth it to try out everything from every category, but I still love testing out chips just to make sure they do what they say on the tin. Anyway, cya later!
