title: Recreating the Traxion psychophysics effect
date: 2021-06-02
label: log
tags: [electronics, haptics]
snippet: Only 8 years late!

Hello! I recently learned of this paper called [Traxion](https://lab.rekimoto.org/projects/traxion/), wherein a genius visionary named Rekimoto discovered that asymmetrical vibration with a linear vibration motor caused a "pulling sensation" on a user's finger. A fake force that feels 32 grams of real force! Amazing!

To tell the truth, I straight-up couldn't believe it until I tried it. With my limited setup, I produced 3V using an LM317 (powered by a 9V I acquired), then drove a transistor with an Arduino to generate the ramp/square wave I needed. 

<p class="caption">Traxion setup</p>
![Traxion setup]({{ url_for('static', filename = 'traxion_setup.jpg')}})

Inside the linear actuator, there's a little weight anchored by spring to the center position of the body. This weight is what moves forward when we give the device a HIGH voltage, and it jerks back when we leave it unpowered. This "asymmetry" is what creates the sensation of a force. 

According to this more recent [paper](https://sci-hub.st/10.1109/HAPTICS.2016.7463151), the effect is caused by the skin dragging more in ON direction than when it turns OFF. This is due to the forward ON happening faster than the spring can pull it OFF. Something about detectable vs. unnoticeable acceleration. 

The authors drive their device with a high plateau, followed by a slow ramp down. This eases the spring-back while keeping the ON switch waaay fast. They claim the effect is strongest at 40Hz, but I found that just a simple duty cycled square wave (100Hz, 20% duty cycle) does the effect too, just less. 

<p class="caption">Linear actuator I used. The little white pin is the weight, and it creates the force sensation in the length-wise axis</p>
![Linear actuator I used. The little white pin is the weight, and it creates the force sensation in the length-wise axis]({{ url_for('static', filename = 'traxion_linearact.jpg')}})

## Note
This may sound silly, but I was surprised to feel vibration. Yea, yea, the thing is turning on and off really fast, but the paper only ever mentioned the force that it produced! I can't be blamed for wanting the vibration to go away to leave us with a free, fake force produced by a tiny vibrating motor. Maybe that's too easy though.

I want to see if this can be done on a larger scale, maybe from a handheld object? (VR controller would be cool). Though vibrating things are hard to hold onto. 

That's all for now, cya later!