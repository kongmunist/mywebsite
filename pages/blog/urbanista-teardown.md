title: "Teardown of the Urbanista Los Angeles headphones"
date: 2026-02-01
label: log
tags: [electronics, teardown]
snippet: "Removing another self-powering device from the world"

Hello all, it's certainly been a while since my last post so I thought we'd do something fun. Because of my current startup, I'm really interested in consumer electronics which can power themselves. I've only found a few devices like this, and today we're gonna take one apart to see how they're implementing it.

# Background

We're currently in a battery-powered era of devices, driven by the cheap availability of rechargable, high density lithium batteries. However, as the chips powering these devices get more efficient, environmental energy sources like light or heat become a large enough source of power to contribute meaningful amounts of power to the device's battery life. Today, electronics that add energy harvesting can 2-3x battery life over pure battery-operated ones, especially if the duty cycle is low. 

The development of light-harvesting products specifically is driven by the availablility of flexible, "normal"-looking PowerFoyle solar cells by a Swedish company called Exeger. Light-harvesting electronics require a minimum power (light level) to harvest properly, and the minimum light level is higher the smaller the photovoltaic cell. PowerFoyle's cells are optimized for indoor harvesting so even dim indoor lighting can make it work, and the consumer device with the most area turns out to be headphones.

{{ add_pic("urbanista-teardown/0.jpg", "") }}

Since we all work in the same space, I felt compelled to get one and test their panels myself. Exeger has partnered with a lot of big brands like JBL and Adidas, but the cheapest device I could find on eBay was a refurbed/stolen pair of Urbanista Los Angeles headphones.

{{ add_pic("urbanista-teardown/1.png", "") }}

My interests lie mostly in the PV cell and the harvesting methodology, but I'm always interested to see how people make certain mechanisms at scale. The rest of this post will mostly be pictures.

# Teardown

Here's the device

{{ add_pic("urbanista-teardown/2.png", "") }}

Here's the panel we're after, built into the top band

{{ add_pic("urbanista-teardown/3.png", "") }}

We start by popping off the pieces of the device that are snap-fit — The inner band, parts of the outer band, the earmuffs. You can immediately see they've strain reliefed the cable on the headband

{{ add_pic("urbanista-teardown/4.png", "") }}

There's a couple of stickers keeping the band together, once those go the PV cell just falls out 

{{ add_pic("urbanista-teardown/5.png", "") }}

{{ add_pic("urbanista-teardown/6.png", "") }}

I used a clamp to pop off the two outer shell bits on the headphone themselves. The right one contains the harvesting and bluetooth chips (labeled on paper), and 2 mics for the noise-cancelling. 

{{ add_pic("urbanista-teardown/7.png", "") }}

The left earmuff has a 750mAh battery (10 kJ), PMIC, and 1 mic. I roughly calculated charging rate in direct sunlight and came up with 3-4 hrs to go from 0 to 100%.

{{ add_pic("urbanista-teardown/8.png", "") }}

The part of the band coupling to the earmuffs (for the wire pass-through) is made of steel, which I found a bit surprising — its the only mechanical component that's made of metal in the whole device. Actually I felt a bit bad seeing how good the build quality was during the teardown. It was taken apart in a way that could be put back together, but I'm not really interested. 

# Analysis

From my brief research into this, Exeger bought another company called Sunboost which was also nordic in origin, and this is the harvester chip that's labeled SUNBST. Exeger also likes to partner with e-peas, a Belgian chip company. For now I don't have more info, so I'll just leave this section a stub. 

# Conclusion

Two interesting realizations I had during this:

1. The amount of power available in the environment (heat/light) has been fixed for millenia, but our devices have become steadily more efficient. The next generation of devices will not need charging, the one after that will not even need energy harvesting.

2. All devices trend smaller over time, except for things that must conform to the human body (headphones, gloves, bracelets). All tools are made small to the extent that people can still manipulate and use them effectively.


My review of the Urbanista Los Angeles headphones: Excellent build quality, decent noise cancelling, slightly uncomfortable and cheap earmuffs. Panel testing will come in a later
