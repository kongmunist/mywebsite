title: Learning AppleScript
date: 2022-01-05
label: blog
tags: [applescript, scripting, quantifiedself]
snippet: Go Go Mac Powers

Hello. I've always wanted to learn AppleScript in order to replace my Mac tracking apps and save a bit of money. Over this break, I had time to do that. And it seems to be about as hard as I expected it to be, which is to say it's simple to the point of being hard to learn. Here's an example

Applescripts is written in this natural language sort of format. You expect that makes it easier to learn and read and write, but it doesn't unless you know the syntax. Much like how a Python aficionado would find it difficult to explain to a newbie how they know of all the different built-in functions, I find it similarly hard to learn the types and values that variables can take on in an AppleScript. 

I've written a few atomic scripts and tips I wanted to share, and I'll show them in this post. Like usual, examples of other scripts helped me learn how to write my own. For Applescripts, I had an interesting problem that my example code wouldn't work when I began to switch in my own variables. This leads me to tip #1

# Tip #1: Do not name your variables "yes"
Everyone has a default name for trash variables that will be replaced by something more descriptive later, and mine happens to be "yes". However, if you name your variables yes in your Applescript, you are going to have a bad time. The script throws a funky error that doesn't mention that yes is a built-in word that cannot be assigned. 

# Tip #2: Applescript has no OOP, at least officially
This means when you try to write a more complicated Applescript and want to be a good little SWE who uses objects and functions, you will encounter various forum posts which tell you that AS is not meant for this stuff and you should give up. Maybe I just phrased my problem poorly, but my desire to make functions is solved perfectly by subroutines, which nobody mentioned until I saw it on an Applescripts blog. 

There are also not AppleScript blogs in the same way that there are Javascript/CSS blogs. Being Apple fans, each of the AS tutorial websites is written in a legible fashion. However they are nowhere as smooth as those CSS blogs showing live examples of X property. I understand that this is because scripts cannot be played online, but it still makes it hard when they show no pictures of what the output is supposed to look like. 

OK, onto the examples.

# Examples
### Spotify Context

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888">############ Get current spotify usage</span>
<span style="color: #008800; font-weight: bold">on</span> <span style="color: #996633">getSpotify</span>()
    <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">retList</span> <span style="color: #008800; font-weight: bold">to</span> {<span style="background-color: #fff0f0">&quot;&quot;</span>}
    <span style="color: #008800; font-weight: bold">if</span> <span style="color: #007020">application</span> <span style="background-color: #fff0f0">&quot;Spotify&quot;</span> <span style="color: #000000; font-weight: bold">is</span> <span style="color: #996633">running</span> <span style="color: #008800; font-weight: bold">then</span>
        <span style="color: #008800; font-weight: bold">tell</span> <span style="color: #007020">application</span> <span style="background-color: #fff0f0">&quot;Spotify&quot;</span>
            <span style="color: #008800; font-weight: bold">if</span> <span style="color: #996633">player</span> <span style="color: #0000CC">state</span> <span style="color: #000000; font-weight: bold">is</span> <span style="color: #0000CC">playing</span> <span style="color: #008800; font-weight: bold">then</span>
                <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">tr</span> <span style="color: #008800; font-weight: bold">to</span> <span style="color: #996633">current</span> <span style="color: #996633">track</span>
                <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">retList</span> <span style="color: #008800; font-weight: bold">to</span> {<span style="color: #0000CC">name</span> <span style="color: #008800; font-weight: bold">of</span> <span style="color: #996633">tr</span>, <span style="color: #996633">artist</span> <span style="color: #008800; font-weight: bold">of</span> <span style="color: #996633">tr</span>, <span style="color: #996633">player</span> <span style="color: #0000CC">position</span>, (<span style="color: #996633">duration</span> <span style="color: #008800; font-weight: bold">of</span> <span style="color: #996633">tr</span>) <span style="color: #333333">/</span> <span style="color: #0000DD; font-weight: bold">1000</span>, <span style="color: #0000CC">id</span> <span style="color: #008800; font-weight: bold">of</span> <span style="color: #996633">tr</span>}
            <span style="color: #008800; font-weight: bold">end</span> <span style="color: #008800; font-weight: bold">if</span>
        <span style="color: #008800; font-weight: bold">end</span> <span style="color: #008800; font-weight: bold">tell</span>
    <span style="color: #008800; font-weight: bold">end</span> <span style="color: #008800; font-weight: bold">if</span>
    <span style="color: #003366; font-weight: bold">return</span> <span style="color: #996633">retList</span>
