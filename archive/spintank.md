title: Spin Tank
date: 2019-08-20
label: project
timespan: August 2019
pic: spintank.png
description: Proof-of-concept prototype for a new kind of armored tank.

I propose a lightly-armored battle tank that is as defensively and offensively capable as its much heavier counterparts. 

### Modern tanks suck

Here is an image of a modern tank, the M1 Abrams, for reference. 

M1 ABRAMS TANK

Weighing in at 62 tons, this beast is heavily armored against all kinds of missiles with depleted uranium armor (1.7x the density of lead), ceramic plates, and strategic empty space for redirection of explosive forces. However, all this armor makes it harder to manouvre around in the oil-rich fields that the US government is trying to liberate. Not to mention, you'd need an entire army to switch out the plates when they get damaged, and the entire point of the plates is to get damaged! Besides, it's not very smart to just sit there and take every shot thrown at you. Enter the spin tank.

SKETCH OF SPIN TANK

### What is a spin tank?

While a normal tank has to heavily armor its front, sides, back, top, and bottom to absorb explosions without damage to its crew, imagine a formidible, light dome of armor viciously spinning at high speeds that just deflects every projectile shot at it. Slow-moving (relatively) projectiles like missiles and bullets will contact the hull briefly before being turned around by the contact point and going off harmlessly in another direction. Even fast-moving, deeply-penetrating projectiles will be affected, since every moment the target changes and the missile will now be pointing at a less critical portion of the interior. I haven't even mentioned the centripetal force pushing out foreign weapons the instant they strike a spin tank, severely affecting their penetration abilities.

### How well does it work?

The effectiveness of the spin tank's hull relies on a few factors: length of the projectile, velocity of the projectile, rotational speed of the dome, and penetrability of the dome compared to the projectile. Because of all these variables, it's hard to determine with certainty how deeply the projectile penetrates the spin tank's armor. However, we can just run experiments and come up with an empirical law.

### Testing

I tested the rotational deflection mechanism of the spin tank by 3D printing a dome and mounting it on a food processor spinning extremely fast. This dome represents the armored hull of a spin tank. It is mostly hollow with a very thin exterior wall, both to properly represent the inner compartment and because I wanted to be able to easily, visually damage the hull. By shooting projectiles at it when it's spinning and when it's still, we can determine whether the spinning hull works to the advantage of the spin tank. 

PIC OF THE DOME and THE DOME SITTING ON THE SPINNING

There are two major classes of projectile: bullets and missiles. One is generally circular, the other is pointy. To simulate bullets, I will use lead pellets shot from a compressed air pellet gun, and for missiles, crossbow bolts shot from "toy" crossbow. This is a shrunk-down demo, but I have used both the pellet gun and crossbow and know that they can do some serious damage. 

PICTURE OF THE PELLET GUN AND AMMO AND CROSSBOW AND AMMO

I ended up using a rubber band-propelled chopstick as the missile. Using the width of my hand as the barrel worked well enough at the near point-blank distances I was shooting at. Fired at the unmoving projectiles, 

### Demo 










### Side notes

I wanted to measure the rotational frequency of the dome mounted on the food processor, but it was going so fast that my phone's built-in, 240 FPS slo-mo wasn't fast enough. I counted 24 rotations in a second from a phone video, but wanted a more rigorous method to confirm. My friend [Sam](http://sam.zeloof.xyz) suggested using an oscilloscope, but I didn't have access to one of those. He also suggested shining a strobe light on foil taped to the dome, since at the proper frequency the foil would appear to be stationary. Using an Arduino Mega, I set up a pulsing LED that wasn't very bright. I could only light up one small patch of the dome. 

ARDUIO SETUP

By fiddling with the pulse length, I got the flash of the spinning foil to stand nearly in place around an 11.2 ms pulse time. Doing the math, you get over 90 Hz! That seemed excessive to me, but then I realized I was probably just strobing at a higher multiple of the actual rotational frequency. I counted how many foil images there were, and got 7 in a full circle, leaving us with an actual rotational frequency of around 12.7 Hz. Pretty damn fast for a consumer appliance! This means that a point on the rim of the sphere goes around 0.6 meters per second! 






<img class="d-block mx-auto" src="{{ url_for("static",filename="fqspotipy.png") }}"/>
<p class="caption">Something made by someone smarter than I am</p>
