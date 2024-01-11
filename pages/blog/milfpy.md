title: Average clip duration in MILF Manor
date: 2023-06-11
label: blog
tags: [python, clipduration, milf]
snippet: Gauging the audience attention span from TLC dating shows

Whenever I'm watching unpretentious TV like sports or reality TV, I calculate the average clip length. I get my phone stopwatch out, and enter a lap whenever a cut happens. 

Do this maybe 20 times, and you usually get some idea of the distribution. Usually the cuts happen so quickly and fluidly that you may notice yourself _missing_ a few cuts, even though every pixel on the screen dramatically changes and it seems like something you'd notice. 

Recently I watched Milf Manor, a "reality" dating show where older women seeking younger men are paired with younger men seeking older women on a fancy island. The twist is that every young man is the child of one of the older women. Hilarity ensues (?). 

{{ add_pic("milf_cutfeature.jpg", "The complicated feature I used for detecting jump cuts") }}

Common decency aside, this show jump-cuts like nothing else. I did my stopwatch thing but didn't want to stop there — I really wanted to know all about the cut length distribution. I downloaded an episode and used the change in standard deviation of the absolute color difference of two adjacent frames. When this number crossed ~30, I called it a cut and recorded the frame number.

Then I calculated a few stats about it. Here they are:

{{ add_pic("milf_stats.png", "Avg clip length is 2.48 sec, with the median at 1.92 sec") }}

While the average clip length is 2.5 seconds, the median is only 2 seconds. I also find it interesting that the average human blink rate is 1 blink per 4-5 seconds, which means we can see around two clips between blinks. Since the average blink takes ~0.3 seconds, we also won't miss much of a clip while blinking.

{{ add_pic("milf_cutdistro.jpg", "Milf Manor clip duration histogram") }}

# Conclusion
The difficulty of identifying a cut in a video surprised me, but it makes sense if you consider all the possible transitions (fade to black, fade to another clip, slo-mo transition to real-time, etc.). There is even a library in Python called [scenedetect](https://pypi.org/project/scenedetect/) which identifies these for you. Next time I will definitely use that for cut detection instead of making my own feature. 

I have completely satisfied my curiousity about Milf Manor at this time. 
