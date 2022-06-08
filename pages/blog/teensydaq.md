title: "Teensy DAQ: ADC Oversampling on the Teensy 4.0 microcontroller"
date: 2020-11-27
label: blog
tags: [hardware, microcontrollers, Teensy, ADC]
snippet: "300 kSPS to 1 kSPS faster than you can say \"free bits\""

I recently wrote a [Teensy Data Acquisition GUI](https://github.com/kongmunist/TeensyDAQ-Fast) for recording data from a microcontroller/sensor onto the computer. It's pretty simple, just a Python QT5 GUI that has a plot of the data as it comes in over the serial and writes it into a list as fast as it can. After you hit 'stop recording', it writes it into a text file. And yes, this order was the fastest. I checked.

I felt wasteful when first using it because I only wanted to get signals at around 1kHz at most, while the Teensy analog-digital converter running at full-tilt with some averaging (noise reduction) still sampled at well over 200 kHz. What to do with these extra samples? Get extra bits, of course!

![Free-running ADC goes at 362kHz]({{ url_for('static', filename = 'teensydaq_ADCoutput.jpeg')}})
<p class="caption">Free-running Teensy ADC goes at 362kHz — and it's got two of 'em!</p>


So while you can average 2<sup>n</sup> samples to reduce the Noise Power by a factor of n, you can't quite do the same with bits of resolution from your ADC. Turns out when you sum two measurements, their noise magnitude grows by a factor of sqrt(n), while your signal magnitude only grows by a factor of n. The SNR only improves by sqrt(n), since n/sqrt(n)... well, you understand. More on that [here](https://en.wikipedia.org/wiki/Oversampling#Resolution). Basically, you need to sample 4 times per bit of extra resolution you want to get. So if you wanted one more bit, you'd oversample at 4x the Nyquist frequency, if you wanted two you'd have to sample at 4<sup>2</sup>, etc.

However, I'm still not sure exactly how SNR relates to bits of resolution. I understand the math, but not intuitively. It still feels like you could average two binary numbers to get one that has one more bit of info. Maybe it only has 0.5 more bits of extra information? That would definitely correspond to it having "less noise," which it does after averaging... I definitely don't understand completely. 

<br>

### Noise is necessary

Also, I learned that you NEED noise on your ADC input. Luckily microcontroller voltage references are not the most stable thing in the world, so you usually have enough noise on the pin to wiggle the signal up and down already. I read on some Stackoverflow post that if God made you a 10-bit ADC that was perfectly stable, it could not be directly oversampled to get extra bits of resolution. It'd always give the same answer. Some systems couple a sawtooth wave through a capacitor onto the sampling pin as a form of dithering noise, but I think I don't need to do that. 

### So how many bits can we really get?
So the Teensy ADC goes at 362 kHz, and gives 12 bits natively. We can get 16 bits at 362000/256 = 1414 Hz, and maybe one more bit for a 350 Hz sampling freq. Not bad! We've upgraded our ADC for no noticeable loss, besides maybe some noise loss we could've used the averaging for. I think if we use both ADCs to sample, we'd reduce the noise and perhaps even get 17 bits at 700 Hz, but that's a really minor improvement. 

Anyway. I'll try it later, but this is what I've been exploring for now. 

