title: "Testing out the BPW34"
date: 2024-03-04
label: blog
tags: [electronics, solar, micropower]
snippet: "Tiny experiments with a tiny solar cell"

{{ tableofcontents("blog/testingbpw34.md") }}

Hello! Did you know solar cells work even through skin? More on that later.

Today I'm going to show you some basic testing I did with the BPW34. This is technically a photodiode (for detection), but as we know, photodiodes work both ways.

{{ add_pic("testingbpw34/0.png", "") }}


# BPW34 Description

These are sold on SparkFun as miniature solar cells, and I wanted to see how much power I could pull out of them in ambient light. 

{{ add_pic("testingbpw34/1.png", "") }}

The reported open-circuit voltage is 350mV, so two in series should be enough to drive an energy-harvesting PMIC. We may even get away with just using one and a dedicated solar cell harvester IC, but I didn't have any of those on hand. Also, the more the merrier!

I looked on Digikey for similar photodiodes (just find the BPW34 and then trace back what product category it fits into), and found plenty. There are alternatives, but none go much higher than 300mV (though they might be of photon->current higher efficiency). Watch out also, some have a daylight blocking filter which stymies their usage as solar cells.

{{ add_pic("testingbpw34/2.png", "") }}

Here's how big it is. 

{{ add_pic("testingbpw34/3.png", "") }}

If you're using it for power harvesting, the positive terminal is the leg with a single stripe of metal (where the probe is clipped in this photo)

{{ add_pic("testingbpw34/4.png", "") }}

# Voltage under no light

I put one in a black bag just for fun and got >70mV, which is not a lot, but not zero. I think this is from light leakage into the bag, but it gets an awfully small amount of light for a pretty decent voltage. You know the old saying, 5 in a bag is worth 1 in the air. I didn't try drawing power from it like this, but it should not provide very much. 

{{ add_pic("testingbpw34/5.png", "") }}

# Voltage under some light

Indoors near a large window I get >300mV no-load from a single diode. This varies from 290-350mV, depending on if the diode faces the window or not. 

{{ add_pic("testingbpw34/6.png", "") }}

# Voltage under lots of light

I blasted one with my phone flashlight and the voltage goes over 500mV. When the flashlight LED is held directly over the photodiode, I max out at 600mV. I couldn't take pictures of this since I was using my phone's flashlight, so you'll have to trust me, bro.

# 2 in series, some light

I wanted to make sure the diodes actually do add in series so I soldered two together. In ambient light they add up as expected. 

{{ add_pic("testingbpw34/7.png", "") }}

# 2 in series, some light, through skin

I read [this paper](https://www.sciencedirect.com/science/article/pii/S0956566316311320) which reported that fresh human skin transmits a lot of light in the spectrum of 700nm and up, allowing subdermal electronics to be powered by light exposure.

{{ add_pic("testingbpw34/8.png", "") }}

{{ add_pic("testingbpw34/9.png", "") }}

I did a very rudimentary test of this by covering the two diodes with my thumb. While I'm sure this is mostly leakage light from the sides of the diodes, I do get ~half the voltage.

{{ add_pic("testingbpw34/10.png", "") }}

The paper tried this using a thin skin sample (1-2mm); my thumb is a quite a bit thicker than that so I expected way less voltage than just half. 

# Expected voltage vs. skin thickness
 
We can compare the fresh "Upper inner arm" 1mm sample with the fresh "Forehead" 1.5mm sample — transmittance goes from ~0.56 to 0.28 at 800nm, so the relationship between transmittance and thickness is nonlinear. 

{{ add_pic("testingbpw34/11.png", "") }}

However, if we compare shoulder and forehead, we get totally different transmittances at 800nm despite the similar thickness. From [this paper](https://pubmed.ncbi.nlm.nih.gov/14690333/), the shoulder epidermis is 11mm thick and in [this paper](https://www.selcukmedj.org/uploads/publications/2022-102-13168603.pdf) the forehead epidermis+dermis thickness is 0.07mm and 1.6mm. Because the shoulder sample is mostly epidermis and the forehead sample is mostly dermis, I think the dermis is doing most of the light blocking here. I conclude that the forehead (and face in general is not a great place to put implanted solar cells. 

Anyway, that's all the testing I've done so far. Open-circuit voltage is not power, but this high of a voltage is enough for energy harvesting, however slowly that may happen. Let me know if you explore this any further!

Cya next time!
