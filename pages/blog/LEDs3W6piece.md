title: Testing out some high power LEDs
date: 2020-12-28
label: blog
tags: [electronics, LED, projectlog, wallscreen]
snippet: Casting light on far away surfaces using 3W LEDs

I bought some cheap, high-power LEDs off Amazon about a week ago. I wanted something really bright that came with a backing, and I didn't want too many. They look like this:

<p class="caption">Cheap, 3W LEDs with aluminum backing connected to a 9V wall adaptor</p>
![Cheap, 3W LEDs with aluminum backing connected to a 9V wall adaptor]({{ url_for('static', filename = 'LED3W_poweringsetup.JPG')}})

I have here soldered it to a 9V wall adaptor, which outputs a DC 9V at 0.3A max load. This is precisely what was specified by the Amazon page, though the accuracy of that I cannot be sure. I tried a 5V at first and that failed. VERY BRIGHT! Hurts to look at for any amount of time, at arm's length. Heats up negligibly when turned on for under a minute.

I funneled their light through my projector lens, but just got something like this. I guess I'll need a diffuser or something between the LEDs and lens to get a uniform wall projection.

<p class="caption">Projected image produced by the LEDs and a lens from a projector clock. All 6 LED segments are separated out, instead of diffused</p>
![Projected image produced by the LEDs and a lens from a projector clock. All 6 LED segments are separated out, instead of diffused.]({{ url_for('static', filename = 'LED3W_projected.JPG')}})

I tried to diode test them using my trusty multimeter, but it saturated. I then tried using a 2V voltage reading across one LED, and it saturated as well! The voltage drop for these babies was 2.8V each!! I've never seen them so high before, though it's probably to do with needing a lot of current to turn on the LED. 