title: "iPhone camera vs. real camera"
date: 2023-12-23
label: blog
tags: [photography, optics]
snippet: "Learning about sensor size"

Recently Frido got a nice camera and took some photos of me. They looked great, with nice color and incredible close-up detail. However, when I imported them into my photos library, I saw that the shots were only in 2K (1920x1080). My phone camera consistently shoots photos in 4K, but doesn't look nearly as good. What gives?

We talked about it on a tram and took some side-by-side shots, him with his camera and me with my phone. Even from his camera's tiny LCD screen, the closeup detail in the camera shot was incredibly clear compared to mine, which looked dusty and blurry. Unfortunately we have lost those test photos, but luckily I borrowed a similar camera to take comparison shots with.

Here are two photographs of the same scene. The first photo is taken with the Canon EOS 3 (APS-C sensor), while the horizontal one is taken with an iPhone 13.

{{ add_pic("phonecamvsrealcam/0.jpg", "") }}

I have some closeup shots, but the comparison is kinda impaired by the lower resolution of the Canon. Again, the Canon is the first shot. 

{{ add_pic("phonecamvsrealcam/1.jpg", "") }}

The Canon's details on the right side of the curtain come out better, but the iPhone does a bit better on the left side (less lighting). Even though more detail is resolvable in the iPhone photo, the whole shot looks a bit washed out - the colors are much crisper with the Canon.

On the left wall, the iPhone image is much grainier, and I think the weird coloration on the Canon shot is from the JPG encoding and not the camera itself. 

# Does it come from sensor size? 

The Canon APS-C sensor size is 25.1×16.7 mm (or 419.17 $mm^2$) while the iPhone 13's is 44 $mm^2$ total, almost a 10x increase. This larger sensor should let the camera capture more light for each "photographable region", reducing any graininess in flat areas and offering better capture for lower-light regions. This is how Frido explained the difference in the two cameras to me. 

But I'm not sure. The iPhone benefits from the many millions Apple poured into computer vision research for ML image enhancements, and doesn't do too badly against the Canon. Take a few pics and average them out, maybe the grain will go away and the resolution is still ~2x higher than the Canon camera? 

# What about video?

I'm interested in shooting video with a slightly nicer camera than my iPhone, so this is the primary focus of my curiosity. I tried to take a comparison video on the camera as well, but it shoots video in a lower resolution than it takes photos.

So the camera is not ideal for taking photos with, but then how much does sensor size matter for video cameras? I could believe that the optimizations are way different if we're encoding using H.264 instead of just capturing photographs every once in a while.

# Conclusion

Anyway, I'm sure this is one of those naive blog posts I write and then regret once I learn a bit more about cameras, but currently it's still news to me.
