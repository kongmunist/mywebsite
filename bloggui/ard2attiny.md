title: "Programming an ATtiny85V using an Arduino"
date: 2024-02-02
label: blog
tags: [electronics, arduino]
snippet: "Blink & SoftwareSerial & ADC, oh my!"

Hello! Today I'm gonna walk you through uploading code to an ATtiny using an Arduino. This was my first time programming a microcontroller off-board, and I got most of the process following [this video](https://www.youtube.com/watch?v=TUlzOD9T3nI). But that video was not sufficient alone, so I'll be describing some of the extra steps in this post.

{{ add_pic("ard2attiny/0.EMt3j09WvLViGEUrJDaZkmKcaX4w5jSaT3oRj9LMgyldTz0IfafKeQj85YxbV3ZQ4YxUOhuMh1HUyttmbQLYNstMIu7YAoF2PBpwnCNt2lSxw3vC_R0hepWty7K7O0ibWZC7oAqn18ZGvdTayleEi1o", "") }}

# Ingredients

You'll need an ATtiny25/45/85 chip, Arduino, 6 jumper wires, a resistor + LED, and maybe a 10uF capacitor. 

# Prepping the Arduino

First we must flash the Arduino with the ArduinoISP sketch (found in File->Examples->11.ArduinoISP). We are using the "old style" wiring, so also uncomment line 81 in this sketch. 

{{ add_pic("ard2attiny/1.25akqCrj6tuWnSYry8gf87gDU0q8DXgPDqxuheHuk09oxtWkfBZIlo0g2_2HUhU7VFHNwziiDA1nXAEPaj65cqnj6T7ciVy1Ce7D40YaiQReM5YqQwcd86nQjoDBYBgqPju3_LqoP1AYdb64XcXT2vE", "") }}

