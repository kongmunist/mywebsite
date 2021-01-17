title: EEG fails in the prescence of household EMI
date: 2021-01-17
label: blog
tags: [eeg, bci, emi, thoughts]
snippet: I am beginning to have doubts on the feasibility of everday BCIs...

Hello!

Yesterday I ran several experiments on my EEG (electroencephalography) headset. You always start with something you know is working — in this case, I checked the impedance (low, 10kΩ instead of the usally 400kΩ), then performed the closed-eye alpha spike test (check [here](../bcieyeclosedetection) if you don't know what I'm talking about). It worked, so I moved on to trying to evoke an SSVEP with a 15Hz flashing light. I had just built this structure for blinking 3W LEDs that looks vaguely like an apartment front architecture student would have to design in a class, and it worked wonderfully. The SSVEP is evoked most strongly from 10-20Hz, with a peak around 15Hz. I used 15Hz, and the peak was as large as the closed-eye alpha waves, which are the strongest EEG signal discovered. Basically, it was working fine. 

<p class="caption">Picture of the apartment-shaped blinker, Arduino controlled MOSFETs and a CC source made from 1W resistors and an LM317 to drive the big LEDs.</p>
![Picture of the apartment-shaped blinker, Arduino controlled MOSFETs and a CC source made from 1W resistors and an LM317 to drive the big LEDs.]({{ url_for('static', filename = 'aptblinker.jpg')}})

At this point my laptop began running low, so I plugged it into the wall. The next 2 hours I spent running experiments, trying new signal averaging techniques. However, none of them seemed to be working — there was this constant randomness to the signal. Since I had just checked whether the headset measured EEG properly, I thought for sure that new technique just didn't work. I made the experiments simpler and simpler, and eventually I went back to doing the closed-eye thing. Guess what? Our nice consistent graphs had tanked, and were now noisy as hell with the peak barely discernible. 

I started considering environmental factors, like EMI emission from the things near me. I knew the apartment blinker setup didn't throw off that much EMI — I had put it across the table, and checked to make sure that the 15Hz didn't just spike all the time. Since it had worked earlier, I knew the EMI pick-up was much lower than the SSVEP signal (which is very small, under 10 microvolts). My laptop finished charging, so I unplugged it and tried my alpha test again. And it worked perfectly :(. It was the charger! 

<p class="caption">Still from the video "Removing RFI Noise from MacBook Power Supply
"</p>
![Still from the video "Removing RFI Noise from MacBook Power Supply
"]({{ url_for('static', filename = 'macbookrfi.jpg')}})

I'm no expert, but modern laptop chargers pass a huge amount of DC current from the AC wall, and usually convert it using a switching power converter instead of a linear DC converter. They're usually more efficient (80% vs 60%), which you care about when you're passing 80+ watts to charge a computer battery. However, they generate a lot of high frequency noise because they have to switch constantly, on and off, to produce a stable current. Most of my info here I read a [teardown by Ken Shirriff](http://www.righto.com/2015/11/macbook-charger-teardown-surprising.html), but I also found a [Youtube video](https://t.co/cDLqXJmekF?amp=1) which shows how to reduce EMI produced by a Macbook MagSafe (though an older version). 

Though the EEG board I'm using doesn't have a physical connection to my laptop, it did sit right next to my laptop as it charged. The Macbook grounds itself to its chassis, which means that there should be some radiated EMI from the casing itself to nearby devices (I can see this on the EEG output as increased 60Hz noise when I touch my laptop — even when it's not plugged into the wall!). Since EEG is so sensitive, I think the proximity to my charging laptop is what did my signal in ;(. Wack!

## Discussion
It's fine that I have to redo the experiments, but my main concern is for the usefulness of EEG in daily settings. I mean, brain-computer interfaces are the future of HCI (in my opinion); they're useless if they can't work in the presence of everyday electrical noise.

I started using the SSVEP because it's a stable, high bandwidth signal, but if the alpha spike can't even function in the presence of noise then I don't know what can. 

<p class="caption">The alpha wave spike when your eyes close is one of the strongest EEG signals</p>
![The alpha wave spike when your eyes close is one of the strongest EEG signals]({{ url_for('static', filename = 'emialphaspike.png')}})

Maybe if we shielded the board it'd be slightly better, but even then the cables have a decent amount of pickup, as does my conductive, sacks-of-saltwater body. Maybe shielded cables and boards will have to be the norm? But then if a person touches the box, it'll still couple noise into the whole system. It seems intractable, considering our power systems are too ingrained to change now, and our brain signals aren't getting any stronger (In fact, if you go on Facebook, they seem to be getting weaker... /s). The future of BCI may not last very long...

