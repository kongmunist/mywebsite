title: Chargerless Manifesto
date: 2025-08-23
label: project
timespan: Jan 2025-now
pic: chargerless/beaut.jpg
description: Why Chargerless?

[//]: # (Hello! Usually I write up a project after it's done, but this time I'm going to explain it to you as it's happening. Check out the website at [chargerless.xyz]&#40;https://chargerless.xyz/&#41;)

{{ add_pic("chargerless/beaut.jpg", "<a href='https://chargerless.xyz'>Chargerless</a>") }}


Between 20-30% of the US adult population owns a fitness tracker, and I haven't met a single person who likes how they look. At best, wearables are tolerated, "discreet <i>enough</i>" ; at worst it sticks out like a stain on a nice outfit. 

{{ add_pic("chargerless/clunky.avif", "Chunky, chunky, chunky") }}
<br>

But do wearables today "earn their keep" through their functionality in spite of how they look? No! Outside of the top 1% most fitness-brained users, everyone else mostly uses it to check the time. That is, when their device isn't dead.


What's up with this? If everyone is wearing ugly bricks on their wrists, why hasn't anyone showed up with a nice, sleek wearable yet? The answer is an old way of thinking about the core component that all wearables share: the battery.

{{ add_pic("chargerless/allbats.jpg", "Oops! All Battery") }}

It goes something like this: the engineers say "this feature needs this much power per day", and the designers say "this should only need charging once a week", then they ship the product. Since everyone uses the same battery technology, this means that today's wearables all carry around 200mAh of lithium to power their sensor and communication stack, and end up at a similarly sized package.

Can we do better?

<hr>
# Going Chargerless

Chargerless is a rethinking of the way personal devices have always been powered. Instead of making the user top up their watch every day, what if wearables charged themselves just by being worn around? What if, like the previous generation of self-winding watches, our wearables could power themselves using the heat or light or motion they see every day? 

{{ add_pic("chargerless/handshot.jpg", "") }}

First, if your device charges itself all the time, we can get the same functionality using a much smaller battery; sleep, exercise, health tracking without any of the hassle. Ane secondly, your device would never die again — how magical is that?

{{ add_pic("chargerless/beaut.jpg", "") }}

# Why now?

Energy harvesting has been studied for decades, but only recently have low-power microcontrollers caught up. The current generation of chips can run sensors, process data, and transmit signals wirelessly, all from a silicon chip smaller than a salt grain — the primary limitation is a way of thinking about power: how to use it and where it comes from. 

{{ add_pic("chargerless/smallenough.jpg", "") }}

<br>

# So what?
You might be wondering why I'm so eager to build a fitness tracker if today's people only use it to check the time — it's because Chargerless will be so much more than that. Today's devices offer "health insights" but the data is so limited they can basically only calculate sleep scores. Humans are so much more than that — we constantly emit data about our cognition, mental energy levels, or mental state, and one of the goals of Chargerless is to cast a wider net to get that bigger picture view of your health, mind and body.

Bryan Johnson obviously has someone analyzing his biometrics data, and in the near future AI can offer this analysis to anyone. But you can't get data from the past, we must start now, and do it by removing any reason to not have a device. This means smaller designs enabled by our power harvesting stack, and an infinite battery life when others are quibbling over weeks and days.

{{ add_pic("chargerless/glowing.jpg", "") }}

<hr>

# Financials
A 2019 Pew Research [survey](https://www.pewresearch.org/wp-content/uploads/2020/01/FT_2020.01.07_FitnessTracker_Methodology-_Topline_final.pdf) reports that 21% of US adults regularly wear a fitness device. Applied to the US, we get ~70 million devices in circulation and a market size of ~80 B ([source](https://www.grandviewresearch.com/industry-analysis/wearable-technology-market)). 

The Ray band is intended as both a first product in this space and a replacement device for existing fitness users — we will grow the pie and take a big slice. The top two quitting reasons for fitness users are the aesthetics (~20%) and battery life (~18%), which are an entangled problem solved by our new device, and conversions on existing users can easily hit ~14M users. New users will be a larger component than other wearables given the social advantages of the Ray, and this plays into marketing as well.


[//]: # (. I'm extremely excited to boost average health across the population, and have it done effortlessly. )

# Marketing

Our target audience is primarily people in their mid-20s to late 40s — with friends and family members to care about and keep up with through day-to-day wellness. A lot of outreach will happen via word-of-mouth, gifts, being active on forums, and social media. Traditional web media will also play a big role for the slightly older end of our target audience. We think this will work well for two reasons. 

1. More data, more insights. Today's trackers can tell your sleep impacted your day, but not much more, which makes it hard to justify their annoyance. We want to do more than that, to expand the data sources that a user can analyze and self-improve upon, and deliver novel insights across the mind-body axis for a higher value user experience. 
2. Chargerless is the first fitness and health for everyone. As a gift to your parents, grandparents, or kids, it is the only device which feels more like an object than a responsibility because it works "for free" and has a minimal look. We'll focus marketing on families and friend groups, which we believe is a great way to get people to care about their health, and is an angle in which Chargerless is outstanding. 



 
[//]: # (<hr>)

[//]: # (# Why you?)

[//]: # ({{ add_pic("chargerless/andy.jpg", "") }})

[//]: # ()
[//]: # (My name is Andy Kong, welcome to my website! )

[//]: # ()
[//]: # (- I've previously worked at CMU, Google, ETH Zurich, and MIT, with a research focus in biosensing &#40;EKG, EEG, EMG, eye tracking&#41;, energy harvesting, and micropower devices)

[//]: # (- I have ~4 years experience working in top HCI labs, where I learned a lot about human-centered design and PD)

[//]: # (- I love wearables and other personalized health data &#40;tracking since 2017!&#41;, and I think data-driven personalized data analysis is the future of health. )

[//]: # ()
[//]: # (I'm the only person I know at this intersection, and if you know someone else I'd love to meet them! My email is andy at [chargerless.xyz]&#40;https://chargerless.xyz/&#41;)

<hr>
# How's it going?
It's going great, and there's a lot left to do!

Chargerless was loosely started ~fall 2024 as a series of disconnected experiments; Digikey deep dives, napkin math, and de-risking various pieces of the puzzle. The vision coalesced around January of this year, then in July I incorporated and moved to SF to work on Chargerless full-time. 

{{ add_pic("chargerless/stabby.jpg", "Programming on test boards") }}

We're making strong progress thanks to our early angel investors — technical derisking is finished, and integration is well underway. At our current rate of development, we plan to ship out 100 beta devices to paid users by November 2025 for tuning and testing (list is ~80% full, please DM me if you'd like to join the list!). The next time you'll be able to get one will be the first public batch around next year.

Keep up on our [twitter page](http://twitter.com/chargerlessxyz) or by joining our newsletter!






[//]: # ()
[//]: # (## The Future)

[//]: # (Once the beta devices are out the door, our next target is getting >10k preorders.)

[//]: # ()
[//]: # (I'm writing this on August 24, 2025. I'm looking to raise a bit more money and close the pre-seed so I can front costs for development and focus on shipping first devices. I'm currently spending most of my time on the technical side, so I'm looking for a product person to take the time to really nail down the brand / marketing of this company. And I'd also like to move quicker on other deliverables &#40;app, website, database&#41;, looking for some help on that front. )

[//]: # ()
[//]: # (If you'd like to get in on the first 100, reach out @oldestasian or andy at [chargerless.xyz]&#40;https://chargerless.xyz/&#41;)