We're not going to program the Arduino again, so go ahead and switch the target board to "ATtiny25/45/85" in Tools. If you don't have this option in your boards, follow the instructions in the [ATtiny repo](<a href="https://github.com/SpenceKonde/ATTinyCore/blob/v2.0.0-devThis-is-the-head-submit-PRs-against-this/Installation.md">https://github.com/SpenceKonde/ATTinyCore/blob/v2.0.0-devThis-is-the-head-submit-PRs-against-this/Installation.md</a>). 

Change the programmer to "Arduino as ISP" as in the image below, and we'll be ready to go. 

{{ add_pic("ard2attiny/2.QNjRaq9X8spoW2y6xI26KncG4jl899N8GxDktKsQuah1eahwwVIZFguWdkMqUT_Zl8FwkCGTFxBFwpHq9g8Cwx9-PIqmlSaHqLvrOLofb35Rvwx2qzN3NS73qnKHqbcr-3Kgj7HZSfCBa1ysypaZprE", "") }}

# Wiring the ATtiny

Now we're going to need those jumpers. Follow this wiring diagram from the video above so we can upload code to the ATtiny

{{ add_pic("ard2attiny/3.HIrpvn1-qmIolI03zWSWAqE3QFjgo0NbPD-kejB-2kK-h16um6U-x69KWVYvMXeZJ_eLOZ1yEaYNUHqRn1OM1HrOYMxtMYox9zhLwKSBQ6Fz7CJ7mtC-HwOmIBntrifX7m4ELjIOGpVFmLafFd3YbcA", "") }}

To do the Blink sketch properly, we need to add the LED and resistor across PB0 and GND. Make sure the longer (positive) leg of the LED is on PB0. 

{{ add_pic("ard2attiny/4.51O5gIuJccwACaAqIhRbEg2n1BwUKAR6xghGU083yULFq8oy17erlE_3aKVw6DvuUE3skPnRjp69M_ixpNPW7Lr4ZAwhsaNVqSSgxlHuOuMroCyqne3Kl8Rj83LBbEAvIn8WkgfNnDllvJrFTYoCd_s", "") }}

# Uploading Blink

If this is the first time your ATtiny is being used or you've changed any build settings, you'll need to hit Tools->Burn Bootloader. This should work with no errors, but if you get one, make sure you've uncommented that "old style wiring" line in ArduinoISP and that your wire connections are solid. 

Now, open the Blink example sketch. Change all instances of `LED_BUILTIN` to 0, then upload the sketch. If you have no errors, fortune smiles upon thee. Proceed to the next section. 

If you instead get an error like `avrdude: stk500_paged_write(): (a) protocol error, expect=0x14, resp=0x10`, you'll need to place a >10uF capacitor across the RESET and GND pins of the Arduino to temporarily disable the RESET button. Put it in and hit upload again, and your ATtiny should start to blink. Woohoo!

# Uploading SoftwareSerial

To test any non-visual functionality, we're going to want to print debug messages over Serial. While we can't do Serial in the ATtiny hardware, we can include the SoftwareSerial library and do it anyway. The following code is derived from an example on this [guide](<a href="https://www.instructables.com/ATtiny85-ATtiny84-Analog-Pins-Serial-Communication/">https://www.instructables.com/ATtiny85-ATtiny84-Analog-Pins-Serial-Communication/</a>), but you can use the sketch in Examples->SoftwareSerial also. 

{{ add_pic("ard2attiny/5.nP5AoiHWqoxigF7JR-8uKy3GUOAhUzhw5YYhmhRhn3iHRAX7JUF6tpxq35hOS9S8i1W8l2RzBPrUYcvcWYRvsOTIkD8-ltreZnN3sVHxAbPHu-WVWxIjoJDgnTJaUlgzSvoaICx4K9Zg492z7Y3VmeA", "") }}

## Sus method

If the ATtiny uses SoftwareSerial, you can route the TX physical pin to the Arduino's TX pin and open the Serial monitor. You should see random noise characters, but if you hold down the RESET button, you can get messages from the ATtiny to show up.

{{ add_pic("ard2attiny/6.9-sPzno3iau2898kdJs4jk5vkF-zUeJe8ft856yvqz3EhYgs6VJdxmN4lx-ImT5F_OkPRu5df4bIDqwFMvizjCiEEPxaQAeTJOR9Rjw_NA3aODJ5UzSK470X2imvPur6a5RZZsfYmmu0g9XCqP_DPOk", "") }}

Because the Arduino also uses the RX/TX pins and they're physically routed to the UART->USB converter chip, the ATtiny's messages are scrambled when we receive them over Serial. By holding down the RESET, we disable the Arduino and get to see the ATtiny messages without any problems.

## Less sus method

The proper way is to get an FTDI Friend or other UART->USB converter and receive messages using that instead. 

{{ add_pic("ard2attiny/7.DHOSOshopEyhXwWka8-zcnB7DcBOQXqJ-wwXnuJOsK2twPRctL1IBBMMHr3Af5-IluWAqPCDMZXdlgjgc9v5Fwhd35k4-92HK3z1qOFJVMrHPpT9ppF6q3kI7tsN6qj6jt6QZfXnxgmx7Uw1IkBv2sE", "") }}

If you go this route, the ATtiny's TX goes into the FTDI Friend's  RX, and the GNDs are connected. The port will have to be changed, and the messages will be received just fine. 

{{ add_pic("ard2attiny/8.JaoKb2PoWQDNCrNeNIG2MqxXwwlad3He1N-gS3kUBMB15Ixzgbh0AEE62kPHR2gtR1rlBHbJKs37aS_vAL_mvbzwQOh1Mc-JD_qlckRaeQKiP6SgPENX3JooreJpY8EC6D3BYiqkNgufwxWr74Ttr5w", "") }}

# Trying out the ADC

The ATtiny85 is big enough to fit a lot of the Arduino helper functions, so the `analogRead` function just works like normal. You will need to be careful to pick a pin which can receive analog, so be sure to check. Here's my code to read from pin 2 and print it to Serial. 

```

#include "SoftwareSerial.h"

const int LED = 0; 

const int ANTENNA = 3;

const int Rx = 2; 

const int Tx = 4;

SoftwareSerial mySerial(Rx, Tx);

int valu = 0; // variable to store antenna readings

void setup(){

    pinMode(LED, OUTPUT); // tell Arduino LED is an output

    pinMode(ANTENNA, INPUT);

    pinMode(Rx, INPUT);

    pinMode(Tx, OUTPUT);

    mySerial.begin(4800); // send serial data at 9600 bits/sec

}

void loop() {

    valu = analogRead(ANTENNA); // read the ANTENNA

    mySerial.println(valu); // send the value to Serial Monitor, ^Cmd-M

    digitalWrite(LED, HIGH); // turn LED ON

    delay(10); digitalWrite(LED, LOW); // turn off

}

```

{{ add_pic("ard2attiny/9.RHNO1qJK8evOAx1SYnD7JtN22e3eF0Xhof6TsQ2YEQeewRVd2wU8i_LnVdS9AAYYj9oOO9p2HRLxJAtrY20dcp_KKNdIoWeezZLwdlXTuPafhvnui-Az8k24R7TzvThPP50viwohR5pHNFin1ip9YNs", "") }}

# Have fun!

Hopefully you know the basics. As [DeepBlueMbedded](<a href="https://www.youtube.com/watch?v=7bZg_GzUbHI&t=1771s">https://www.youtube.com/watch?v=7bZg_GzUbHI&t=1771s</a>) said, you're basically done once you get blinking.

{{ add_pic("ard2attiny/10.i2ir1u0FLVSBclEGA7M0BbCgW-R95MRNENfQGhFLkrUyqhRwcg8d3IO4mUsJg4n6XHR_nEoHyderv4XX8gKtKXJZAUE4HUJU019oDgyTV4DMaOSn989VnR2JMBmqw8-x-dcCro270ExI7TBYuaoGyWg", "") }}
