title: Strooper
date: 2024-01-08
label: project
timespan: October 2023
pic: strooper/strooper_icon.png
description: A Chrome extension for tracking your cognitive performance whenever you visit particular websites

{{ add_pic("strooper/strooper_storepage.png", "") }}

Strooper is the first Chrome extension I've ever made that worked. It pops up a Stroop test which you must complete whenever you visit a user-specified list of websites, and logs your performance to the localStorage. Check it out [here](https://chromewebstore.google.com/detail/strooper/bmpmimimabakkagnniammiljclhjcmgi)!

# Background

The Stroop test is a cognitive performance test invented by John Ridley Stroop in 1935. Participants are shown a list of 100 color words (red, blue, green, etc.) which are colored in a different color from the word itself ("blue" would never show up blue). 

{{ add_pic("strooper/img_1.png", "") }}

If you give it a try with the list above, you'll notice it's pretty confusing. Here's a graph from the original paper where 1 is the time to name a color shown in its own color (congruent, no interference) and 2 is naming the color shown in a different color (incongruent, interference). 2 takes longer than 1, and their difference is the Stroop effect.

{{ add_pic("strooper/img_2.png", "") }}

Psychologists use the Stroop test as a measure for executive function and selective attention because they believe that a test participant must suppress their stronger urge to read the word in order to say the color instead. Here's [the first article](https://psycnet.apa.org/doiLanding?doi=10.1037%2F0894-4105.21.2.251) I found about people with ADHD doing worse on the Stroop test, but there are many, many more about other conditions and variants.

# Motivation
I wanted to track my cognitive performance to see if I got any terrible effects from sleep deprivation, caffeine intake, etc. Since I was previously using [Tetris](https://kongmunist.medium.com/playing-faster-tetris-by-sleeping-less-3d9b04d30349) as a cognitive proxy, taking the Stroop test seemed like a nice step-up. 

{{ add_pic("strooper/img_3.png", "") }}

While researching, I found only terrible Stroop tests online (click instead of keyboard button, no logging), and felt the strong desire to make my own.

I had a lot of Tetris data because I played it a few times a day, and I wanted the Stroop data at the same frequency. But I knew that taking the Stroop isn't as fun as playing Tetris, so I wouldn't be able to displace it directly.

Instead, I needed to hijack my Tetris play time with the Stroop test, using the Stroop as a gate that needed to be passed each time if I wanted to play Tetris. It needed to be a Chrome extension.

# Development
I spent four hours failing to figure out how to make a `manifest.json` for a Chrome extension, then paid a Moroccan guy 13 dollars on Fiverr to write the skeleton code. Shoutout to [Mohammed](https://www.fiverr.com/autowebsy)!

The true Stroop test has three separate subsections to adjust the Stroop effect score by individual color naming and reading speeds. I've incorporated all three of these for more data. I think the color naming and reading tests are basically reaction time tests, and the Stroop effect gives a less low-level measurement of cognitive control.

Since taking the full Stroop test takes around 3 minutes, I also shortened each subtask down to 4 trials administered with four colors — the overall test should take less than 10 seconds.

Finally, an unintended side effect is as a focusing agent. Currently, I have Strooper set to open on YouTube. If I ever open the homepage to browse for anything, I have to do a Stroop. This is annoying, and means that sometimes I just leave without ever watching anything. Great for productivity!

# Privacy
All your data is stored in the localStorage, so it's device-only. 

There are many permissions required for the extension because it must inject HTML/JS into any website in order for you to be able to use it on any website. If it helps, I don't really want to have to house your data along with mine — there's really nothing interesting/profitable I can do with it. 

# Usage
Here is a demo video using Strooper. I complete a test gatekeeping my Tetris website, then I see the result in the popup.

<div class="video-container">
    <iframe class="youtubevideo" src="https://www.youtube.com/embed/2bOjkHnEKlU" allowfullscreen></iframe>
</div>

<hr>
# Pre-emptive FAQ
## Does short stroop even measure anything?
Taking the test needs to be easy, and for me that meant keeping it brief. Prior research has generally stuck with 20-100 item Stroop tests, but I see no reason why the Stroop effect will not be exhibited on a 4-item test. Of course, it will be noiser, but better noisy data for years than great data for a week.

## Why are there three scores?
I got this from reading ["Scoring the Stroop Test"](https://psycnet.apa.org/record/1966-02137-001) by Arthur Jensen. 

Basically, there were a lot of different score calculation methods floating around and he wanted to figure out which ones were actually useful. He got a big batch of data, calculated all the different scoring methods, and noted which ones were redundant using PCA. That left us with scores B, D, and E. 

{{ add_pic("strooper/img_5.png", "") }}

Scores A, B, and C are the scores of the three subtasks in order. B is the reading speed, D = A/(A+B) (color naming score regularized by reading speed), and E = C-A (Stroop effect score)

I enjoyed this paper, really I just love reading old research to see how the wording and procedures have evolved. 

## Does it work if we hit/click the buttons instead of saying it out loud?
Manually doing the Stroop gets just as much interference as verbally doing it, according to a few papers I found [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5686059/) and [here](https://journals.sagepub.com/doi/abs/10.2466/pms.1977.45.1.11). 


## Stroop sucks, it doesn't really measure anything
As mentioned above, even if the Stroop effect itself is not useful, the approximate reaction time scores can be useful anyway. But please email me with your proposed alternative, I am eager to consider new tests.

<hr>

# Prior work in n=1 cognitive performance tracking
- Dynomight's [Puzzle Storm improvement](https://dynomight.net/puzzle-storm/) article - Dyno, if you're reading this, you owe me an email!
- ACX [WordTwist vs. CO2](https://www.astralcodexten.com/p/eight-hundred-slightly-poisoned-word)
- My [Tetris vs. Sleep article](https://kongmunist.medium.com/playing-faster-tetris-by-sleeping-less-3d9b04d30349)
- Alexey Guzey's [Aim Trainer vs. Sleep](https://guzey.com/science/sleep/14-day-sleep-deprivation-self-experiment/) experiment
- No results, but KPier's [Chess](https://www.lesswrong.com/posts/nvRauqCD3u5hdkLm9/chess-and-cheap-ways-to-check-day-to-day-variance-in) article

Here's a graphic I made for my email to Mr. Mite comparing the different tests.
{{ add_pic("strooper/img_4.png", "") }}

[//]: # ()
[//]: # (Tetris - 90hr, 850 games)
[//]: # (Puzzle storm - 18hr, 358 games)
[//]: # (Aim Trainer - 3hr, idk how many games)
[//]: # (Wordtwist - 40hr, 800 games)



<br>