title: "Timezone correcting Fitbit sleep data using Google Timeline"
date: 2024-02-12
label: blog
tags: [fitbit, quantifiedself, timezonecorrection]
snippet: "My last post on dealing with terrible Fitbit data"

Hello friends, I purchased an Apple Watch and (hopefully) escaped from the hellhole that is the Fitbit data environment — forever!

<blockquote class="twitter-tweet" data-media-max-width="560"><p lang="en" dir="ltr">Custom Apple Watch strap that turns it into a tilted driver watch <a href="https://t.co/Ktp1nmskyw">pic.twitter.com/Ktp1nmskyw</a></p>&mdash; Andy (@oldestasian) <a href="https://twitter.com/oldestasian/status/1756578851893760155?ref_src=twsrc%5Etfw">February 11, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

To cap off all my Fitbit posting, I exported my data one last time and noticed that they have restructured the data and ruined my [stress method](../fitbitsleeptzcorrection) for timezone correction, rendering all my latest data unusable. Since I've collected more Tetris and Stroop data that I wanted to correlate, I decided to try one final method that I've always thought about but never cared enough to do — syncing my Google Location with Fitbit's data to get UTC timestamps. I'll describe the steps verbally and the code will be at the end. 

# Method

First I loaded my Google location data with [this neat tool](https://github.com/Scarygami/location-history-json-converter) by Scarygami which produces a massive CSV of all the longitude and latitude and everything else. Here I visualized part of it using plotly's `scatter_mapbox` function. 

{{ add_pic("glocfitbittzcorrection/0.png", "") }}

From each longitude and latitude, you can get the timezone name using the Python library [timezonefinder](https://pypi.org/project/timezonefinder/), which works at a rate of ~2ms/1000 coordinates without needing to do GET requests. I converted the timezone strings into timezone offsets using some code from [this SO post](https://stackoverflow.com/questions/5537876/get-utc-offset-from-time-zone-name-in-python). 

Then I realized that I needed to also account for daylight savings time across two regions, Europe and America, which for some reason have DST dates that are about a week off from each other. I can't wait for them to abolish DST so I'll have to add a bool which determines if DST correction is necessary in my timezone correction pipeline /s

{{ add_pic("glocfitbittzcorrection/1.png", "") }}

Some sleep sessions have no "close" longitude/latitude coordinates, so I toss them. Close is defined arbitrarily, I use 6 hrs as my cutoff. 

My success rate with this method is ~60%, and most of the loss comes from me neglecting to turn on Google Timeline on my iPhone until sometime mid-2021. In total, I recovered 600+ days of _accurate_ Fitbit sleep data and can now produce fun sleep graphs which I can trust. For instance, here is my true Tetris speed vs. sleep graph: 

{{ add_pic("glocfitbittzcorrection/2.png", "") }}

Turns out sleep is good for you, actually.

# Code

Code is provided with no guarantees or user-friendly comments. Use at your own risk, etc. etc.

<script src="https://gist.github.com/kongmunist/a4945c339b11d4e953e5e806344e42c8.js"></script>
