title: Noisy NeoPixels
date: 2023-05-31
label: blog
tags: [electronics]
snippet: Audible annoyance from WS2812B LEDs

_When I was small, I visited my friend whose dad was an electrical engineer. I got to talking with him, and asked "Hey, what's the point of that thick bit on my cables?"_

{{ add_pic("nn_ferritebead.jpg", "Big chunky cylinder on a charging cable") }}

_He said "that's a ferrite bead, it reduces noise," and I nodded in understanding — that explained why my cables never made noise._

_About a decade later, I learned about electrical noise._

<hr><br>

Hello!

Recently, I've been playing with the Adafruit Circuit Playground Express. This is an incredibly nifty SAMD21 microcontroller board which I have been using exclusively for its built-in ring of NeoPixels.

NeoPixels are like multi-colored RGB LEDs but smarter, and it's easy to control a whole strip of 'em from just a few digital pins. But like all LEDs, the brightness control is implemented via PWM — in this particular case, at a frequency of 400 kHz or so. And while it should be out of the human hearing range, _I can hear it!_

# Electro-audible noise
As it turns out, electrical oscillation often creates audible noise. Most people are probably familiar with electronics or wall warts that start whining or [singing](https://product.tdk.com/system/files/contents/faq/capacitors-0031/singing_capacitors_piezoelectric_effect.pdf) when plugged into the wall. Usually it comes from a high frequency physical oscillation caused by the electrical oscillation. 

I'm quite sensitive to noise, and I noticed a slight buzzing coming from my Neopixels when setting the brightness higher than 5/255. Since I'm making a desktop doohickey, I wanted to learn more about the noise, particularly how it changes with brightness. 

In a stroke of luck, the Circuit Playground board comes with a microphone! I wrote a small script to vary the brightness and recorded sound pressure levels (SPL) for a 0.5 second window at each level. My board has a small cover which probably amplified the measured noise. 


{{ add_pic("nn_dbvslight.png", "Graph of NeoPixel noise in dB as brightness increases") }}

Each line is represented by the LED color that produced it. Since white is produced by keeping all three LEDs on, it makes sense for it to be higher than all the others. 

Now I could target low and high brightness to cause the least amount of noise.


# Future Work
One factor I forgot to test is the pitch of the whining at each brightness. Some brightness levels sound more annoying than other levels, even with a lower SPL. This is probably related to the nonlinearity of human hearing. 

With my NeoPixels on, I recorded the audio spectra to see where the whining lay. It turns out to be much lower than the PWM frequency of the Neopixels, which means I do not understand the root causes of the noise very well. 

{{ add_pic("nn_points.png", "The three noisiest frequencies are all much lower than the PWM frequency of the NeoPixels. Vertical lines are the whining, and horizontal ones are me dropping my phone") }}

# Conclusion
The Circuit Playground mic also has an FFT function, and someday I will get around to recording the spectrum along with the SPL. For now, I have minimized the overall sound, and that is enough. 

Cya later!