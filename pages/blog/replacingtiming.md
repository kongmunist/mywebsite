title: Replacing Timing
date: 2022-01-09
label: blog
tags: [quantifiedself, applescript, python]
snippet: I promise I'm not trying to be more productive

I have been working on replacing a piece of software I use on a weekly basis. The Mac app [Timing](https://timingapp.com/) is a computer context tracker, which is to say it logs what windows have been open as long as you're using it. It even offers you a beautiful interface to interact with your data through.

<p class="caption">My Timing history for the past year</p>
![Screencap of my Timing history for the past year]({{ url_for('static', filename = 'rt_timingdashboard.png')}})

Timing has cost me $8.50 a month for the past 6 months, and they primarily target freelancers who bill clients by the hour. Unfortunately, I am not a contractor, and Timing does not help me track hours. Timing just offers me a cool composite of time as I've spent it on my laptop in the past day/week/month. And though I can't justify its cost,  I still love the functionality. So I've been trying to replace it. 

# General plan
Timing calls itself a time tracker, but I don't think that's really what I want. I want to know how I'm using my laptop during the course of a day, and make adjustments based on whatever I happen to want to change.

Really, I just wanted to make a background-running shell or Python script that logs my context on the computer, then shows me the aggregated stats once in a while. 

To understand what I'm doing on my computer, I think you need to know A) the current time, B) what I'm listening to, and C) which application is open and for how long. I think these give you a pretty clear picture of my mental state. For example, if I have docs open, I'm probably writing. If I'm on Youtube, I'm watching videos. If I'm on preview, reading. Of course there are exceptions — I could be on YouTube watching gaming videos or electrical engineering tutorials.But it should be good enough. Logging my music will also help me conclusively decide if music helps or harms me when I'm working. 

## Improvements over Timing
My main complaint with Timing is that it didn't ever show me aggregated features pulled out of my data. I don't mean the "automagical insight extraction" that so many data analysis teams claim to implement for millions of dollars. The human brain can do all of that truly automatically, as long as the right data is shown routinely. I simply wanted something showing my usage to establish a feedback loop, and let myself decide what needs to change or not, and how that change has been going historically. 

# What've you done so far? 
So far, I've cancelled my Timing subscription and written a pretty crude day-by-day activity tracker using Applescripts, Bash, and Python. I'm gonna refer to it as Casey for now, just to have a name for it. 

<br><br>

## As a logger, Casey uses only 15% of the storage of Timing while being 50% more efficient

<br><br><hr>

## Performance
Here's a photo of the two programs in the activity monitor, monitoring the same stretch of 16 minutes.  

<p class="caption">CPU time for Timing</p>
![CPU time for Timing]({{ url_for('static', filename = 'rt_cputesttiming.png')}})

vs.

<p class="caption">CPU time for Casey</p>
![CPU time for Casey]({{ url_for('static', filename = 'rt_cputestcasey.png')}})

We see the CPU time of Casey is 5.66 seconds compared to Timing's 7.68, around a 25% reduction. 

The memory footprint of Casey is also lower, sitting at 27.4 MB vs. 48.1 MB for Timing, representing a savings of 22.2%. 

<hr>

## Storage
Casey retrieves user context every second, and accumulated 1033 new lines and 179kB of extra storage during the test. Each record takes up around 173 bytes pre-compression. After compression, the total storage is only 6kB, putting each log entry at 5.8 bytes for Casey. 

![Compressed and uncompressed log sizes for Casey, Finder screenshot]({{ url_for('static', filename = 'rt_stotestcasey.png')}})

I planned on comparing this to Timing's 12kB + 235kB in the sync.db and wal.db respectively (they do not immediately store it into a sqlite database), assuming the same logging rate.  But I personally can't believe that Timing could be so terribly inefficient. At 239 bytes/log, it's worse than Casey when naively storing everything as text directly. I'll instead refer to the 2400 hours of data it has recorded into a storage folder only 320MB in size, including backups. This means it sits at 2346 hours/320.8 MB = 38 bytes/sec. A much more reasonable quantity, still beaten handily by Casey's 5.8 bytes/log.

<p class="caption">My Timing records and how much space they take up</p>
![My Timing records and how much space they take up]({{ url_for('static', filename = 'rt_stotimingrecords.png')}})

# Shortcomings
Casey does not yet have a GUI, or a plan for long-term backup storage. The lookup and indexing system is still not in place, nor is the aggregation of data. Casey also lacks the periodic reminder system that I want it to have through emails. But it's a WIP, so I'm happy to document its baby steps.


# Conclusion
I want to conclude by saying that Timing is a beautifully polished piece of software. I applaud the Timing team for making such a smooth application that does one job and does it well. But it isn't what I wanted, and it's a bit expensive for me. 

The storage and performance don't matter so much since we're talking about such small beans (7 secs on 16 minutes is around 0.7%, 320MB vs 3.2GB is not such a big swing for a year of data), but this is my current optimization. 

More progress tomorrow. 
