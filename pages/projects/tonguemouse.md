title: Tongue Mouse
date: 2025-02-12
label: project
timespan: March 2021
pic: tm_hero_elio.jpg
description: A mouse for your mouth

Hello! Wouldn't it be cool to be able to control your computer without (visibly) touching it? I thought so too.

{{ add_pic("tm_hero_elio.jpg", "The Tongue Mouse", True) }}

<br><hr><br>
A while back, I wrote up [a blog post](../blog/mpr121passthrough) about the MPR121 capacitive touch sensors and how they perform under different surface coverings. Those experiments were the precursor for the Tongue Mouse. 

## The Idea
One day, my roommates and I were discussing the next generation of computer input devices. What would we use after the mouse and keyboard? How could we communicate more smoothly with our devices? One potential way was to use the mouth. The tongue is an actuator with fine motor control that is only rarely used to communicate with computers (not counting voice control!). 

We thought that by adding a trackpad to the mouth, we could use both the mouse and keyboard simultaneously, thus increasing the speed of computer interactions. From the outside, it would appear as if you "magically" controlled your computer!

While we found papers exploring mouth-computer interaction devices, most groups used a custom-fit touchscreen that sits on the roof of the mouth. We initially tried that location too, but found it to be much more comfortable to keep a trackpad in the side of the cheek. Maybe this is due to our lack of a custom mouthpiece.

{{ add_pic("tm_mouthrooftopmouse.jpg", "The roof of the mouth is a common location for mouth-computer interaction devices, but I didn't find one that used the cheek") }}

{{ add_pic("tm_mouthsidemouse.jpg", "We found the side of the cheek to be more comfortable", True) }}

To make a touchpad, you just need to detect touch location on a surface. The easiest way is to use capacitive touch, which relies on the human body adding capacitance to a pad which is being charged and discharged quickly.

{{ add_pic("tm_capacitivetouch.png", "Capacitive touch works by detecting the change in capacitance on a conductive pad", True) }}

While most microcontrollers can natively do [touch detection on their pins], we needed a bit more resolution and chose to use the MPR121. It comes with 12 inputs, and we arranged 8 of them into a 4x4 grid of overlapping copper strips to get 16 points of contact. Out of the mouth, it worked just like any other capacitive touchscreen; here I am using my finger to control it.

{{ add_vid("tonguemouse_finger.mp4") }}

There were some challenges with moving the touchscreen to the mouth. 

## Water
The mouth is a wet place, and the liquids there are conductive. We pre-emptively waterproofed the whole touchpad because we were worried that the water might bridge between the different copper strips and hamper our ability to distinguish between different touch locations. We used tape with the sticky side facing inwards to waterproof the sensor.

{{ add_pic("tm_waterproofing.jpg", "We waterproofed the sensor by sandwiching it between two layers of tape", True) }}

## Stray capacitance from the mouth
Besides water, there is also the problem of the mouth itself. To the capacitive touchscreen, tucking it in the mouth meant the cheek acts as one huge touch that covers every part of the grid simultaneously. We didn't want to worry about this pre-emptively, so we hoped that the *relative* sensor values would still be able to stand out enough for us to detect them. 

We did consider a strategy where the device's backplane could be covered entirely in copper tape, which could then be grounded. I think this would reduce the cheek's touch interference through the backplane, but probably not completely.


After some rudimentary waterproofing, we were able to use it with our tongues without the taste of copper. Here's a video of my friend Elio using v1, which was waterproof but not enough to enter the mouth.

{{ add_vid("tonguemouse_elio.mp4") }}

When it came time to make the 2nd prototype, we committed a fatal error — the waterproofing method we used relied on two squares of tape sandwiching the sensor, but little did we know that we had left some gaps in the taping. As soon as the sensor entered the mouth, the inputs were all swarmed with maximum capacitance.











Hello! Welcome to my 2nd attempt at giving the Internet a physical form.


{{ add_vid("gridworldherovid.mov", speed=0.5) }}

Grid World is a 64x64 RGB LED matrix which anyone on the internet can modify. You can draw pictures, write messages, or scribble random pixels.

<br>
<video
    src="{{ url_for("static", filename="gridworldherovid.mov") }}"
    style="display: block; margin-left: auto; margin-right: auto;"
    width="75%"
    controls
    muted
    playsinline
    autoplay
    onloadstart="this.playbackRate = 0.5;">
</video>
<br>
<hr>

