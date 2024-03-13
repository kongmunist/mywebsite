title: "Apple Vision Pro Hackathon: A Retrospective"
date: 2024-03-13
label: blog
tags: [avp, ar, vr, mr, hackathon, logistics]
snippet: "Thoughts on the Vision Pro"

If you have a Vision Pro we could borrow and live in/near Pittsburgh and are free before May 2024, I would be interested in hosting this hackathon again. Please email/DM me if you'd like that, and we can make it happen :)

<hr>

Hello! Last weekend I hosted an Apple Vision Pro Hackathon (aka AVP Hackathon), which simply entailed asking everyone I knew if I could borrow a Vision Pro and then asking everyone if they wanted to develop on it for a couple days.

{{ add_pic("avph_reflection/0.png", "") }}

I think hackathons are a good event for colleges since full-time coders are usually too world-weary to also spend their weekends coding. Nonetheless, I picked a bad time to ask, since I mostly knew researchers and we're a month shy of the next big conference deadline. 

Anyway, somehow I got a crew of four people and we spent 48 hours building apps and demos for the AVP. The main goal was to write app that would make you want to wear the AVP (the most useful are screen-mirroring and web browsing). 

We also had a rule that someone had to be wearing the AVP at all times —  in the end, this didn't even need enforcing because we were iterating so fast that someone always needed it. In the end, we made 3.5 working apps, which is a pretty good hitrate. 

{{tableofcontents("avph_reflection.md")}}


# Day 1 

Started at 10am, got to the space around 10:30am. I provided beverages and coffee.

{{ add_pic("avph_reflection/1.jpg", "") }}

We spent most of the day learning Swift. I made and loaded a custom 3D model and then tried to write custom gestures that would spawn/move it around. 

{{ add_pic("avph_reflection/2.jpg", "") }}

