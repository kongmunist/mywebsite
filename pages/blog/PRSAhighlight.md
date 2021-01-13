title: "New EEG Technique: Phase-rectified signal averaging"
date: 2021-01-13
label: blog
tags: [ssvep, bci, eeg, paperhighlight]
snippet: Basic method of aligning waves helps when averaging out noise from long time-series

Today I'm going to tell you about the technique of phase-rectified signal averaging, or PRSA, applied to EEG signals. I stumbled upon [this](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.160.879&rep=rep1&type=pdf) paper talking about it. Originally the technique was applied to like astronomy data or something, you can find that here, ["Phase-rectified signal averaging detects quasi-periodicities in non-stationary
data"](https://www.sciencedirect.com/science/article/pii/S037843710501006X). This guy who used to be at Philips Research wrote it, he now works at some Mattress company's research department doing sleep EEG to determine how comfy their products are. Interesting career path.

## What's all this PRSA stuff anyway?
Anyway, onto the good stuff. Basically, sometimes your SSVEP signal is dispersed along a time series — maybe it's not always coherent, and it comes and goes and the phase is not directly sequential. When you average your data, you find that a lot of the signal was overlapping, and not in the good way. It averages to zero, and your signal is worse than the noise previously was. 


![Graphs from original PRSA paper]({{ url_for('static', filename = 'prsaoriginal.png')}})

This technique relies on the waveform *usually* lining up within the noisy signal. Which is to say, when the waveform of interest goes up, the noise+signal overall should go up too, at least for a majority of the times you check it. So you average a big window around all "up" or "down" points, and might be able to pull out the original signal. The original paper uses some jank original signal, so it looks atrocious even after averaging. I'm told this was on purpose. Why couldn't they just use a sine wave?

I can't wait to try it. Looks like it won't work, but it seems stupid enough that it just might.

