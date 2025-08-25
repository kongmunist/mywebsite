title: Chargerless
date: 2025-08-23
label: project
timespan: Jan 2025-now
pic: chargerless/beaut.jpg
description: Why Chargerless?

Hello!

This post is going to be a bit of a departure from my other posts. Usually I write up a project after it's done, but this time I'm going to explain it to you as it's happening because I think this time I think it's going to take years to finish. Check out the website at [chargerless.xyz](https://chargerless.xyz/)

{{ add_pic("chargerless/beaut.jpg", "") }}

<br>
<hr>

# Chargerless Manifesto

Between 20-40% of the US adult population owns a fitness tracker, and I haven't met a single person who likes how they look. At best the wearable is tolerated, "discreet <i>enough</i>" ; at worst it sticks out like a stain on a nice white shirt. 

{{ add_pic("chargerless/clunky.avif", "Chunky, chunky, chunky") }}
<br>

But do wearables today "earn their keep" through their functionality in spite of how they look? No! Outside of the top 1% most fitness-brained users, I'd argue that everyone else mostly uses it to check the time. That is, when their device isn't dead.


What's up with this? If everyone is wearing ugly bricks on their wrists, why hasn't anyone showed up with a nice, sleek, "looks like jewelry" wearable yet? The answer is an old way of thinking about the core component that all wearables share: the battery.

<br>
{{ add_pic("chargerless/allbats.jpg", "Oops! All Battery") }}
<br>

It goes something like this: the engineers say "this feature needs this much power per day", and the designers say "this should only get charged once a week", then they ship the product. Since everyone has access to the same battery technology, this means that today's wearables all carry around 200mAh of lithium to power their sensor and communication stack, which is why they're all the same size and can barely last a week.

Can we do better?

<br>
<hr>
# Going Chargerless

Chargerless is a rethinking of the way personal devices have always been powered. Instead of making the user top up their watch every day, what if wearables charged themselves just by being worn around? What if, like the previous generation of self-winding watches, our wearables could power themselves using the heat or light or motion they see every day? 

{{ add_pic("chargerless/handshot.jpg", "") }}

First, it'd be incredibly convenient to never worry again about charging your watch. And as a second order effect — if your wearable is always charging, we can use a much smaller battery to get the same functionality that we're used to: heart rate, sleep, and activity tracking without any of the hassle.

{{ add_pic("chargerless/beaut.jpg", "") }}
<br>

# Why now?

Energy harvesting has been studied for decades, but only recently have low-power microcontrollers caught up. The current generation of chips can run sensors, process data, and transmit signals wirelessly, all from a silicon chip smaller than a salt grain — the primary limitation is a way of thinking about power: how to use it and where it comes from. 

{{ add_pic("chargerless/smallenough.jpg", "") }}
<br>

### Now is the right time:

- tech for tech's sake is out, the people want the functionality but don't want the "device" look
- personalized health is gaining mass appeal but wearable trackers still look cold and bulky to non-tech audiences
- smaller designs which solve this are enabled by our power harvesting stack and modern advancements in semiconductors, alleviating the primary pain points of wearables (low battery, bad aesthetics)
- truly continuous biometrics data integrated across data sources can revolutionize medicine, and you can't get data from the past, we must start now

<br>
# Financials
A 2019 Pew Research [survey](https://www.pewresearch.org/wp-content/uploads/2020/01/FT_2020.01.07_FitnessTracker_Methodology-_Topline_final.pdf) reports that 21% of US adults regularly wear a fitness device. Applied to the US, we get ~70 million devices today. Chargerless is more fashionable and convenient to use than any existing tracker, appealing to both current fitness tracker users and non-users. But how many people is that? 

An [NIH study](https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-017-4888-1) reports about 40% of ex-users quit wearing a tracker because they disliked the aesthetics or short battery life of their wearable. If only 10% of those users switch to Chargerless, that is 2.8 million users, amortizing over the device lifetime to ~280M ARR. Lower bounding at a 10x revenue multiple, this will be a company valued at 3B. 

This is without accounting for any non-users who decide to use a fitness tracker that looks good and functions "for free". The numbers on this one are harder to estimate, but I think it's pretty clear that many people are interested in fitness tracking but unwilling to deal with the hassle presented by today's products. Those people would enjoy Chargerless.    

<br>
<hr>
# Why you?

{{ add_pic("chargerless/andy.jpg", "") }}

My name is Andy Kong, welcome to my website! 

- I previously worked a lot on EE/CS at CMU, ETH Zurich, and MIT, with a research focus in biosensing (EKG, EEG, EMG, eye tracking), energy harvesting, and micropower devices
- I have ~4 years experience working in top HCI labs, where I learned a lot about human-centered design and PD
- I love wearables and other personalized health data (tracking since 2017!), and I think data-driven personalized data analysis is the future of health. 

I'm the only person I know at this intersection, and if you know someone else I'd love to meet them! My email is andy at [chargerless.xyz](https://chargerless.xyz/)

<br>
# How's it going?
It's going great, but there's a lot to do!

Chargerless was started ~fall 2024 as a series of disconnected experiments; Digikey deep dives, napkin math, and de-risking various pieces of the puzzle. The vision coalesced around January of this year, then in July I incorporated and moved to SF to work on Chargerless full-time. 


{{ add_pic("chargerless/stabby.jpg", "Programming some test boards") }}
<br>

We're making strong progress thanks to our early angel investors. Today, all the technical components have been derisked, and we are currently integrating the hardware and embedded into one tiny package. At our current rate of development, we'll have 100 beta devices ready by November 2025 to send out to a select group for tuning and testing — around the same time, preorders will open for the first public offering shipping next summer.


## The Future
Once the beta devices are out the door, our next target is getting >10k preorders.

I'm writing this on August 24, 2025. I'm looking to raise a bit more money and close the pre-seed so I can front costs for development and focus on shipping first devices. I'm currently spending most of my time on the technical side, so I'm looking for a product person to take the time to really nail down the brand / marketing of this company. And I'd also like to move quicker on other deliverables (app, website, database), looking for some help on that front. 

If you'd like to get in on the first 100, reach out @oldestasian or andy at [chargerless.xyz](https://chargerless.xyz/)

