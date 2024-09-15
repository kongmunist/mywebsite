title: How to get access to your Fitbit data (API tutorial)
date: 2021-07-26
label: log
tags: [tutorial, API, fitbit]
snippet: Navigating a slightly complicated process for API noobs

I bought a Fitbit to access my heartrate live, or at least to track the way it changes over time. After wearing it for about two weeks, I figured I had enough data to begin requesting it through their API. However, I got confused because there's a bunch of different API names and webpages. I figured it out, and here's how you do the same.

My end goal is a command line GET request that dumps my heartrate logs, for use in Python scripts or a website. To get there, we will use the Web API.

# 1. Sign in and register your app [here](https://dev.fitbit.com/apps/new)
Any URL will do for every URL they ask you for. For every URL I just used my personal website (the one you're sitting on now!). This is meant for external users, so when they agree to let you access their data you can get their authorization token. However, I'm just setting it up once, so I'm ok with manually snipping out my keys and such from the URL redirect. 

I also selected "Personal" while registering my app, so I can get higher fidelity heartrate data.

<p class="caption">Register a Fitbit app page</p>
![Register a Fitbit app page]({{ url_for('static', filename = 'fitbit1_register.png')}})


# 2. Head to "Manage My Apps" and click on "Oath 2.0 tutorial page" [[link here]](https://dev.fitbit.com/apps/oauthinteractivetutorial)

I left all the settings default and clicked the link under step 1. Accept the agreement, and you will be redirected to the page you filled in earlier, with a bunch of params after a "#". Copy everything past the "#" and paste it in the "2. Parse response"

After pasting, the site should auto-generate you an "API endpoint URL: `https://api.fitbit.com/1/user/-/profile.json`" as a `curl` command. It redirects to your own profile though. To ask for more useful information, you can check out the Web API reference [here](https://dev.fitbit.com/build/reference/web-api/heart-rate/). For instance, to get heartrate, the API endpoint is `https://api.fitbit.com/1/user/-/activities/heart/date/today/1d.json`. Paste this in, and you should see the command change. 

I'm not going to show you any commands I ran, that would give away my Auth token. Here's the results of the heartrate one though. Granularity goes down to 1 second, though I'm not sure why you would need that. 

<p class="caption">Successful heartrate output from the terminal</p>
![Successful heartrate output from the terminal]({{ url_for('static', filename = 'fitbit1_heartrateout.png')}})

This is a short post, but I wasn't sure what else needed to be done while I was navigating the process. Turns out it's just two things. Cya next time!
