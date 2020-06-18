title: Carnegie Calendar
date: 2020-06-18
label: project
timespan: August - January 2019
pic: CCmain.png
description: All-encompassing, auto-updating events calendar for everything going on at uni


<a href="https://carnegiecalendar.com" target="_blank">Here's</a> the site, and <a href="https://github.com/kongmunist/CarnegieCalendar" target="_blank">here's</a> the GitHub. 

<img class="d-block mx-auto" src="{{ url_for("static",filename="CCmain.png") }}"/>

<hr>

### Why I made it
This site was a personal project attempted in freshman year by me and some overzealous friends. I had some trouble figuring out when/where student orgs were meeting because there was no central location to post all that stuff (and often nobody in the club cared enough to post their events somewhere else), so I wanted to make a searchable site that could collect all that automatically. 

During a hackathon in 2nd semester, we entered with the plan to make this site, since one didn't already exist. We tried to run regex and NLP on the school sites in order to retrieve all the events going on around the school, following every link on the site in the hopes it would redirect to another school site. In the process, we found the branching factor of each school website was about 43, learned how to make websites using Django, and that we suck at demoing after not sleeping for a whole night. 

I later realized many of the websites already had embedded Google Calendars with URLs and everything that I could just download directly. I spent a frenzied three hours collecting every calendar link manually, then wrote a Python script to manually poll all of them and filter the events. No events without a location and time, no events with no description, and no events before the current moment. Timezones are also wacky in .ics files. I learned a lot about the standard. 

<hr>

### How it works
Website is two parts: event collection and searchable front-end. Event collection is done by using the requests library to download every calendar in a very long list that I put together by hand. The ics files are immediately cracked open and their events extracted and added into a big list. This list is filtered, so contains no events with duplicate descriptions or times. After iterating through the entire list of calendars, it saves all the filtered events (and standardizes their timezone information) into one honkin' big .ics. 

<img class="d-block mx-auto" src="{{ url_for("static",filename="CCurllist.png") }}"/>

Front-end is written in Flask, all it does is load in the main .ics and crack it open, displaying all the events through a jinja2 template. There was a lot of weird markdown/prerendering stuff I had to do to the site in order to get the dates to show up as Month Day, Year, instead of 05-12-20 or something, but it looks serviceable. When users search something, the terms are split by comma and we look if the description or title of events contains each search term. This has to be redundancy checked as well. Computers are good enough now that I didn't have to do this in an efficient way at all for the load times to be under 0.5 sec. If a user searches empty string, we just display all the events. The download link performs the search again (search terms are stored in the local storage of the site) and packages the matching events into an .ics that is then downloaded. 


That's all the features!

<hr>

### Bonus: How I advertised for it
I finished this over Winter Break, and then came onto campus a few days before everyone else came back. I decided to put up posters on the billboards around school like everyone else. But unlike everyone else, I decided to run a huge A/B test of which billboard locations were prime scanning locations. I created a script to make every poster have a unique QR code going to the carnegie calendar website (carnegiecalendar.com/1001 for example), then had those redirect to the main site URL. I assigned every billboard a unique number, then write a big spreadsheet of the numbers and their corresponding locations. This way, I could count which redirects were most common and use this data for future advertising. I wrote the number on the QR code very faintly in a corner, and then me and a bunch of friends went and posted them around the school. It took like an hour together, but would've taken me around 5 alone. Thanks, friends.

<img class="d-block mx-auto" src="{{ url_for("static",filename="CCzoomout.png") }}"/>
<p class="caption">Normal poster, from a glance nothing is out of the ordinary.</p>

<img class="d-block mx-auto" src="{{ url_for("static",filename="CCzoomin.png") }}"/>
<p class="caption">As you can see, a tiny hidden number denoting the link</p>

It turns out very few people actually scan the posters on the walls, so I only got around 100 hits on 60 posters. Not super worth it. However, I posted it on Facebook and immediately got like 900 hits before the mods took it down, so I guess social media really is the future of the internet.





