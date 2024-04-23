title: "How To Set ATtiny Fuses (with Arduino as ISP)"
date: 2024-04-23
label: blog
tags: [electronics, arduino, attiny]
snippet: "Change clocks, reduce startup delay, and more!"

Hello! This post'll show you how to set the fuses on an Attiny using the arduinoi IDE and an ARduino as ISP. You'll need to do this to confirugre som new optins on the ATtiny that arne't abaivltle in the ArdinoIDE dropdown. Were geonna start off wherw ew levft off in the blog post [befioejor](../ard2attiny), so be sure to follow that thorugh if you hventh yet.

Hello! This post will show you how to set the fuses on an ATtiny using the Arduino IDE and an Arduino as ISP. You'll need to do this to configure some new options on the ATtiny that aren't available in the Arduino IDE dropdown. We're gonna start off where we left off in the [previous blog post](../ard2attiny), so be sure to follow that through if you haven't yet.

{{ add_pic("attinyfuses/0.png", "") }}

# Motivation

Recently, I wanted to use energy harvesting to power an ATtiny. Every electron is precious in such a scenario, so I had none to waste. However, on startup, I noticed my ATtiny was actually just doing nothing for around 60ms after power-on!

{{ add_pic("attinyfuses/1.png", "") }}

Digging into the datasheet, I found that by default the ATtiny waits 64ms after startup to give the clock time to stabilize. While this is all nice and good, I don't have that kind of power to waste! This could be changed to 4ms or 0ms by setting the LFUSE (datasheet page 26), but I had no idea how — all I knew were the options on the Arduino IDE. From more reading, I learned that the fuses were what changed every time I altered the clock frequency or other pre-code options then hit Burn Bootloader, but I still didn't know how to upload non-common options.

{{ add_pic("attinyfuses/2.png", "") }}

# Custom fuses

##Burn Bootloader command from the CLI

On a forum post someone mentioned you could burn the fuses from the command line using the same command that the Arduino IDE used to burn the bootloader (fuses included). To get the starter command, you can go to Settings->verbose output and turn it on for upload. Next time you hit the Tools->Burn Bootloader button, at the very top of the stdout box will be the command that the IDE tried to run.

{{ add_pic("attinyfuses/3.png", "") }}

When we copy this line elsewhere, we can see exactly where the fuses are in the command. They're towards the end, and encoded as bytes. If you ran this in the terminal, it would do the same thing that hitting "Burn Bootloader" in the IDE does. 

{{ add_pic("attinyfuses/4.png", "") }}

## Determining fuse byte values

One way to set the fuses is to figure out exactly which bits of the LFUSE bytes alter the startup time. In my case, SUT should be 00 for 0ms delay, meaning the right byte should be changed in LFUSE (0x62 above). This approach is possible albeit annoying, and I worried that I had the wrong endian-ness all the time.

{{ add_pic("attinyfuses/5.png", "") }}

The second time, I realized there were several fuse calculators webpages (like [this](https://eleccelerator.com/fusecalc/fusecalc.php?chip=attiny85) or [this](https://www.engbedded.com/fusecalc/)) where you could pick the options and it would auto-generate the correct fuse value. Super!

{{ add_pic("attinyfuses/6.png", "") }}

Once you figure out the fuse bytes, just edit the original Arduino IDE string to include the new values for the appropriate fuses. You can then just run the command in your computer's terminal to set the new fuses on your ATtiny. Now my startup time is <1ms!

{{ add_pic("attinyfuses/7.png", "") }}

Alright, that's all. Cya around!
