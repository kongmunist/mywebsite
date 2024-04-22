title: "Immersive Space Workarounds In The Vision Pro"
date: 2024-04-21
label: blog
tags: [avp, ar, vr]
snippet: "Quick Immersion"

Hello!

Apple's VisionOS is the first AR headset I've worn for more than a few hours, and I've been writing VisionOS apps for about a week now.

So far, one thing that bothers me about VisionOS is the inability to use custom gestures in the main "area". The Vision Pro is mostly billed as a productivity tool, and while working in it I wanted to do hand gestures to open specific webpages or send data to some program for processing. Unfortunately, accessing hand tracking requires ARKit, which requires the app to be in an "Full Space", which closes all other apps (e.g. Safari, Macbook screen mirroring). This is intentional on Apple's part, possibly to prevent custom gestures from interfering with the system-level "Tap" and "Drag" motions.<img src="/files/imageKTWUQ.png" style="height:222px; max-height:20em; object-fit:contain; width:100%" />

I'm not sure what privacy would be protected by restricting ARKit usage like this, but I think custom gestures would be really cool to enable spatial computing and I want to do it. What are our alternatives?

# Quick Immersion

I've been experimenting with opening a Full Space and closing it really quickly, essentially using an app's windowed version as a toggle for the app's Full Space. The Full Space and the user's workflow can then complement each other — I do some 3D modelling on my laptop's shared screen, launch my app's Full Space for life-size model viewing and tweaks, then return to my desktop with a quick gesture. Here's some demo photos.

{{ add_pic("quickimmersion/0.png", "") }}

{{ add_pic("quickimmersion/1.jpg", "") }}

{{ add_pic("quickimmersion/2.jpg", "") }}

{{ add_pic("quickimmersion/3.jpg", "") }}

{{ add_pic("quickimmersion/4.jpg", "") }}

In the past I've seen apps with an exit button to get out of the Full Space. by using a custom gesture, exiting out takes only about a second — the approximate delay when switching between desktops on the Macbook. It's been quite comfortable to use, however I haven't found a really useful thing to do with it. Here's some ideas I had though.

## Inventory app

An "inventory" website can have drag-n-drop slots for objects (3D meshes, URLs, text, files) and share those objects with an Immersive app. A user can drag assets from their computer into the inventory site, enter the Full Space to work with the assets as objects, return them to the inventory, and then exit the Full Space and get the finished files off the website.

Since meshes/objects in a Full Space can communicate on-interaction (such as sending a GET request), the website can know what's happened to its own objects and persist those changes outside of the space.

## 3D viewer

A classic AR use case is viewing life-scale 3D models. An engineer in the middle of PCB design can visualize several boards and connectors in the Full Space, ensuring they fit together. A designer can export their couch design halfway through the process to see how their chosen materials look in real environments, or to check if the approximate sizes make sense. 

# Conclusion

Anyway, just wanted to let y'all know that this was possible. The code is in a [Github repo](https://github.com/kongmunist/QuickImmersion) and it does a few other things (spawning cubes that bounce around the room), but the Full Space opening/closing is simple enough that I hope you can find it. Cya! 
