title: Setting up Electric Tables v0.2
date: 2022-04-22
label: blog
tags: [electrictables, notes, logging, javascript, web]
snippet: Shoutout to Tom Critchlow

Hello everyone! I've recently been thinking about how much time I spend on my computer, and I've gotten gotten into activity logging so I can reflect on the countless hours spent on here. There are other tools out there, but many are manual and many are paid, and I just can't be bothered with either. 

<hr>

## Browser as a Memex

{{ add_pic("rt_timingdashboard.png", "Screenshot from my Timing dashboard, back in my period of riches") }}

Over half of all my computer activity happens in the browser, so I've decided to start with indexing browser activity automatically. 

[Tom Critchlow](https://tomcritchlow.com/) recently released this great bookmarklet tool he calls [Electric Tables](https://tomcritchlow.com/2022/02/07/electric-tables-v2/), which template matches onto author names, titles, dates, and more to index a website as a row in a spreadsheet. Previously, this used the browser's `localStorage`, but it has since moved to Google Sheets. 

I think this is a great development, and wanted to set up Electric Tables myself. The [gist](https://gist.github.com/tomcritchlow/cbb06a9298fb6cc0804372552fda1f96) that Tom posted with the code had instructions for each step of the way, but silly coder I am, I ran into some trouble setting it up. This post is to clarify what exactly needs to be done so future Andy (and others!) can have less trouble in the future. 

If you're reading this, thanks Tom! 

# Let's begin!
So, theres three things to set up: the Google Script, the Google Sheet, and the Javascript bookmarklet. 

<hr>

## Google Script
Go to [script.google.com](https://script.google.com/home) and sign in, then click "New project" in the top left. It should take you to this blank page

{{ add_pic("et_googlescript1.png", "Blank Google Script") }} 

Name your project, then paste in the code from Tom's [gist](https://gist.github.com/tomcritchlow/cbb06a9298fb6cc0804372552fda1f96) under `electrict-tables-v0.2.gs`. Feel free to delete the starter `myFunction`. 

We need to add a dependency called Cheerio which scrapes the text from websites. Hit the plus icon next to "Libraries" on the left panel, and include [Cheerio](https://github.com/tani/cheeriogs) by looking up the Script ID: `1ReeQ6WO8kKNxoaA_O0XEQ589cIrRvEBA9qcWpNqdOP17i47u6N9M5Xh0`. Hit "Add" to include it.

{{ add_pic("et_googlescript2.png", "Google Script with code, looking up Cheerio successfully") }} 

Now we just gotta publish it to the web. Click "Deploy -> New deployment", and select "Web app" as the type. I don't think the type matters for functionality, and you can leave the options as default. 

When you click deploy, you'll get a permissions popup screen. Since only you can run this script, it's safe to allow it to edit your spreadsheets, so go ahead and give it permission.

If you go to Deploy->Manage deployments, you can grab the Web app URL. We'll need this for our bookmarklet. 

{{ add_pic("et_googlescript3.png", "Our script's API endpoint URL") }} 


<hr>

## Google Sheet
Create a new Google Sheet, making sure it's under the same Google account as your script. We're going to add headers to the file so added rows are properly formatted. The column names are case-sensitive!

{{ add_pic("et_googlesheet.png", "A properly set up Google Sheet") }} 

I've also highlighted the Sheet ID in the URL. We only need this bit for the bookmarklet, not the whole thing. 

<hr>

## Bookmarklet
Last step, the actual trigger for adding pages to Electric Tables. Open your favorite text editor, and paste in `bookmarklet.js` from Tom's [gist](https://gist.github.com/tomcritchlow/cbb06a9298fb6cc0804372552fda1f96). 

You only need to add the macro URL from step 1 (should look like "[script.google.com/macros/s/....../exec]()") and the spreadsheet ID (should look like `AodN89ua98dWL12O1oidRTa...` and be really long)

Then head over to a [bookmarklet generator](https://caiorss.github.io/bookmarklet-maker/) and copy in your edited `bookmarklet.js`. Hit "Run Code" to test it out, and the Electric Tables menu should pop up in the top right of your screen. Add a note, then click "Submit". 

{{ add_pic("et_bmtesting.png", "Bookmarklet page getting indexed") }} 

Tab over to your Google Sheets page, and you should see a new row with the bookmarklet site and your note appear after a second.

{{ add_pic("et_newrow.png", "Successful Electric Tables entry!") }} 

Celebrate! Now you can just drag the bookmarklet button onto your bookmarks bar to make a button for it. You can also create a bookmark, then for the URL paste in the "Output" Javascript function. 

{{ add_pic("et_handbookmark.png", "Adding bookmarklet manually") }} 

<hr>

# Wrapping Up

So, you should have a nifty little bookmark sitting in your bookmarks bar that catalogues interesting pages you find for later, and it's all stored on Google's big boy servers! No need to remember it all yourself anymore (as if you were doing that before 😜)

{{ add_pic("et_bookmarklet.png", "Electric Tables bookmarklet") }} 

Happy searching!
