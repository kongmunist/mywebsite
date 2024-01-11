title: Fast-charging capacitors
date: 2021-08-09
label: blog
tags: [electronics]
snippet: Who has time for 5RC?

I recently thought about a way to charge capacitors really quickly. 

If you think about it, capacitors are sort of like buckets that you can fill with electrons. Their peak level is their voltage rating, and if you keep filling them they explode. Usually this means you only charge capacitors using a voltage less than or equal to their max voltage, to avoid the explosion.

But! This method sucks, and it's slow. As your cap fills up, the voltage difference between your source and the capacitor goes down, which makes your charging current go down too. Diminishing returns means that really big capacitors can take several seconds to charge up to a desired voltage. 

# Better method
Ideally, we'd use some massive voltage source for charging, and then turn it off immediately when our capacitor hits the final voltage. We only use the previous method because we humans have slow reaction times, and can't turn off the voltage source quickly enough to avoid a potential capacitor explosion.

But I'm *pretty sure* we've invented faster voltage switches than the human hand.

# Enter, the humble microcontroller
![Arduino-enabled fast off switch]({{ url_for('static', filename = 'sc1_setup.jpg')}})


All I did was connect an Arduino-controlled MOSFET to a 2200µF capacitor. The Arduino reads the voltage of the capacitor, and shuts off the MOSFET when the voltage gets past our set point (4V). I used 5V, 10V, 20V, and 30V for charging. Here's how long each one took:

<p class="caption">Charging with 5V</p>
![Charging with 5V]({{ url_for('static', filename = 'sc1_chargeto4with5.jpg')}})

<p class="caption">Charging with 10V</p>
![Charging with 10V]({{ url_for('static', filename = 'sc1_chargeto4with10.jpg')}})

<p class="caption">Charging with 20V</p>
![Charging with 20V]({{ url_for('static', filename = 'sc1_chargeto4with20.jpg')}})

<p class="caption">Charging with 30V</p>
![Charging with 30V]({{ url_for('static', filename = 'sc1_chargeto4with30.jpg')}})

In text form, charging a 2200µF capacitor to 4V took:

- 5V -> 5.6ms

- 10V -> 1.7ms

- 20V -> 0.76ms

- **30V -> 0.43ms**

My power supply caps out at 30V, and that gives you a **13x speedup** in capacitor charging time!

# Theoretical speedup
We've seen how the real world does it; how about comparing it to theory?

Here's the equation that governs how fast a capacitor charges. It calculates the cap's voltage given some time *t* connected to a voltage source Vs.

<p class="caption">Capacitor voltage after some time t, charging with a voltage Vsource</p>
![Capacitor voltage after some time t, charging with a voltage Vsource]({{ url_for('static', filename = 'sc1_chargeVeq.png')}})

Solving this backwards for *t*, we have some terrible looking equation for how long it would take to charge a capacitor given a source voltage.

![Above equation solved for time t]({{ url_for('static', filename = 'sc1_chargeTeq.png')}})

Plugging in our previous charging voltages and magically using R=1.5Ω, we get the following charge times:

- 5V -> 5.3ms

- 10V -> 1.7ms

- 20V -> 0.73ms

- **30V -> 0.47ms**


Greater than 10x theoretical speedup at 30V! And pretty good agreement with the numbers I measured. 

# Theoretical mismatch

Some of my times were faster than the theoretical times. What could cause these faster-than-theoretical real world charging times? 

- Volt drop across the MOSFET? The MOSFET is fairly low resistance (IRFZ44NPbF claims 0.0175Ω at max), so that can't be it. 

- Lower R_cap than 1.5Ω? Possibly, but I'd just be guessing.

- Perhaps the Arduino got a bit overzealous and cut off the capacitor before it truly charged to 4V? This seems like the case from some of the charging graphs > 10V. For some reason, the reached voltage hit 4V, the Arduino shut off the MOSFET, and then the capacitor voltage dropped a bit. I'm not quite sure why this happened.

# Conclusions
I used an Arduino for reading voltage, meaning that I only have an effective range of 0-5V. I can get a higher effective voltage range if I buffer and divide the capacitor voltage down before `analogRead`ing it. Maybe even a resistor divider would work.

The only way my program was able to run fast enough on the Arduino is because there was nothing in the loop except the voltage checking. With that, it was able to stop the capacitor under a few hundred us. With a faster µC, we could use even higher charge voltages and still be sure we'd turn it off in time.

A friend suggested I use voltage prediction to get a more precise turn-off time for the capacitor, sorta like an instant-read thermometer. I forgot about that until after I finished, but it's probably a good idea.

# Head Fake

This post is actually about supercapacitors. Why go through the trouble to find a high current 3V source when you could just use any old voltage source and turn it off in time? 

Hell, for a large supercap, it'd charge slowly enough that you could probably disconnect it yourself. Just make sure you don't exceed your source or capacitor's current limit. I AM NOT RESPONSIBLE FOR BURNT CAPACITORS / FINGERS / HOUSES. 

Be safe. Cya around!