<span style="color: #008800; font-weight: bold">end</span> <span style="color: #996633">getSpotify</span>
</pre></div>

My problem with learning from example Applescript I read online is that the examples are not clearly cross-applicable and the errors you get are not helpful. I can read this code perfectly fine, and you probably can too — but it's a trap to trick you into thinking you know how to write it! This took me like an hour because I kept naming my variable yes, but even when I stopped that it still took me a while to realize "application "x"" is not replaceable with a macro like it would be in C. 


### Current date and time, formatted as a timestamp or filename
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888">########## get current date/time formatted as a sortable string</span>
<span style="color: #008800; font-weight: bold">on</span> <span style="color: #996633">date_format</span>(<span style="color: #996633">adate</span>) <span style="color: #888888">-- Old_date is text, not a date.</span>
    <span style="color: #008800; font-weight: bold">set</span> {<span style="color: #007020">year</span>:<span style="color: #996633">y</span>, <span style="color: #007020">month</span>:<span style="color: #996633">m</span>, <span style="color: #007020">day</span>:<span style="color: #996633">d</span>, <span style="color: #996633">time</span>:<span style="color: #996633">t</span>} <span style="color: #008800; font-weight: bold">to</span> <span style="color: #996633">adate</span>
    <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">delim</span> <span style="color: #008800; font-weight: bold">to</span> <span style="background-color: #fff0f0">&quot;.&quot;</span>
    <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">yada</span> <span style="color: #008800; font-weight: bold">to</span> (<span style="color: #996633">y</span> <span style="color: #008800; font-weight: bold">as </span><span style="color: #BB0066; font-weight: bold">string</span>) <span style="color: #333333">&amp;</span> <span style="color: #996633">delim</span> <span style="color: #333333">&amp;</span> (<span style="color: #996633">m</span> <span style="color: #008800; font-weight: bold">as</span> <span style="color: #996633">integer</span>) <span style="color: #333333">&amp;</span> <span style="color: #996633">delim</span> <span style="color: #333333">&amp;</span> <span style="color: #996633">d</span> <span style="color: #333333">&amp;</span> <span style="color: #996633">delim</span> <span style="color: #333333">&amp;</span> <span style="color: #996633">t</span>
    <span style="color: #003366; font-weight: bold">return</span> <span style="color: #996633">yada</span>
<span style="color: #008800; font-weight: bold">end</span> <span style="color: #996633">date_format</span>
</pre></div>

Here you'll note that I did not include the word "yes" as my variable, but notice how similar it is to the current variable "yada". Wonder how that happened...

