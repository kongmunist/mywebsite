title: "Stroop Effect vs. Sleep duration"
date: 2024-01-10
label: blog
tags: [personalinformatics, quantifiedself, data]
snippet: "Preliminary results from collecting too much personal data"

 

Hello​! I have been collecting my Stroop effect data for about three months now, and I have my Fitbit data spanning the whole period. A friend asked me how my sleep affects my Stroop data, and I decided to go ahead and set up the analysis because I was also curious. 

{{ add_pic("stroopvssleep/0.png", "") }}

When doing any personal data analysis, we must try to be scientific about it. I'm not gonna just throw up a random best-fit line and ask you to trust the coefficients — there's also the p-value for the probability that the slope is that value by random chance. I have also Bonferroni-corrected the threshold value, though I think this boundary is a bit arbitrary (we pick p=5% arbitarily like everyone else, then divide by 12 to Bonferroni correct. p<.00416 is significant).

As you can see, while there are some data series which appear to be related (most notably Stroop score vs. sleep duration), but they are not actually by our experiment. I would need more data to confirm, and there are only 27 days of data here because I have not been collecting Stroop for long. 

Now, if the top-right graph were significant, then it would show that my Stroop interference time goes down with the more sleep I have. Stroop interference should go higher with less executive function, and so we see the expected relationship in my data if we believe more sleep good. However, I've been pondering <a href="https://guzey.com/theses-on-sleep/">Guzey's work lately in the realm of sleep deprivation, and I hoped to see something surprising. Alas, we will wait for me to generate more data. 

# Aside or Favor

I'm working on a Quantified Self dashboard with the ability to upload any time series data and see how it correlates with your other data. As part of this, I've written a lot of basic OOP-y code which allows large scale analysis — this code is not good, but it is generalizable enough for now. If you're interested in using the same structures to analyze your data (code request) or working on this project and have the time to commit to it (collaboration), please email me! I am trying to bring this to fruition for others to use. In particular, please contact me if you know anything about modern software best practices, because I do not. 
