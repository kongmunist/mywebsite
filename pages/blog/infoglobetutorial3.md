title: Infoglobe Tutorial Pt. 3 — Software
date: 2023-04-09
label: blog
tags: [infoglobe, software, gist, tutorial]
snippet: Adding bits to our atoms

<style>
    /* Limit height. Show scrollbars when exceeding height */
.gist .blob-wrapper.data {
   max-height:40vh;
   overflow:auto;
}
    </style>

Ok, welcome back for our final installment of the infoglobe tutorial series. If you've not been following along, here's links to the hardware mods that you'll need to have done before this post will be useful to you — [part 1](../infoglobetutorial1) and [part 2](../infoglobetutorial2).

{{ add_pic("igt1_hero.jpeg", "") }}

If you've forgotten, here's the device we're hacking - the Olympia Infoglobe. I have described it too often, so we're gonna get right into the meat of this post. 

<hr>

# Code
We're using the Wemos D1 mini ESP8266/ESP32 breakout board to control our globe, it looks like this.
{{ add_pic("igt3_wemos.png", "") }}

Boot up your Arduino IDE and download the "IRremoteESP8266" library from the Tools->Manage Libraries-> then search for IRremoteESP8266. This library should be supported for ESP32s as well. Hit install, and twiddle your thumbs for a bit as it installs.

{{ add_pic("igt3_irlib.png", "") }}

Now, copy past [this gist](https://gist.github.com/kongmunist/a8bdadbacda4bcb129cd183f2f0fffc5) into a new Arduino file and upload it to your ESP board. 
<script src="https://gist.github.com/kongmunist/a8bdadbacda4bcb129cd183f2f0fffc5.js"></script>

This script is a demo showing the usage of all the functions we have to make controlling the Infoglobe easier. If you read through the `loop()` function, then you'll begin to understand the code and become able to extend it to your own beneficial/nefarious purposes.

If all went well and your ESP and Infoglobe are both powered up, you should see a "Hello World" message swirling around. You can change the default message on line 47, or you can open the Serial Monitor to upload a message to the Infoglobe immediately. 

## Example use case

I've personally written some code which lets the Infoglobe connect to my wifi and access [this website](https://aksuper7.pythonanywhere.com/) I made for receiving notes from my friends. If you type a message and my globe is plugged in, I'll be able to see the message right on my Infoglobe. Pretty cool, right? 

{{ add_pic("igt3_example1.png", "Website to connect digital friends to my physical environment") }}

I know of other people using their infoglobes as a weather/disaster reporting station, or a way to visualize Alexa messages. 


## Alternatives to ESP
It should be possible to substitute in any microcontroller which is supported by one of the IRremote libraries, since it should work as long as the function names are identical.

## More code?
There are some cool folks working on a more sophisticated platform for interacting with the Infoglobe, but I don't currently have the link for that. Hopefully I can update this soon with the link.

# That's all folks!
What will you do with your Infoglobe? I'd love to see it! Please feel free to email me if you get it working :)

Happy hacking!