### Get currently focused app and path to that app
Remixed from [Stack Overflow](https://stackoverflow.com/questions/5292204/macosx-get-foremost-window-title)
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888">############ Get URL and name of focused app</span>
<span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">windowTitle</span> <span style="color: #008800; font-weight: bold">to</span> <span style="background-color: #fff0f0">&quot;&quot;</span>
<span style="color: #008800; font-weight: bold">tell</span> <span style="color: #007020">application</span> <span style="background-color: #fff0f0">&quot;System Events&quot;</span>
    <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">frontApp</span> <span style="color: #008800; font-weight: bold">to</span> <span style="color: #007020">first</span> <span style="color: #007020">application</span> <span style="color: #996633">process</span> <span style="color: #007020">whose</span> <span style="color: #0000CC">frontmost</span> <span style="color: #000000; font-weight: bold">is</span> <span style="color: #003366; font-weight: bold">true</span>
    <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">frontAppName</span> <span style="color: #008800; font-weight: bold">to</span> <span style="color: #0000CC">name</span> <span style="color: #008800; font-weight: bold">of</span> <span style="color: #996633">frontApp</span>
    <span style="color: #008800; font-weight: bold">tell</span> <span style="color: #996633">process</span> <span style="color: #996633">frontAppName</span>
        <span style="color: #008800; font-weight: bold">tell</span> (<span style="color: #007020">1st</span> <span style="color: #0000CC">window</span> <span style="color: #007020">whose</span> <span style="color: #996633">value</span> <span style="color: #008800; font-weight: bold">of</span> <span style="color: #996633">attribute</span> <span style="background-color: #fff0f0">&quot;AXMain&quot;</span> <span style="color: #000000; font-weight: bold">is</span> <span style="color: #003366; font-weight: bold">true</span>)
            <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">windowTitle</span> <span style="color: #008800; font-weight: bold">to</span> <span style="color: #996633">value</span> <span style="color: #008800; font-weight: bold">of</span> <span style="color: #996633">attribute</span> <span style="background-color: #fff0f0">&quot;AXTitle&quot;</span>
        <span style="color: #008800; font-weight: bold">end</span> <span style="color: #008800; font-weight: bold">tell</span>
    <span style="color: #008800; font-weight: bold">end</span> <span style="color: #008800; font-weight: bold">tell</span>
    <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">appfilepath</span> <span style="color: #008800; font-weight: bold">to</span> <span style="color: #996633">POSIX</span> <span style="color: #0000CC">path</span> <span style="color: #008800; font-weight: bold">of</span> <span style="color: #007020">application</span> <span style="color: #996633">file</span> <span style="color: #008800; font-weight: bold">of</span> <span style="color: #996633">frontApp</span>
<span style="color: #008800; font-weight: bold">end</span> <span style="color: #008800; font-weight: bold">tell</span>
</pre></div>


### Get the URL of any application that has a URL or path (Finder, Preview, Chrome, Safari)
Remixed from Stack Overflow, [[1]](https://gist.github.com/EvanLovely/cb01eafb0d61515c835ecd56f6ac199a) [[2]](https://stackoverflow.com/questions/12129989/getting-finders-current-directory-in-applescript-stored-as-application)
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #888888">############ Get URL of current chrome/safari/preview/finder tab</span>
<span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">currentTabUrl</span> <span style="color: #008800; font-weight: bold">to</span> <span style="background-color: #fff0f0">&quot;&quot;</span>
<span style="color: #008800; font-weight: bold">if</span> (<span style="color: #996633">frontAppName</span> <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&quot;Safari&quot;</span>) <span style="color: #000000; font-weight: bold">or</span> (<span style="color: #996633">frontAppName</span> <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&quot;Webkit&quot;</span>) <span style="color: #008800; font-weight: bold">then</span>
    <span style="color: #008800; font-weight: bold">tell</span> <span style="color: #007020">application</span> <span style="background-color: #fff0f0">&quot;Safari&quot;</span> <span style="color: #008800; font-weight: bold">to</span> <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">currentTabUrl</span> <span style="color: #008800; font-weight: bold">to</span> <span style="color: #996633">URL</span> <span style="color: #008800; font-weight: bold">of</span> <span style="color: #007020">front</span> <span style="color: #0000CC">document</span>
<span style="color: #008800; font-weight: bold">else</span> <span style="color: #008800; font-weight: bold">if</span> (<span style="color: #996633">frontAppName</span> <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&quot;Google Chrome&quot;</span>) <span style="color: #000000; font-weight: bold">or</span> (<span style="color: #996633">frontAppName</span> <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&quot;Google Chrome Canary&quot;</span>) <span style="color: #000000; font-weight: bold">or</span> (<span style="color: #996633">frontAppName</span> <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&quot;Chromium&quot;</span>) <span style="color: #008800; font-weight: bold">then</span>
    <span style="color: #008800; font-weight: bold">tell</span> <span style="color: #007020">application</span> <span style="background-color: #fff0f0">&quot;Google Chrome&quot;</span> <span style="color: #008800; font-weight: bold">to</span> <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">currentTabUrl</span> <span style="color: #008800; font-weight: bold">to</span> <span style="color: #996633">URL</span> <span style="color: #008800; font-weight: bold">of</span> <span style="color: #0000CC">active</span> <span style="color: #003366; font-weight: bold">tab</span> <span style="color: #008800; font-weight: bold">of</span> <span style="color: #007020">front</span> <span style="color: #0000CC">window</span>
<span style="color: #008800; font-weight: bold">else</span> <span style="color: #008800; font-weight: bold">if</span> (<span style="color: #996633">frontAppName</span> <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&quot;Preview&quot;</span>) <span style="color: #008800; font-weight: bold">then</span>
    <span style="color: #008800; font-weight: bold">tell</span> <span style="color: #007020">application</span> <span style="background-color: #fff0f0">&quot;Preview&quot;</span> <span style="color: #008800; font-weight: bold">to</span> <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">currentTabUrl</span> <span style="color: #008800; font-weight: bold">to</span> <span style="color: #0000CC">path</span> <span style="color: #008800; font-weight: bold">of</span> <span style="color: #007020">front</span> <span style="color: #0000CC">document</span>
<span style="color: #008800; font-weight: bold">else</span> <span style="color: #008800; font-weight: bold">if</span> (<span style="color: #996633">frontAppName</span> <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&quot;Finder&quot;</span>) <span style="color: #008800; font-weight: bold">then</span>
    <span style="color: #008800; font-weight: bold">tell</span> <span style="color: #007020">application</span> <span style="background-color: #fff0f0">&quot;Finder&quot;</span>
        <span style="color: #008800; font-weight: bold">if</span> <span style="color: #007020">exists</span> <span style="color: #996633">Finder</span> <span style="color: #0000CC">window</span> <span style="color: #0000DD; font-weight: bold">1</span> <span style="color: #008800; font-weight: bold">then</span>
            <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">currentDir</span> <span style="color: #008800; font-weight: bold">to</span> <span style="color: #0000CC">target</span> <span style="color: #008800; font-weight: bold">of</span> <span style="color: #996633">Finder</span> <span style="color: #0000CC">window</span> <span style="color: #0000DD; font-weight: bold">1</span> <span style="color: #008800; font-weight: bold">as</span> <span style="color: #996633">alias</span>
        <span style="color: #008800; font-weight: bold">else</span>
            <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">currentDir</span> <span style="color: #008800; font-weight: bold">to</span> <span style="color: #996633">desktop</span> <span style="color: #008800; font-weight: bold">as</span> <span style="color: #996633">alias</span>
        <span style="color: #008800; font-weight: bold">end</span> <span style="color: #008800; font-weight: bold">if</span>
        <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">currentTabUrl</span> <span style="color: #008800; font-weight: bold">to</span> <span style="color: #996633">POSIX</span> <span style="color: #0000CC">path</span> <span style="color: #008800; font-weight: bold">of</span> <span style="color: #996633">currentDir</span>
    <span style="color: #008800; font-weight: bold">end</span> <span style="color: #008800; font-weight: bold">tell</span>
<span style="color: #008800; font-weight: bold">end</span> <span style="color: #008800; font-weight: bold">if</span>
</pre></div>


# Conclusion
That's all I got for now. I'm going to try to run a continuous log of my current laptop's "context", so I need file appending eventually. Until then, cya later!