title: "A Layman's Guide To The ICNIRP Guidelines On Limiting Exposure To Electromagnetic Fields (100kHz-300GHz)"
date: 2024-04-15
label: blog
tags: [electronics]
snippet: "I read this and it was actually interesting"

Hello!

In this post I'm going to sum up all the cool things I learned about the human body and the way the body interacts with electromagnetic (EM) radiation. All these facts I learned from a casual perusal of the ICNIRP 2020 guidelines doc, which you can find yourself [here](https://www.icnirp.org/cms/upload/publications/ICNIRPrfgdl2020.pdf).

ICNIRP is an international non-profit made up of random scientists who enjoy quantifying electromagnetic radiation safety. They read the most up-to-date literature every few years and compile a large guidelines doc describing limits of what the human body. These guidelines are then used by researchers and government regulatory bodies to establish safe legal bounds on human-EM exposure.

{{ add_pic("icnirp/0.images?q=tbn:ANd9GcRU1BjWaIRiWqjlAg0-v5DxjXGIe4oHT0SBeN1ke48umQ&amp;s", "") }}

# Why did you need to read this dry and boring safety text?

Recently, I needed to describe the safety of an electromagnetic system that interacted with the human body. To do so, I needed to show that the design conformed to the ICNIRP guidelines — this was a task I had been putting off in case A) the system wasn't actually safe, or B) the guidelines would be complex and hard to understand. 

I was close to giving up in favor of relying on a secondary source's interpretation of the ICNIRP guidelines, but in a moment of clarity, I decided to first give the primary text my best crack. And thank goodness! The text is full of interesting little details, explanations of why the limits are what they are, and the different ways EM radiation can damage the human body. I found the info I needed and got out, but I found the guidelines so interesting that I told myself I'd revisit them after my deadline. 

The rest of this blog will be in list format, interrupted by occasional screenshots. 

<hr>

# Interesting electromagnetic trivia

- ICNIRP only acknowledges three ways EM radiation can harm human tissues: 1) electric fields below 10MHz can stimulate nerves, 2) biological membranes can break down or change permeability in response to sufficiently strong fields, and 3) EM radiation can cause tissue heating.

- At higher frequencies >10MHz, damage from tissue heating (3) happens way before cell permeability changes (2), so we can ignore 2 as long as we respect the guidelines for (3). At lower frequencies <10MHz, nerve activation (1) happens way before the permeability stuff (2), so again we can ignore 2 as long as we follow the guidelines for (1). At 10MHz, changes in permeability kill you immediately (just joking)

{{ add_pic("icnirp/1.png", "") }}

- The frequencies that can affect nerves are limited to ~100kHz and are described by participants as tingling. As frequency increases to 10MHz, this sensation becomes one of "warmth" and we start to care more about thermal safety. Nerve effects are mainly described in the other ICNIRP doc for lower frequencies.

- Waves at a higher frequency penetrate less deeply into human tissues. Because of this, below 6GHz the guidelines are concerned with measuring temperature rise with "specific energy absorption rate" (SAR, W/kg), and above 6GHz they measure temperature rise with "absorbed power density" ($S_ab$, W/$m^2$). 

- Humans' core body temperature is 37°C and can vary up to 1°C throughout a day. Correspondingly, the guidelines try to keep EM radiation exposure below a power level that increases body temperature 1°C (as a conservative limit, they actually try to keep it under 0.1°C). At the 100kHz-6GHz range, a SAR of approximately 6 W/kg leads to a core body temperature increase of 1°C. The issue with increased body temperature is that the heart has to work harder and it causes more accidents

{{ add_pic("icnirp/2.png", "") }}

{{ add_pic("icnirp/3.png", "") }}

- From this we also learn that children can dissipate heat better than adults and therefore have a higher SAR threshold.

{{ add_pic("icnirp/4.png", "") }}

{{ add_pic("icnirp/5.png", "") }}

- ICNIRP also gives us a neat reference for how much power an adult human uses normally. At rest 1W/kg, at stand 2W/kg, and 12W/kg running. I guess this means standing desks actually work?

{{ add_pic("icnirp/6.png", "") }}

- Earlier I mentioned the distinction between surface and deep tissue EM energy absorption. The doc elaborates that at 6GHz, 86% of the power is absorbed in the first 8mm of skin. Surface heating is also less worrisome because we can get rid of it more easily.

{{ add_pic("icnirp/7.png", "") }}

- More tangential trivia, almost all human tissues get damaged beyond 42°C, exhibiting very little interperson variation. To respect this limit, ICNIRP tries to limit localized tissue heating to 41°C. 

{{ add_pic("icnirp/8.png", "") }}

- Extremeties are usually around 33-36°C, while core tissues are closer to 38°. Therefore extremeties are limited in heating to +5°C, while core is limited to +2°C. 

{{ add_pic("icnirp/9.png", "") }}

- Testicles stop making sperm when people sit down because they heat up. I wonder if the increase in desk jobs is responsible for the global decline in sperm count? 

{{ add_pic("icnirp/10.png", "") }}

- They approximate whole-body SAR by using a 10g meat cube. They say the spread of heat in a 10g mass is "close enough" to a larger mass. 

{{ add_pic("icnirp/11.png", "") }}

- ICNIRP wants to limit body temperature rises to 0.1C, because of this they choose a whole-body SAR limit of 0.4W/kg. For civilians who don't know what they're up against, the limit is 5x better at 0.08W/kg. This reduction is a bit arbitrary to me, but I appreciate the safety factor. 

{{ add_pic("icnirp/12.png", "") }}

- Old people sweat 25% less effectively than younger people

{{ add_pic("icnirp/13.png", "") }}

<hr>

It's cool to read these guidelines to see how these large organizations think about risk, and to realize how much harder it would be to spec safety without these guidelines compiling everything.

I also realized that 5G cell phones use frequencies covered by these guidelines (450MHz-6GHz and 24-52GHz). In light of ICNIRP's explanations, people who freak out about 5G affecting their babies don't make much sense — it's just the effects of heating, and our communications are so efficient that the heating is not even significant. 

Anyway, I hope you successfully stay away from dangerous EM waves. Cya next time!
