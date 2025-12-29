title: Amp Box
date: 2019-10-22
label: project
timespan: October 2019
pic: ampbox.png
description: A box optimized for ease-of-use in amplifying tiny electrical signals (<10 mv)

A friend recently complained that there was no product that could take in an electrical signal, feed it through an amplifier, and output the result. So I made one for him. Let me show you its features:
<ul>
	<li>Adjustable gain</li>
	<li>Battery powered</li>
	<li>Easily wire-able inputs</li>
</ul>

<img class="d-block mx-auto" src="{{ url_for("static",filename="ampbox.png") }}"/>

### Rundown

It's a simple little device, but very useful. Let's take a closer look

To turn it on, simply flick the power button on the left to the on position. This eliminates the three power supply wires you'd ordinarily need to power an amplifier circuit (positive, negative, and ground). Since it's battery powered, there's no power source jitter to add noise to your circuit, and there are hidden decoupling capacitors on the underside for even higher supply stability. A voltage divider made of 5k resistors creates an artificial positive and negative voltage to operate on signals positive and negative. 

The red and black inputs and solid wires allow you to plug in components or alligator clip them to the input solid cores. To see the amplified signal, simply clip onto the left half of the feedback resistor. 

<img class="d-block mx-auto" src="{{ url_for("static",filename="ampboxcircuit.png") }}"/>

The potentiometer leads to ground, meaning the gain can be dialed as high as you want it (or at least until your signal hits the supply rails, around 2V for this battery). The low power op amp will last a while, at which point you just need to replace it with another 18650 which isn't too hard to find. 

### Testing
Since the amplifier's gain equation puts the potentiometer on the bottom (100k/potentiometer), any signal can be amplified until you can see it. I fed in a 10 mV sine wave, and was still able to boost it to the rails at 2V. The noise spec is not the best, but this box is really just for seeing if a tiny signal exists before you begin building a circuit specifically for measuring the tiny signal. 

As the final test, we hooked up electrodes across my arms to see if the heartbeat (EKG) was detectable. The wires leading to the electrode was unshielded, and you could really tell from the 60Hz noise. Regardless, with the gain turned up you could see a periodic flutter in the 60Hz wave of around 1 Hz. I'm not going to conclude that the heartbeat was visible, but if you looked closely enough this box would work as a general purpose heartrate detector. 

Let me know what you think, or what features could be added or improved on at andykongresearch@gmail.com





