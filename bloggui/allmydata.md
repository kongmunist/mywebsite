title: "My Quantified Self Data Stack"
date: 2024-01-26
label: blog
tags: [quantifiedself, personalinformatics, data, lifelogging]
snippet: "Many cool self-insights and the data logging methods I used"

If you've ever wondered if you sleep worse after drinking coffee in the morning, or how listening to music affects your focus, or if you get weaker after eating a lot, this post is for you. I used to frequently have these musings, and now I just have the data to check for myself. 

In this post I'm going to show a few self-insights I've derived from logging a lot of my personal data. I'll also list all the types of data and how they're collected. 

# Why research

I think it's important to specify "why research" as well as "how research", and this "why" can become insincere when scientists court the big grant-writers in industry and government instead of saying what they really mean. I currently work for myself and will try to be a bit more honest — I like learning how my body and mind interact with my environment to create my lived experience. I also just like to know stuff.

{{ add_pic("allmydata/0.png", "") }}

# What I have found


	My Ritalin blood concentration correlates with better Tetris performance


{{ add_pic("allmydata/1.png", "") }}


	I think better with more sleep (actually one of my most burning questions)


{{ add_pic("allmydata/2.png", "") }}


	My Tetris speed (pieces per second = PPS) correlates slightly with lower humidity


{{ add_pic("allmydata/3.png", "") }}

Here's a [few](https://medium.com/@kongmunist/playing-faster-tetris-by-sleeping-less-3d9b04d30349) more [examples](../blog/stroopvssleep/)

<hr>

# How do you collect the data?

Data that's useful for my analysis is either physical (heart rate, blood glucose, weight), mental (Tetris, Stroop), or environmental (air quality, music, location, computer activity). Data collection can be easy (hard drive space, Google location), or hard (computer activity), or just cost money (Fitbit, Spotify)

Not all the data is obviously useful — some of it is just easy to collect. But most data I expect to use as an 'x' or 'y' variable in some future analysis.

## Automatic data

### Electric Tables

Chrome, websites visited with URL and timestamp. Collected via Tom Critchlow's [JS electric tables script](../blog/settingupelectrictables/)

{{ add_pic("allmydata/4.png", "") }}

### Hard Drive

Every 4 hours, a bash script logs my available hard drive space in bytes. 

{{ add_pic("allmydata/5.png", "") }}

### Location 

Google Maps Timeline is enabled on my phone and records my latitude/longitude every few minutes. I have this data going back a couple of years, and it includes the velocity and predicted mode of transport. 

{{ add_pic("allmydata/6.png", "") }}

### Smartwatch Biometrics

Fitbit records a ton of data and multiple granularities. There's tons of problems with the data itself (documented [here](../fitbittsproblem/) and [here](../fitbitsleeptzcorrection/) ), but the majority is usable. Most usable stuff is probably the nightly sleep stats, minutely heart rate + HR variance, and daily step count. Fitbit offers this data export [through the web interface](<a href="https://www.fitbit.com/settings/data/export">https://www.fitbit.com/settings/data/export</a>)

{{ add_pic("allmydata/7.png", "") }}

### Music

Spotify! It's a bit complicated and I haven't looked into it, but all the streaming data is there. Spotify offers this data export [through the web interface](<a href="https://support.spotify.com/us/article/understanding-my-data/">https://support.spotify.com/us/article/understanding-my-data/</a>)

{{ add_pic("allmydata/8.png", "") }}

### Tweets

Twitter activity, has been used by [ultimape](<a href="https://twitter.com/ultimape/status/1145889385256296449">https://twitter.com/ultimape/status/1145889385256296449</a>) to detect their shifting circadian rhythm, has been used by Andy for nothing so far. Twitter offers this data export [through the web interface](<a href="https://help.twitter.com/en/managing-your-account/how-to-download-your-x-archive">https://help.twitter.com/en/managing-your-account/how-to-download-your-x-archive</a>)

{{ add_pic("allmydata/9.png", "") }}

### Purchasing data

My Apple Card tracks all my purchases. The data is retrieved by manually hitting the "Export CSV" button on each month, and includes the Merchant and category and date.

{{ add_pic("allmydata/10.png", "") }}

### Glucose

I wore a Freestyle Libre 2 CGM for two weeks and have nearly continuous data from that period (15-min intervals). Export is done through web interface.

{{ add_pic("allmydata/11.png", "") }}

### Air quality

I use a QingPing air quality monitor to track my relative humidity, temperature, CO2, particulates (PM2.5), and tVOC (total volatile organic compounds). Through the QingPing IoT app, we can export the past year of data logged at 15-min intervals. 

{{ add_pic("allmydata/12.png", "") }}

## Manual

### Tetris (cognitive)

I play Tetris for fun a few times a day. The website I play on records the stats and timestamps of each game, and I wrote a little Selenium scraper to retrieve it all. I run this every few months to collate all the data into a CSV.

{{ add_pic("allmydata/13.png", "") }}

### Stroop (cognitive)

I use my Strooper [chrome extension](../../projects/strooper) and complete a mini-Stroop test a few times a day. This gives me a coarse metric of my executive function, reading speed, and reaction time randomly throughout the day. I transfer the results into a spreadsheet monthly. 

{{ add_pic("allmydata/14.png", "") }}

{{ add_pic("allmydata/15.png", "") }}

### Weight and grip strength

Every night I record my weight and fat % with a bioimpedance scale, then record my left and right handed grip strength using a dynamometer. I record these as calendar events and transfer them to spreadsheets monthly. 

{{ add_pic("allmydata/16.png", "") }}

### Dose times

I frequently drink caffeinated beverages, sometimes use nicotine patches, and randomly try out OTC supplements like L-Theanine or magnesium. I update a calendar notebook with my dosage and time, and have gotten pretty good at just noting the time when I take them and logging it later. I transfer this to a spreadsheet every month or so. 

{{ add_pic("allmydata/17.png", "") }}

<hr>

# Do it now!

Collecting personal data for long periods of time has compounding returns — you'll need to gather enough data points to average out daily fluctuations. So if you're reading this and even slightly curious — set up as many as possible ASAP! Storage is cheap, especially for single-user data like this, and in the worst case you can just delete it all. 

# Conclusion

I hope this gives you some idea of the scope of data that can be collected for minimal effort on your part, and the potential cool graphs you can make from it. If you think of any cool correlations I should do with this, please DM and tell me!
