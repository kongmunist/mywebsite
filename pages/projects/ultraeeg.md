title: Brain Hack 2
date: 2024-12-26
label: project
timespan: August 2024
pic: ultraeeg/brainhack.png
description: Taking the best of tFUS and EEG

<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

{{ add_pic("ultraeeg/brainhack.png", "Muscle contraction test on Myo2 boards") }}

Hi! This post is gonna describe the Ultrasound+EEG project I worked on as part of Brain Hack 2 hosted by [Marley](https://www.marleyx.com/) and [Raffi](https://www.rhotter.com/)

- Proper [writeup](https://brainhack.vercel.app/ae)
- Layman description [on Twitter](https://x.com/_marleyx/status/1845999421542334608)

<hr>

# Background
## Muscles
My first circuit board measured the electrical signals thrown off by muscles as they tense and flex, amplifying a small voltage on the surface of the bicep 10,000x so I could see it on the oscilloscope, a quantification of my body working as it had for many years. This marked the beginning of my exploration into biosignals and what we could communicate to a computer through our movements.

{{ add_pic("myo2output1.png", "") }}

## Brain
Later I moved to EEG because I thought it would be cool to think and have my computer pull up information for me. Brain signals are 10-100x smaller in magnitude than muscle signals, and coupling an electrode to the scalp through the hair was way harder than simply sticking 3M red dot electrodes onto the arm. I had a lot of trouble getting useful signal, so I went searching through the literature.

{{ add_pic("ultraeeg/initialeeg.jpeg", "OpenBCI Ganglion kit for measuring EEG") }}

There's many ways to look into the brain without opening it. You can use light (fNIRS, optogenetics), voltages on the scalp (EEG), magnetic fields right outside the head (MEG), magnetic fields inside the brain (fMRI), or many more. But the trouble with all of these is that the brain cannot be touched. It's kinda like that guy who got his cylinder stuck in a M&Ms container but refused any unstucking methods that could damage it — how can you get better signal resolution out of a source that cannot be harmed or isolated or altered without fundamentally ruining the original point to all the sensing? Anyway, from all this I learned that the methods that could exactly see WHEN a cluster of neurons fired (EEG, MEG) were terrible at figuring out where that cluster was, whereas the approaches that were really slow to react (fNIRS, MRI) could tell you exactly where neurons were firing. What a crazy world!

{{ add_pic("ultraeeg/SSVEP.jpg", "My SSVEP setup, operating from ~10-20Hz") }}

I did read about a technique called lock-in amplification, which claimed to be able to pull nanovolt signals out of the noise floor, but it required the signal to be modulated by some reference signal. Since I couldn't figure out a way to modulate the brain signal inside my head, I tried instead to lock onto the stimulus frequency (a lamp flashing at 10Hz). This technique doesn't work so well at low frequencies, and the brain is not a reliable function generator anyway, so that didn't work. Shortly afterwards I gave up on EEG entirely.

<hr>
# Fast forward 3 years
After that project, EEG was completely and totally dead as far as I was concerned — I saw no way to get good signal non-invasively. But 2024 was a magical year. One day in August as I was about to leave San Francisco, a friend (Marley) mentioned a signal processing problem involving EEG they were scoping out, and would I like to come over and think about it together? And what they revealed to me had the potential to become EEG's salvation. 

As mentioned before, EEG's resolution could be enhanced by modulating brain waves at a certain frequency, then using a lock-in amplifier to extract the signal. This works just like a car radio — every station is always broadcasting, but your radio decides what frequency to pick up on. The technique goes by many names (lock in amplification, heterodyning, synchronized detection), but basically it lets you pull signals deep, deep in the background noise — all you needed was a way to modulate biosignals. 

<p class="caption">Modulation shifts the original red signal to the blue signal, where it can be recovered above the noise floor <a href="https://www.edn.com/design-a-dsp-lock-in-amplifier-part-1-background/">(source)</a></p>
{{ add_pic("ultraeeg/edn.gif","") }}

What Marley and Raffi had found in the literature was an approach to modulate electrical biosignals by physically compressing the tissues the biosignals passed through using focused ultrasound energy. It's called the acousto-electric effect, or AE; by applying ~1MPa of pressure, tissues would typically change resistitivity by ~0.1%, allowing us to use the ultrasonic signal as the modulator for locking onto EEG waves. This wasn't even a theoretical technique — it had been done on the heart to image cardiac currents [(In vivo acoustoelectric imaging for high-resolution visualization
of cardiac electric spatiotemporal dynamics)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8569939/pdf/nihms-1696551.pdf). 

<p class="caption">A map of the peak voltages at different areas of the heart, produced using the acousto-electric effect  <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8569939/pdf/nihms-1696551.pdf">(source)</a></p>
{{ add_pic("ultraeeg/cardiacae.png","") }}

Not only did this give us a method for higher-resolution EEG, it also meant we could read a much denser resolution of EEG. Since ultrasound can be focused down to a tiny \\(<1mm^3\\)spot, if we stimulated just one section of the brain we would be able to decode the activity from just that part. Spatial resolution of tFUS and the time resolution of EEG — I was hooked.

We did the math on a whiteboard. 0.1% change in resistivity on top of a ~10-100uV neural signal means we would be hunting for a 10-100nV signal hidden within the typically ~1-3 V raw amplified EEG signal. Totally possible with the lock-in! I moved my flight by a week and joined their quest. 

<hr>
# Brain Hack 2
Our hackers were situated in a beautiful house in Mill Valley, half an hour north of SF in a quaint old house with a painting of the OG homebuilder. We turned it into a lab as soon as we got there. The TV stand became the 3D printer table, the big dining table was claimed by team skull, and the living room table became the dominion of team AE. 

{{ add_pic("ultraeeg/house.jpeg","Just a side house of the main house") }}

{{ add_pic("ultraeeg/raffiyawning.jpeg","Team tFUS") }}
{{ add_pic("ultraeeg/teamaedominion.jpg","Acousto-electric living room") }}

Closets were filled with deionized water, and a huge pot was constantly being boiled and cooled in order to produce degased water, a required medium for the ultrasonic transducer to not blow up. Every day Amazon packages arrived, bottlenecks lifted, and the team would make progress until we could no more. It felt like a skunkworks. It was heavenly.

{{ add_pic("ultraeeg/skullwifhat.jpeg","") }}

# Process
I think most "science" is pretty straightforward engineering. Get it working in ideal settings, then replace ideal components with non-ideal ones, one at a time. 


{{ add_pic("ultraeeg/allmachinesandmarley.jpg", "Function generator for the ultrasonic transducer, oscilloscope to see the ultrasonic microphone, lock-in (SR860) for demodulating the AE signal, and Marley for head scratching") }}

First we tested all the equipment. Does the lock-in report a tiny attenuated signal when we divide the function gen output by a million? Does the ultrasonic transducer work, and does the ultrasonic mic pick it up? 

{{ add_pic("ultraeeg/momsaiditsmyturnonthelockin.jpg", "I loved the lock-in. You would tell we were a real group of nerds because as soon as it arrived we were all vying to be the first to read the manual. 
") }}


Once all the components are working we started on the real thing. Here were our rough milestones:

1. AE working in saline
2. AE working in saline, and we pick up a DC signal running through the ultrasound's focus
3. AE working in saline, and we pick up an AC signal running through the focus
4. AE working in muscle
5. AE working in muscle, and we pick up flexing
6. AE working on brain

We made it to step 4.

<hr>
# Learnings

I didn't keep good notes on the process, and now it is several months after the hack. All I have remaining are the struggles that we overcame and the lessons we learned. In no intentional order:

1. Using the function generator to drive the ultrasonic transducer directly works great.
2. Saline solution (0.9% salt) has similar properties to human tissue w/r/t the acousto-electric effect, so you can use it for testing AE
3. Saline is conductive, and most coaxial cables are not waterproof. This means that the driving signal for the ultrasonic transducer can weakly conduct through the saline to get picked up (on the order of ~5-30M). This is deceptive because it looks like the AE signal, but is actually electrical and not acoustic. To solve this, we encapsulated the transducer in a latex balloon filled with mineral oil, which doesn't affect the ultrasonic propagation {{ add_pic("ultraeeg/balloon.jpeg", "") }}
4. One way to ensure your signal is acoustic and not electrical is to look at the delay between driving signal and receiving signal. Acoustic signals are limited by speed of sound in the medium (50-100us), while electrical happens instantly {{ add_pic("ultraeeg/drivesignal.jpeg","") }}
5. Ultrasound can be focused using any physical shape, for instance a cone. It kinda just matters the hardness of the material, I think. We tried using orbeez cut into cones, wax molded into a cone, silicone cone, and finally went with a 3D printed one. {{ add_pic("ultraeeg/carrotlens.jpeg", "") }}
6. 3D printers have come so far. Our Bambu was running nearly the whole time, and every print was necessary or saved us a lot of janky work holding. I'm beginning to enjoy 3D printing a holder for everything
7. Working with other skilled engineers is a joy I hope everyone gets to experience. Your expertise is generally spiky, and in a group those spikes balance out to make a glorious, fast-rolling circle down progress lane. Made great friends with [Ethan](https://x.com/BigCrete) on this trip {{ add_pic("ultraeeg/menethan.jpeg", "") }}
8. On most multi-channel function generators, there exist nanovolts of leakage between the outputs. Typically there is nothing wrong with this, except for the edge case where your signal is in the nanovolts. Oops!! Just buy a 2nd function generator. 
9. You can buy skulls for 2000 USD online, and their reward points are denominated in "bones"
10. Being away from the usual location is like staying up to work without social distractions, but 10x better. I thought it was a bit wasteful to just go half an hour away for this, but it really puts you in a hackathon mindset. Loved the house also, Mill Valley is a beautiful area. {{ add_pic("ultraeeg/house!.jpeg", "") }}
11. You can boil bones, in fact you have to if you want to put ultrasound into them. Cause in real life they're wet, so you gotta make them wet to show the proper propagation. 
12. Bambu printers have high speed settings, and they even have ludicrous mode. These are named the same as the Tesla speed settings, but they don't go up to Plaid, which is a reference to Spaceballs, which is a parody of Star Wars, both of which I have never seen.
13. If you put a mini-projector on a gimbal you can create a new way to be online. {{ add_pic("ultraeeg/brian.jpeg", "") }}
14. Modern lock-in amplifiers allow you to lock onto a specific frequency, but in case you're off by a few Hertz or don't know where to look, they also offer the option to sweep their modulation frequency across a range. This gives you a clearer signal than simply picking one frequency. 
15. Morale is a real thing. There is still room for fun and relaxing after a day's sprint, even if the task seems impossible. I don't know if I can implicitly budget this in yet, but Marley and Raffi and everyone else included time for it very naturally.
{{ add_pic("ultraeeg/latenights.jpeg", "") }}


# Conclusion
I used to be extremely stubborn, wanting to be the one to choose a project that I decided was important. This year I've worked on three large projects (PoS, this, Open Quantum), each showing me that it was actually more important that I loved the people I worked with. If I love waking up and going in, then I could do anything. So even with that knowledge, I'm blessed that this project team contained only amazing people and still could've been a project I'd chosen myself. 

External EEG seemed so impossible for many years, and now I have hope. That too is a magical thing. 


# More, please!

And finally, working on this a) hard/nearly impossible problem with b) minimal resource constraints, c) a team of competent, fun people under a d) tight timeline has been a peak experience in my life. If you have a similar problem which fulfills at least a, c, and d and needs some help on the prototyping/research/EE/signals/ML/CV/problem solving/thinking/minimum viable solution side, I am your man and would love to join. Please reach out!


{{ add_pic("ultraeeg/goodworks.png", "") }}