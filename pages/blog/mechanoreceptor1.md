title: "Stimulating the Merkel Discs: Nerve stimulation using TENS"
date: 2021-05-23
label: blog
tags: [EMS, TENS]
snippet: The Firm Handshake-inator 3000

Hello! As you may know, there are 4 mechanoreceptors in the skin.

I wanted to create a specific sort of sensation on my skin, and I thought the best way would be to **target one of these specific mechanoreceptors**. 

## Background

These mechanoreceptors are like a biological equivalent of electronic sensors; cleverly shaped bits of nerve tissue that are sensitive to specific vibrations, sustained or brief pressure, etc, and report back to the brain what they feel. Through these sensors, you learn what textures feel like, what shapes you're touching, and all that cool tactile stuff we rely on every day. You can read more about them on [Wikipedia](https://en.wikipedia.org/wiki/Mechanoreceptor#Types). 

While each receptor is most sensitive to a range of frequencies as stimulation (running your hand over a cloth for example), this tells me nothing about the way the receptors send this message back to the brain. 

<p class="caption">Pacinian corpuscle image I got from <a href="https://en.wikipedia.org/wiki/Pacinian_corpuscle">Wikipedia</a></p>
![Pacinian corpuscle image I got from <a href="https://en.wikipedia.org/wiki/Pacinian_corpuscle">Wikipedia</a>]({{ url_for('static', filename = 'mr1_pacinian.png')}})

For example, the Pacinian corpuscles are these bulb-like things which leak calcium ions when they are deformed. This leaked Ca causes nerves to fire at the base of the bulb, and the more deformation, the more Ca, and the faster the nerves can fire. Therefore this receptor bulb sends its info in a frequency-encoded fashion. But how fast? What electrical stimulation speed would I need to "pretend" to be a Pacinian corpuscle that's feeling a vibration?

<p class="caption">Off-the-shelf TENS unit I used for this testing</p>
![Off-the-shelf TENS unit I used]({{ url_for('static', filename = 'mr1_tens.jpg')}})

Despite this limitation, I still found something cool. By placing a set of pads on the front of the bottom segment of my fingers, I was able to simulate a tight squeezing sensation on my finger. It felt as if my finger were being pressed on all sides by a vise.

<p class="caption">One electrode on the back of my hand, one on the front bottom pad of a finger</p>
![One electrode on the back of my hand, one on the front bottom pad of a finger]({{ url_for('static', filename = 'mr1_elecplacement.png')}})

I'm using pulses of a few hundred microseconds, at a frequency of 70+ Hz. Lower than that, and the sensation no longer felt like squeezing. There's also a persistent buzzing feeling from the TENS, and it is on-par with the strength of the squeezing. A bit distracting, but the squeeze is cool. 

I'm assuming the mechanoreceptors I'm stimulating are the Merkel discs, since squeezing is really a sustained pressure. You could argue I'm feeling a momentary pressure multiple times per second, but I think that's just the same thing as a sustained pressure. 

## Applications
Ideally we get all the mechanoreceptors stimulating separately, since this would let us produce a whole world of different textures when we touch objects in VR. Side note, does anyone want to make a VR game together? We can call it Firm Handshake Simulator 2022.

We could also use it for finger-specific tasks like learning piano and guitar, or sign language. This could be used as a finger indicator. Besides that, I dunno.

Cya next time!
