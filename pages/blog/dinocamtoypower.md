title: "Power profiling a thermal printer camera"
date: 2024-04-07
label: log
tags: [electronics, powerprofile]
snippet: "Exposing the internals of a dinosaur-shaped children's camera I got in Shenzhen"

Hello! I've recently finished a paper, so it's time to work on sillier stuff. 

On a recent trip to China, I purchased this children's toy camera consisting of a front/back-facing camera and thermal printer which can print the captured photos on the spot. It's adorable, and I use it to take shitty analog-looking photos of my friends. 

{{ add_pic("dinocamtoypower/0.jpeg", "", alt="Teal dinosaur toy camera opened up, showing thermal printer, camera lens, and blue battery pack inside") }}

As someone whose only used phone cameras, having one as a monotool is pretty convenient. And the terrible picture quality is quite freeing, since no matter what you do or how you look, the picture will be pretty shite.

My only gripe is the speed. Most real cameras have a sleep mode where they're on, ready to shoot, but not really burning much power. I'd like to keep this camera in sleep mode too, cause it takes 5-10 seconds to turn on and another few seconds to flip around the camera. But as far as I can tell, there is no sleep mode, just a screen-off mode. You can also configure an auto-off timer in the settings, but then you have to wait for it to turn back on again.

If "display off" mode uses almost no power, then I can make the auto-off timer absurdly long and just turn off the display when it's in my pocket. However, if power consumption stays high, I'll just leave it off and deal with the startup time. It's time to check!

# Power metering

I've already taken this camera apart several times to re-plug in the battery, so it was easy enough to do it again to measure current consumption. I do this by attaching my oscilloscope probes across a 1Ω resistor in-line with the battery. The millivolts measured will be the milliamps consumed. 

Side note, it's sad to me that some versions of this toy will be thrown away despite being fully functional just because the parents/kid didn't know to open it and push back the battery plug back in. It should be glued on to prevent this, but I digress. 

# Screen on

After the device turns on, power consumption is a steady ~85mA on the start screen

{{ add_pic("dinocamtoypower/1.jpeg", "", alt="Oscilloscope current trace holding steady around 85mA with the toy camera on its start menu screen") }}

# Camera on

With the camera on, current consumption increases to ~95mA. It does not seem to matter which camera. 

{{ add_pic("dinocamtoypower/2.jpeg", "", alt="Oscilloscope trace stepping up to roughly 95mA as the toy camera shows a live viewfinder image") }}

{{ add_pic("dinocamtoypower/3.jpeg", "", alt="Similar oscilloscope current trace with the other camera active, again around 95mA") }}

# Display off

When the display is off but the device is on, power consumption is still quite high. The camera seems to turn off but we are still at a steady ~80mA, nearly the same as when we're on the intro menu.

{{ add_pic("dinocamtoypower/4.jpeg", "", alt="Oscilloscope trace near 80mA with the toy camera display turned off but the device still running") }}

# On shutdown

Display off on the menu screen has a current consumption of ~62 mA. This increases as the turn-off jingle plays and the screen turns back on, but then drops to zero when the device is off (as expected) 

{{ add_pic("dinocamtoypower/5.jpeg", "", alt="Oscilloscope trace during shutdown: current rises for the off jingle then drops to zero once the camera powers down") }}

Keeping the camera on the menu screen with display off uses the least power, but it's still a far cry from zero. It's a shame because I think the startup time need not be so long, and shortening it would make the camera more useful to me. I will continue to use the camera, but probably not the display-off mode. 

{{ add_pic("dinocamtoypower/6.jpg", "", alt="Grainy timestamped toy camera photo of two friends, one wearing a VR headset and the other grinning") }}

Cya next time!
