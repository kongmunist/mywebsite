title: Ultrasonic EEG
date: 2024-12-26
label: project
timespan: August 2024
pic: ultraeeg/realhumanskull.jpeg
description: Combining the best of tFUS and EEG

Spatial resolution of tFUS + time resolution of EEG. WIP since Dec 27 2024

My first circuit board measured the electrical signals thrown off by muscles as they tense and flex, amplifying a small voltage on the surface of the bicep 100,000x so I could see it on the oscilloscope, a quantification of my body working as it had for many years. This marked the beginning of my exploration into biosignals and what they meant about the body. 

Later I worked with EEG, starting and stopping with the OpenBCI Ganglion. This board is essentially the Texas Instruments ADS1299 chip with some nice software integration, and the data is completely useless. I'm not sure if the board is useless or surface EEG is useless — either way, the signals were small and difficult to see. Brain signals are 10-100x smaller than muscle signals, and coupling an electrode to the scalp through the hair was harder than sticking 3M red dot electrodes onto the arm. To find better signal, I went searching through the literature.

There's many ways to look into the brain without opening it. You can use light (fNIRS, optogenetics), voltages on the scalp (EEG), magnetic fields right outside the head (MEG), magnetic fields inside the brain (fMRI), or many more. But the trouble with all of these is that the brain cannot be touched. It's kinda like that guy who got his cylinder stuck in a M&Ms container but refused any unstucking methods that could damage it — how can you get better signal resolution out of a source that cannot be harmed or isolated or altered without fundamentally ruining the original point to all the sensing? Anyway, from all this I learned that the methods that could exactly see WHEN a cluster of neurons fired (EEG, MEG) were terrible at figuring out where that cluster was, whereas the approaches that were really slow to react (fNIRS, MRI) could tell you exactly where neurons were firing. What a crazy world!


There was a technique called lock-in amplification which claimed to pull nanovolt signals out of the noise floor, but it required the signal to be modulated. Since I couldn't figure out a way to modulate the brain signal, I tried instead to lock onto the stimulus frequency (a lamp flashing at 10Hz). This technique doesn't work so well at low frequencies, and the brain is not a reliable function generator anyway, so that didn't work. Shortly afterwards I gave up.

# Fast forward 3 years








