title: Remote Photoplethysmography (PPG) Tutorial
date: 2020-12-07
label: blog
tags: [tutorial, CV, heartrate]
snippet: A guide on how to pronounce the word, and how to implement it in Python

Here's the code if you want to give it a shot yourself: [gist](https://gist.github.com/kongmunist/ba659019a483117a846dc2101e27f13d). You will need to download the Haar cascades yourself though.

<hr>

Today I'm going to be telling you about this sick computer vision technique that requires only your webcam feed to get your heartrate. And no, I'm not talking about the phone flashlight trick. I'm talking photoplethysmography (PPG)!

Existing cameras on phones and laptops are amazing, their resolution has allowed some really cool sensing techniques besides taking great photos of your Chipotle burrito. Even knowing this, I found this technique hard to believe. 

I was reading about a project from Microsoft Research called [CardioLens](https://www.microsoft.com/en-us/research/project/cardiolens/), which projected people's heartrates onto their faces using just the camera in a Hololens headset. When your heart beats, your blood vessels swell out a little from the sudden pump motion of the heart. According to this paper, we can see this cyclical pumping as the blood vessels swell and shrink just by averaging the intensity of the colors on someone's face. With a normal camera!

![Cardiolens pulse signal](http://alumni.media.mit.edu/~djmcduff/assets/cardiolens/cardiolens_image_2.png)

Nuts, right? I procrastinated trying this project despite how simple it was reported to be, but after reading about it on [Jimmy Newland's website](https://www.jimmynewland.com/wp/about-jimmy/presentations/remote-ppg-gui/), I felt I could give a decent crack at it. 

![Face and eye detection using Haar Cascades]({{ url_for('static', filename = 'ppg.gif')}})
<p class="caption">Face and eye detection using Haar Cascades</p>

Setting up a webcam feed from OpenCV is pretty easy, as is using Haar Cascades for face detection. I downsampled the webcam to a 1/16 of the original size to run face detection at 20 FPS, then ran it through SciPy's FFT (technically the power spectral density). Voila! 

![PPG from a crop on my forehead]({{ url_for('static', filename = 'PPG_forehead.png')}})
<p class="caption">PPG from a crop on my forehead</p>

Jimmy recommended using the forehead patch, but I got much better signal from a crop of my webcam under my eyes (cheeks are known for their blush). Interestingly enough, I was reading [one of the earlier papers](https://www.osapublishing.org/oe/viewmedia.cfm?uri=oe-16-26-21434&seq=0) on this and they recommended using the green channel and not the red. Very surprising to me, considering most light used in biosensing depends on red light being more permeable in our skin than the other colors. 

The final signal is only 1-2 intensity level changes of the average on my face. It's kinda crazy to me to know that we can get that kind of noise-free resolution after averaging. Amazing what we can do with today's sensing capabilities.

![PPG from a crop under my eyes, with better signal. You can see the fluctuation of my face intensity from the graph itself]({{ url_for('static', filename = 'PPG_forehead.png')}})
<p class="caption">PPG from a crop under my eyes, with better signal. You can see the fluctuation of my face intensity from the graph itself</p>

You also have to be holding incredibly still. Any movement changes the lighting on your forehead, which screws up your intensity chart massively. Even the back-and-forth movement caused by your heart beating screws it up, but if you hold super still it works very reliably. 

I want to use this for an art project, but the error arising from movement makes it impossible. Not sure how to fix either, since the error depends on your lighting environment. 

That's all for now. Cya next time!
