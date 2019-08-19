title: Spotify Force Queueing
date: 2019-07-31
label: project
timespan: July-August 2019
pic: kerokerokerokerokerokero.png
description: A Python program using Spotify APIs to forcibly queue songs on collaborative playlists when you don't have aux control

I made this project to solve the niche issue the backseat rider faces when they are added to a collaborative playlist but the guy in the passenger seat keeps queueing the songs they want to hear but not the ones the backseat rider wants to hear. The way I chose to remedy this was to add the desired song a few hundred times (~800 seems like a good amount), heavily increasing the chance that the next random song is the song that the backseat passenger wants to hear. I call this technique "force-queueing", just to have the excuse of using a word with 5 vowels in a row

Anyway. Let's get technical. 

<img class="d-block mx-auto" src="{{ url_for("static",filename="fqspotifyapichart.png") }}"/>
<p class="caption">It is already alienating how rigid the API calls have to be; no, it isn't nice to see it on a convoluted, 6 step, 3 level chart. </p>


APIs are hard to use. Debugging is almost nonexistent in the form of vague codes (anything above 400 is bad, ~200 is usually good), and the naming rules use URL headers to encode information. In addition, the lack of distinction between query parameters, header parameters, and body parameters is so unclear and never enumerated well on the API site itself. 

I like to think of my computer as a packet cannon; the API calls I send out are just well-aimed payloads at other packet cannons (servers) that contain information on where to shoot back what kind of data. So, that being my mental model, I am vastly confused by the permissions and authorizations and authentications that making any sort of API call requires. What the hell does the official OAuth site mean when it says that the differences between **Authentication** and **Authorization** are like the distinction between fudge and chocolate? Phenomenal explanation, gentlemen. Thank god I never plan on touching a server as long as I live. 


<img class="d-block mx-auto" src="{{ url_for("static",filename="kerokerokerokerokerokero.png") }}"/>
<p class="caption">A great playlist I made</p>

I registered my application under my Spotify Developer dashboard and gave it a callback URL that I would be hosting with [Flask](https://palletsprojects.com/p/flask/) (127.0.0.1/spotify/callbacks). Using the Python [requests](https://2.python-requests.org/en/master/) library, I made a few GET requests to the authorization URL provided by the Spotify Web API platform in order to make sure my application token worked. 

Then, I launched the user authentication webpage which gave my application 'public-playlist-modify' permissions through a token after I logged in with my Spotify user account. I couldn't figure out how to parse headers from my callback Flask site, so I copy-pasted it into my script body. After this, instead of getting '403 Unauthorized' I got '400 Error parsing JSON'. Whose error? Mine, or the Spotify server? How do i fix the way you or I parsed it? Stack Overflow was unhelpful on this occasion, and I got frustrated with the project at this point.

<img class="d-block mx-auto" src="{{ url_for("static",filename="fqspotipy.png") }}"/>
<p class="caption">Something made by someone smarter than I am</p>

And it turns out anyone who wants to make a Python-controlled Spotify API harness just uses 'pip install spotipy'. That's cool I guess, just read the docs for [that](https://spotipy.readthedocs.io/en/latest/). 