I cribbed the head/hand tracking from a [Hand Ruler](https://github.com/FlipByBlink/HandsRuler) app, then kept cutting the code down until I could understand all of it. I think everyone else had a very similar process, since the default examples that Apple provides are too full-featured to just illustrate single concepts at a time. 

{{ add_pic("avph_reflection/3.jpg", "") }}

The AVP is meant to be a single-user device, so it doesn't let you do screen mirroring unless the same user is signed into both the Macbook and the AVP. In order to avoid taking off the headset every time we uploaded code, we spent a lot of time looking through the AVP cameras at our screens trying to make small edits. This is really close to the limit of what the AVP's AR resolution is capable of, and this process would've been much more comfortable if we could just project our displays into AVP space.

When we wrapped up the day, everyone sort-of understood the Swift structure and had run some example code already. The language is pretty straightforward, and the code completions in the Xcode IDE are more full-featured than any IDE I've used before.

# Day 2

Late start, 11:30am. My roommate had some group project to work on in the morning, and everyone else woke up late.

{{ add_pic("avph_reflection/4.jpg", "") }}

Someone else finished their teardown of an example, and made an app where the press of a button opens an immersive video. I finished wrapping up all my code into a simple demo app ([on github here!](https://github.com/kongmunist/Vision-Pro-Head-Hand-Tracking-Demo)) and started working on custom gesture recognition. 

<blockquote class="twitter-tweet tw-align-center"><p lang="tl" dir="ltr">Italian simulator <a href="https://t.co/TqmlcglZLM">pic.twitter.com/TqmlcglZLM</a></p>&mdash; Andy (@oldestasian) <a href="https://twitter.com/oldestasian/status/1767012032132616565?ref_src=twsrc%5Etfw">March 11, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Gestures have no helper functions. Even in the [Happy Beam demo] provided by Apple, to check that the user has formed a heart-shaped hand gesture they just calculate the distance between specific hand joints and use some smoothing to make it a bit nicer looking. I wrote some functions like `closeTo(jointnames, threshold)` to make simple gestures easy to implement, then used them to detect this Italian pinched fingers gesture. 

By ~3am, everyone had finished their app to a point where we could film it. Due to daylight savings, we thought it was an hour later.

# Demos

In the end, we had written the following apps: 

- Gaussian splatting model viewer running on Metal, with hand gesture control

- Collaborative video upload gallery for AVP/iPhone 15 spatial videos

- AR interface to control the color and brightness of real-life smart bulbs

- Lighter demo like the early iPod apps

<blockquote class="twitter-tweet tw-align-center" data-media-max-width="560"><p lang="en" dir="ltr">Throwback lighter app, made on the <a href="https://twitter.com/hashtag/AppleVisionPro?src=hash&amp;ref_src=twsrc%5Etfw">#AppleVisionPro</a> <a href="https://t.co/y3sJr8NvB9">pic.twitter.com/y3sJr8NvB9</a></p>&mdash; Andy (@oldestasian) <a href="https://twitter.com/oldestasian/status/1767978456908968044?ref_src=twsrc%5Etfw">March 13, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

(I don't have all the videos yet so this list will be updated with the missing ones later)

# Takeaways

## Real device stuff

- At first when I looked through the AVP, I compared the passthrough-AR with other AR headsets I've tried — the AVP is the best I've tried, so I enjoyed it. After a few hours of wearing/developing on the AVP, I began to compare it to no-headset and it loses on every metric. Some LED lights are flickery through the AVP camera, and reflective stuff (screens, windows) looks warped and not flat.

- The IPD calibration (motor moving lenses closer/further) is required everytime we switched headsets, but that takes only ~10 seconds. I find it weird that I had to hit the Digital Crown button to start the IPD, but maybe this is an Apple-y design principle that nothing physical moves unless the user moves something physically. - Since we couldn't get screen mirroring working, we had to look through the AVP to see my computer screen to edit code and upload stuff. The text is surprisingly legible, but no amount of surprise overcomes the fact that it's not good enough to be comfortable. Two of the hackers couldn't read off their screen through the headset at all, and they don't even wear glasses normally. - AVP is clearly meant for a single owner — I think only 2 user profiles can be added at once. This made the hackathon a bit harder, but not impossible — for instance the eye tracking is only calibrated to one person at a time, but it's good enough that other people could use it without needing to redo the calibration.

- The device is not socially accessible. All the experiences are kinda "in your head", requiring screen mirroring or recording to get someone else to see it. All the videos I show are shot on-device using Developer Capture in Reality Composer Pro, and a minute-long video takes ~1-2 minutes to transmit to your laptop. 

## Coding in Swift

- Dev time is quick for small apps. A fresh upload required a bit more time, but each iteration of the code only took ~30 seconds from pressing the Xcode Run button to seeing the app in the headset. On my Macbook Pro with an M1 Max, build times were only ~5-10 seconds and barely noticeable.

- It's possible to upload code through Unity and Swift, and it may be easier for you to get started if you have Unity experience. However, I did hear that there were some features which didn't exist in Unity but did in Swift, so for full features you may want to just bite the bullet and learn Swift. Swift is a great to program in once you get it. Two days after the hackathon, I actually felt an itch to write a Mac app so I could continue using the Xcode IDE. 

- Swift examples provided by Apple are incredibly full-featured, meaning they can put out [four example demos](https://developer.apple.com/documentation/visionos/world) and show most features in use in the code. However, this is not super beginner friendly — I'd much rather have single-use example demos. 

- Examples are great for illustrating what is possible. If you see a transparent window with a floating button in the Hello World demo, you know that somewhere in the example project is the code that makes that happen.

- Xcode is a great IDE, it has both an AVP simulator which launches separately and a containerized one that runs inside the editor. The containerized one does not show windows faithfully, meaning you should always check what they look like in the real simulator

- The AVP simulator can pretty accurately do windows, buttons, and other functionality, so you don't even need to cough up the cash for a device if you're interested in developing more straightforward apps. The only thing it doesn't have is hands — gestures can only be developed using a real device. I remember seeing a [blog post about faking hands](https://varrall.substack.com/p/hand-tracking-in-vision-pro-simulator) in the AVP simulator, but did not try it myself yet. 

{{ add_pic("avph_reflection/ide.png", "") }}

## Dev community

- Forum posts are lacking, and very few people have posted Vision Pro development questions. If we assume 100k units have been sold, and only 10k to developers, then we can only expect ~100-1000 people active on the developer forums. Consequently, there are very few tutorials — large alpha in this space! Within a few months, you could easily become the foremost authority on VisionOS development. 

## Idealogical feedback

- I think if the AVP is meant to be a work device, then it's going to need something equivalent to hotkeys but for 3D space. Custom gestures are really cool, and they offer a lot of possibilities for new interactions (i.e. subtle hand gestures can trigger web apps or specific programs), but they can only be accessed in an Immersive App meaning no other apps can be open simultaneously, preventing window management or any fun systems-level control using custom gestures. You could make the comparison that iPhone apps are only allowed to recognize custom swipe/tap gestures when their app is open, but I think this limits the AVP much more when the available space of interactions comes from fine-grained continuous hand tracking.

<hr>
# Conclusion

Anyway, super fun weekend, and I'm incredibly happy that everyone got to a working demo despite starting from zero re:Swift. I'll reiterate that I'd love to do this again in April 2024, so if you have a headset or want to join next time, just reach out! Out-of-towners are welcome to stay on my couch.