Reddit's April Fool's event from 2011 ([r/place](https://www.reddit.com/r/place)) partly inspired this project. During the event, every registered user could change a pixel on a huge, shared canvas once every 5-10 minutes. The results were beautiful and chaotic, and the open-ended nature of the interactions left plenty of room for unexpected, emergent behavior.

{{ add_pic("gw_rplace.gif", "Reddit's r/place", True) }}

Around 2021, I bought this RGB LED display on AliExpress, intending to mount it in a picture frame and showcase some cool gen‰erative art, moving or stationary. Mulling it over, I realized I would quickly get bored of seeing it unless I constantly maintained it — changing what program is drawing, randomly switching images, etc.

{{ add_pic("gw_frame_off.JPG", "In frame, canvas off", True) }}

The problem is the adaptability of the human mind. I have the capacity to get used to anything, especially if it's all hand-chosen by me. The only thing I cannot easily get used to is the entropy generated by another human being. If people were drawing instead of programs, then I think I would never get bored of it.

{{ add_pic("gw_planets.JPG", "Test drawings from before the website went live", True) }}

### But how can I make people want to draw on my canvas?

In the same way graffiti artists enjoy spraying simply for the joy of seeing their work in public, I thought people would just draw on my canvas if it were made public. Paint on my canvas and be seen by the world!

{{ add_pic("gw_elio_cleanup.JPG", "Nice, random, coherent drawings", True) }}

And it kinda worked! People were uploading like crazy after I posted it on my Tiktok. Visitors coded bots to draw images into the pixels, and someone even wrote a bot which displayed a live clock.

{{ add_pic("gw_greatart.JPG", "My favorite drawing so far", True) }}

{{ add_pic("gw_andyface.PNG", "My face, drawn by some bot", True) }}


<video
    src="{{ url_for("static", filename="gw_wolfandclock.mp4") }}"
    style="display: block; margin-left: auto; margin-right: auto;"
    width="75%"
    loop
    controls
    playsinline
    autoplay
    onloadstart="this.playbackRate = 2.0;">
</video>



So, here is the website where you, dear reader, can draw on my grid:
<a href="https://aksuper7.pythonanywhere.com/gridworld" target="_blank">bit.ly/andygrid</a>


<br><hr>
# Technical Details

## Hardware
The hardware is only minimally interesting. The matrix is an RGB display panel, typically seen making up large indoor screens in malls or airports. Drawing on the matrix is handled by a Raspberry Pi with a special hat made by Adafruit that makes controlling the screen easy. The Pi is connected to the internet via a USB WiFi dongle, and polls the web canvas's server every few seconds to get the real-time state of Grid World.

{{ add_pic("gw_hardwarebuild.JPG", "The Raspberry Pi + Hat, dongle, power supply, and RGB display", True) }}

## Software
For the website to work properly across multiple users at once, I am calling fetch every few seconds from the client-side since my hosting provider does not allow any real-time messaging like Websockets or Server-Sent Events. To avoid conflicting states, I am using a changes-only [CRDT](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type) model on the server. Users can only push updates to pixels, and cannot overwrite the server's grid with their own. The current Grid World canvas is saved to disk every 5 seconds if any edits were made, and the server's python instance maintains the true grid in memory.

{{ add_pic("gw_website.png", "", True) }}

## Social Considerations
I also had to add some social barriers. In Grid World, drawing is done by clicking, but when debugging I wrote code which allowed drawing via mouse hold-and-drag. When deploying the website, I left this in the code and some people uncommented it for extra privileges. This quickly creates ugly noise marks over everything, so I removed that bit of code. I also had to add a rate limit because within a week the first bots were already being annoying — erasing people's work and filling the whole canvas with a single color.

{{ add_pic("gw_camerafeed.png", "Camera feed of the physical Grid World", True) }}

To make the experience more complete, I also added a camera feed which sends an image of the physical Grid World to the website every 10 seconds. I'm not sure how many other people find this interesting, because I think the physical-ness is the only real novelty of this project, but I think it can't hurt. Some people must be compelled to draw because they know it appears in my room.
Because the camera uses an open endpoint in the server, I added an auth key so only my raspberry pi can upload images. This is also why the code is not available, because I do not want some exploiter uploading inappropriate images.

I do not moderate the grid, and I never plan to. Generally, offensive symbols are quickly erased by Good Samaritans, and I quite like the unmoderated feeling of the Grid on an increasingly moderated Internet.

<hr>

## Interesting Observations

The Grid in my room runs almost real-time — so seeing a pixel change means that somewhere in the world, at that exact moment, someone on their computer had browsed to my site and decided to change a few pixels. I could feel their presence so strongly when I saw changes happening live, and I didn't even know who was doing it. Sublime!

Unlike Reddit, there is no method for communication on Grid World except painstakingly drawing words pixel-by-pixel. However, I hosted Grid World on the same site as my previous project [(the InfoGlobe)](), which featured a text box for uploading messages to my device. I noticed after a few days that Grid World users would talk to each other on the InfoGlobe page using the upload message box, and then go back to Grid World to draw a larger piece together. While not the intended use case, I think it's really cool that the InfoGlobe side gets used that way.

<hr>

## Conclusion & Next Ideas

{{ add_pic("gw_bigbuttons.jpg", "Tactile pixels for two-way communication", True) }}

Grid World is great for me because I don't have to go online to receive messages from people, but other people still have to go online to send messages to me. How cool would it be to have a smaller, tactile Grid World that you share with a more intimate group? Think you and your parents, or you and your partner, or a gaggle of friends who are working in different cities. A shared canvas that everyone can draw on without going on the phone or computer. I think that would be really cool.

If you (yes you, dear reader) have any comments/critiques/suggestions for the current Grid World, I am all ears! Shoot me an email, DM, or write me a message on Grid World.

And if you can think of any other ways you would enjoy sharing presence digitally, please let me know and maybe I can build it for you.



Finally, if you control a source of money and are interested, I would love to make a huge one of these. Think, you could have one in your main office that all your employees can participate in, creating a shared sense of space.










