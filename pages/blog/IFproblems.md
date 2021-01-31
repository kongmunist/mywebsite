title: Detecting instantaneous frequency is hard
date: 2021-01-31
label: blog
tags: [thoughts, bci, dsp, fft]
snippet: Major blockades to fast, effective BCI

Hi! Today we're going to be talking about FFT bins and time. 

When you first take an FFT, whether it be `scipy.fft.rfft` or MATLAB's built-in, you may have had to convert from a "bin number" to the frequency range that bin represented. This formula is pretty simple, but might've been tricky to google initially; the Nth bin contains frequencies from N x (sample rate/sample length) to (N+1) x (sample rate/sample length). 

If you were like me, you spent some time staring at the constant (sample rate/sample length) term that each bin was getting multiplied by. The surprising part was that this ratio was independent of sample rate, meaning that the frequency resolution you got from the FFT is entirely dependent on how long the signal is sampled and nothing else. Of course, the total NUMBER of bins you can get is increased if the sample rate goes up (up to the Nyquist frequency of sample rate/2), but that doesn't help you if your signal is in the low Hz. 

Now, if you do RF stuff, this hardly matters. FM radio operates on increments of 0.1Mhz, so a 10 µs sample length is sufficient to get the bin resolution you need. This is basically finding the instantaneously frequency of a signal — we don't notice 10 µs at all. 

The problem arises when you start analyzing the frequency content of EEG, which operates strictly under 100Hz, and usually under 20Hz. Now to get 1Hz bin resolution in your peak detection, you need at least 1 second of data. This is fine for research-grade BCI, but ruins usability when BCI takes 4x the time to press a button and is only 80% reliable. 

Besides that, the number of inputs is reduced, since only 1 Hz differences can be detected. This leaves us with the whole Hz increments from 10-20Hz, which is only about 10 options. If the possible frequency bins were doubled, then there would be twice inputs; however, to get 0.5Hz bins you'd need 2 seconds of data. These are hardly instantaneous methods now, and EEG doesn't become any more reliable with tighter frequency bins.

And don't even get me started on the time-frequency resolution tradeoff. EEG signals are incredibly temporal, meaning a 10Hz signal may only exist for a second within a longer period of recorded data. This is why techniques like phase-rectified signal averaging work so well for it. But that's another post.

Bye!