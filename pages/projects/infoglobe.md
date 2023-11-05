title: Hacking The Olympia InfoGlobe
date: 2023-11-05
label: project
timespan: June - August 2022
pic: infoglobe_hero.png
description: Kinda-vintage internet-connected spinning-LED bulletin-board

{{ add_pic("infoglobe_hero.png", "", True) }} 

Last year I co-opted an Olympia InfoGlobe display with an ESP8266 and made the code public [here](https://gist.github.com/kongmunist/a8bdadbacda4bcb129cd183f2f0fffc5). 

The hardware details are in blog posts [part 1](https://andykong.org/blog/infoglobetutorial1/) and [part 2](https://andykong.org/blog/infoglobetutorial2/), and I walk through the software in [part 3](https://andykong.org/blog/infoglobetutorial3/)

<hr>

## Motivation/Lore
A middle school teacher was cleaning out their closet and wanted to throw away their InfoGlobe. A valid decision, considering that it's useless without a landline phone and spheres don't pack efficiently. I promised them I'd make something cool with it and saved it from the landfill, at least for a few years. 

I started playing with Arduinos to make this thing say what I wanted, and I got kinda close but never figured out the delays in the IR messaging protocol.

{{ add_pic("infoglobe_earlytry.jpg", "(2018) Early attempt to make the hacked Infoglobe, timings are off so some letters are missing", True) }} 

I revisited it a few years later, while working at a software company. During the day, I'd get tired of looking at computer screens for hours on end, and wanted some way to talk to my friends when I got home that didn't involve typing at them on my phone or computer. The reader may mention letters or other physical artifacts, but I also wanted semi-instantaneous communication. 

With my newfound electrical engineering skills, I vanquished the timing issue and got consistent messages to show up on the InfoGlobe. 

{{ add_pic("infoglobe_booyah.png", "(2022) Photo of the modern, working version of the Infoglobe. Desk has not gotten any cleaner", True) }} 

<hr>
## Interactions now

Then I created a website where anyone could leave messages to be displayed on my 'globe. This is totally unmoderated, so do not get mad at me if it says something mean about anyone.

{{ add_pic("infoglobe_websiteex.jpg", "Screenshot of the Infoglobe website where messages can be uploaded. This is actually how I learned of Gorbachev's death", True) }} 

I also added the time and date as possible messages, because it was easy. Actually it wasn't super easy, since the ESP8266 has no geo-locating features and I didn't want to add them. Basically, there's a secret webpage I can visit on the infoglobe site which sets the time zone offset for the infoglobe. Assuming only I visit the page, then the infoglobe's time will always match my timezone.

{{ add_pic("infoglobe_newsite.png", "", True) }} 

Here's what the the current website looks like. If you are a designer and want to make it look less like an eyesore please hit me up. I have no money but it is a very simple page, and maybe you like the concept enough to send me a Figma link :)

Anyway, here's the website where you can write messages: [aksuper7.pythonanywhere.com](aksuper7.pythonanywhere.com)












