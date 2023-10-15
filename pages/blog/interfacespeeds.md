title: How Fast Is Your Keyboard?
date: 2021-01-21
label: blog
tags: [bci, hci, interfaces]
snippet: Calculating the human bandwidth of the keyboard, mouse, and other input devices using information transfer rate

A lot of brain-computer interface(BCI) researchers will express their results in terms of how much information the user can input in one minute, known as information transfer rate (ITR), measured in bits per minute.

I haven't yet seen a compiled list of the ITR of common household interfaces, so I thought I'd make one. This list will only cover INPUT bits/min, so I'm not going to be calculating how much text you can read off a screen or a number readout since that's OUTPUT information.

I'll list each device, explain its peculiarities and any choices I made regarding number of inputs, then give the stats. Here's a table of the results, read on for how I came to each number!

### Definition of bits for ITR
Before we start, it may seem strange to quantify the mouse or touchscreen in terms of bits, since they're almost continuous input devices. Here, "bits" refers to the log2 of the number of options available. For example, if a user in a BCI trial is trying to select one button when there are two available to pick, then they transmit one "bit" of information per correct choice they make. If choosing a button takes the user 5 seconds, then they'll be able to make 12 choices in a minute. making 12 bits per minute the ITR.


## Compiled Tables (Both available at page bottom)
<p class="caption">Table of information transfer rates of all common devices</p>
![Table of information transfer rates of all common devices]({{ url_for('static', filename = 'bpmITRCommon.png')}})

Let's get into it!

# List of Common Input Devices
<hr>

## Thermostat
<p class="caption">Picture of a thermostat</p>
![Picture of a thermostat]({{ url_for('static', filename = 'bpmthermostat.jpg')}})

I pressed 10 buttons in 6.4 seconds. 

##### # of Inputs: 5
##### Input Speed: 1.5/sec
##### Bits/min: 209

<hr>

## TV Remote
<p class="caption">Generic TV remote</p>
![Generic TV remote]({{ url_for('static', filename = 'bpmtvremote.png')}})

Since TV remotes have notoriously gummy buttons, they're a lot slower than the microwave. I pressed 10 buttons in 7.13 seconds. I used a slightly different television remote than the one pictured, which is why the # of inputs may not line up. 


##### # of Inputs: 42
##### Input Speed: 1.4/sec
##### TV Remote Bits/min: 453

<hr>

## Microwave
<p class="caption">Common Household Microwave</p>
![Household Microwave]({{ url_for('static', filename = 'bpmmicrowave.png')}})

Starting with common household electronics, the humble microwave. Though I've never used any button besides the numpad, start, and cancel, there are many more buttons which configure the microwave. I count 25 buttons, plus the trigger that opens the door. 

I can hit 10 buttons in 4.5 seconds (2.2/sec), but they were all sequential and next to each other so I'll say 2 buttons/sec. Log2(26) = 4.7, 4.7 bits/input * 2 inputs/sec * 60 sec/min = 564. Evidently, I did great in high school chemistry.


##### # of Inputs: 26
##### Input Speed: 2/sec
##### Microwave Bits/min: 564
<hr>

## Game Controller
<p class="caption">They control nuclear submarines with these!</p>
![They control nuclear submarines with these!]({{ url_for('static', filename = 'bpmgamecontroller.png')}})

We're starting to get complicated. As anyone who has played Smash knows, single button presses do very little — combinations of keys are necessary to even play. I will count single button presses, joystick positions, and a joystick position + button press. 

There are 4 bumpers, 4 positions on the left pad (D-pad), 4 buttons on the right, and four in the center. Joysticks are analog, but we're going to discretize them as 8 edge positions and the neutral position. They also have an inward click, which I'm going to count as a button. Buttons alone, there are 18 total. There are 9 joystick positions per side, and moving between any two of them gives you 9 choose 2, or 36 unique joystick movements.

Combining them gets complicated. Using the left joystick, you can't press anything on the D-pad or left-center, since your thumb covers that. You can, however, still use the bumper/trigger on the left side. So for the left joystick, you have access to 12 buttons. Doing this calculation for the right joystick, you get 13 buttons to work with. Since we already counted the neutral position + buttons in the single button presses, we have 8 joystick positions. For the left and right joystick respectively, that gives us 96 and 104 combination presses. 

I don't have a controller like this, but my friend who is a pro Smash player does. 
10 joystick moves in 2.25 seconds, averaged over 16 trials (left-right flicking, neutral to edge and back). 1.84 sec for 10 face buttons, 2.35 sec for 10 trigger buttons. Since the center buttons are harder to press, and not everyone is a competitive Smash player, I'm going to use the slower time for the button inputs. I'll use the joystick speed for the combo speed, since it'll be the limiting factor. 

<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax">Buttons</th>
    <th class="tg-0lax">Joystick</th>
    <th class="tg-0lax">Buttons+Joystick</th>
    <th class="tg-0lax">Totals</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky"># of Inputs</td>
    <td class="tg-0pky">18</td>
    <td class="tg-0lax">36</td>
    <td class="tg-0lax">200</td>
    <td class="tg-0pky">254</td>
  </tr>
  <tr>
    <td class="tg-0pky">Input Speed</td>
    <td class="tg-0pky">4.255</td>
    <td class="tg-0lax">4.444</td>
    <td class="tg-0lax">4.444</td>
    <td class="tg-0pky">Average: 4.38</td>
  </tr>
  <tr>
    <td class="tg-0pky">Bits/min</td>
    <td class="tg-0pky">1065</td>
    <td class="tg-0lax">1379</td>
    <td class="tg-0lax">2038</td>
    <td class="tg-0pky">4,482</td>
  </tr>
</tbody>
</table>

<br>
##### Game Controller Total Bits/min: 4,482

<hr>

## Touchscreen

<p class="caption">The Apple iPhone 11, most sold phone in 2019.</p>
![The Apple iPhone 11, most sold phone in 2019.]({{ url_for('static', filename = 'bpmiphone11.jpg')}})

I'm using an Apple iPhone 11 as my reference phone since it's the most sold smartphone of 2019, according to Wikipedia. There are a lot of possible input gestures on the phone, and the touchscreen enables them to be fast. I'll count each input separately to make the count more accurate. However, I'm not counting pinches, so this will be a bit of an underestimate. 

<p class="caption">Icons from the navigation bar on Instagram. Green box is 100 by 75 pixels. Note how it's rectangular in the x-axis. It's much easier to press very wide, short buttons than very tall, skinny buttons on a smartphone, which I didn't realize before.</p>
![Icons from the navigation bar on Instagram. Green box is 100 by 75 pixels. Note how it's rectangular in the x-axis. It's much easier to press very wide, short buttons than very tall, skinny buttons on a smartphone, which I didn't realize before.]({{ url_for('static', filename = 'bpmphoneminsize10075.png')}})

For smallest input size with the finger, I used the sizes of the icon set from Instagram since they're quite reliable (I don't remember ever misclicking one). These also match the icon sizes in the footer of the iPhone clock app. The green square shown is 100x75 pixels. This divides into the iPhone 11 screen resolution of 1792x828, giving us around 198 non-overlapping rectangles. 

There are also 4 buttons around the phone, two of which can be pressed at once to trigger a different event (screenshot, shutdown, etc.). 4 choose 2 is 6, so that adds 10 inputs for a total of 208.

I pressed on the screen 10 times in 4 seconds. It's not noticeably faster using two fingers. I held down 20 icons on my home screen in 27.55 seconds and dragged 20 times around the screen in 17.8 seconds. Each drag is from one square to any other square, making it 330x329. That's a lot of inputs, but the log2 takes it down. And there are 4 swipes, which can be done in the center or from the edge of the screen. I did 20 swipes in 15.5 seconds. 

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;margin-left: auto; margin-right: auto;}
.tg td{border-color:white;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:white;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax">Taps/clicks</th>
    <th class="tg-0lax">Hold down</th>
    <th class="tg-0lax">Drags</th>
    <th class="tg-0lax">Swipes</th>
    <th class="tg-0lax">Totals</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"># of Inputs</td>
    <td class="tg-0lax">208</td>
    <td class="tg-0lax">198</td>
    <td class="tg-0lax">39,006</td>
    <td class="tg-0lax">8</td>
    <td class="tg-0lax">39,420</td>
  </tr>
  <tr>
    <td class="tg-0lax">Input Speed</td>
    <td class="tg-0lax">2.5</td>
    <td class="tg-0lax">0.725</td>
    <td class="tg-0lax">1.12</td>
    <td class="tg-0lax">1.29</td>
    <td class="tg-0lax">Average: 1.41</td>
  </tr>
  <tr>
    <td class="tg-0lax">Bits/min</td>
    <td class="tg-0lax">1155</td>
    <td class="tg-0lax">332</td>
    <td class="tg-0lax">1025</td>
    <td class="tg-0lax">232</td>
    <td class="tg-0lax">2,744</td>
  </tr>
</tbody>
</table>

<br>
##### Touchscreen Total Bits/min: 2,744
<hr>

## Touchscreen (Stylus)
Though not many smartphones these days have a stylus anymore, it does allow much more pinpoint clicks while allowing the same speed and gestures that using a finger does. I'm going to use the same speeds for taps, holds, drags, but will not count swipes or pinches since they are only possible with fingers.

I'll use the screen resolution we used earlier for the iPhone 11 (1792x828), and a smaller 60x60 box for the minimum pointing size. This gives us 412 potential sites for input. I'll include the volume/power/home buttons only in the taps again. 

<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax">Taps/clicks</th>
    <th class="tg-0lax">Hold down</th>
    <th class="tg-0lax">Drags</th>
    <th class="tg-0lax">Totals</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"># of Inputs</td>
    <td class="tg-0lax">422</td>
    <td class="tg-0lax">412</td>
    <td class="tg-0lax">169,332</td>
    <td class="tg-0lax">170,166</td>
  </tr>
  <tr>
    <td class="tg-0lax">Input Speed</td>
    <td class="tg-0lax">2.5</td>
    <td class="tg-0lax">0.725</td>
    <td class="tg-0lax">1.12</td>
    <td class="tg-0lax">Average: 1.45</td>
  </tr>
  <tr>
    <td class="tg-0lax">Bits/min</td>
    <td class="tg-0lax">1308</td>
    <td class="tg-0lax">377</td>
    <td class="tg-0lax">1167</td>
    <td class="tg-0lax">2,852</td>
  </tr>
</tbody>
</table>

<br>
##### Touchscreen Stylus Total Bits/min: 2,852

<hr>

## Touchscreen (Keyboard)

<p class="caption">Picture of the iPhone keyboard, with diction key highlighted. I didn't want to find another picture so I reused this one</p>
![Picture of the iPhone keyboard, with diction key highlighted. I didn't want to find another picture so I reused this one]({{ url_for('static', filename = 'bpmdiction.jpg')}})


I'm using my iPhone 6s keyboard for this one. I'll count each page of keys separately, since they're harder to get to. I'm doing phone keyboard separately because A) we have a lot of muscle memory for it, which lets us input keys a lot faster than a usual interface, and B) to double check my numbers, the final bits/min of this should be bounded by the total bits/min of the touschreen.

There are 29 typing keys on the primary keyboard, plus 26 for capital letters for a total of 55 keys. I type at 45 WPM on the phone, which is 225 characters/min. Including the space after ever word, that's actually 270 characters/min, or 4.5/sec.

On the second page, there are 25 keys (I'm not recounting the delete, return, or spacebar), which can be pressed to your heart's desire, except when the spacebar happens. Since the spacebar is essential to typing, I'm going to count my typing speed with a spacebar after every character, giving us 18 keys in 20.29 seconds. I'll also count the space after each key, so 36 keys.

I'll do the same for the third page, which also has 20 keys (5 are shared with page 2). I typed 19 in 20.93 seconds. Here I'll also count the space after each key, so 38 keys.

<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax">First page</th>
    <th class="tg-0lax">Second page</th>
    <th class="tg-0lax">Third page</th>
    <th class="tg-0lax">Totals</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky"># of Inputs</td>
    <td class="tg-0pky">55</td>
    <td class="tg-0lax">25</td>
    <td class="tg-0lax">20</td>
    <td class="tg-0pky">100</td>
  </tr>
  <tr>
    <td class="tg-0pky">Input Speed</td>
    <td class="tg-0pky">4.5</td>
    <td class="tg-0lax">1.77</td>
    <td class="tg-0lax">1.816</td>
    <td class="tg-0pky">Average: 2.7</td>
  </tr>
  <tr>
    <td class="tg-0pky">Bits/min</td>
    <td class="tg-0pky">1,560</td>
    <td class="tg-0lax">460</td>
    <td class="tg-0lax">471</td>
    <td class="tg-0pky">2,491</td>
  </tr>
</tbody>
</table>

<br>
##### Touchscreen Keyboard Total Bits/min: 2,491

<hr>

## Mouse/trackpad + Screen
<p class="caption">Macbook Air</p>
![Macbook Air]({{ url_for('static', filename = 'bpmmacbookair.png')}})

I'll be using my Macbook Air screen and touchpad as the reference for this one. With a screen resolution of 1440x900, it's worse than the smartphones we just saw, but I think the finger has a broader input area than the mouse pointer. For inputs, I'm counting clicks, double clicks, right clicks, drags, and swipes (scrolling included). 

For smallest reliable click size, I'm using the geometric mean of the icons from Google Chrome and the icons on the MacOS desktop. The green square shown is 30x30 and the desktop icons on MacOS are a slightly larger 70x70, for a combined 45x45. I spend more than half my time on Chrome, and the file icons in Finder are the same size as their icons, but dragging that small an icon is difficult. 

<p class="caption">Smaller of the "smallest reliable click size" bounding boxes. This is from the Chrome toolbar, and has size 30x30 pixels.</p>
![Smaller of the "smallest reliable click size" bounding boxes. This is from the Chrome toolbar, and has size 30x30 pixels.]({{ url_for('static', filename = 'bpmmouseminsize3030.png')}})

This divides into the screen to give us 640 clickable squares, which I use for single click, double click, and right click. Drag is from any square to another, so 640x639 = 408,960. There's 2 finger swipes and three finger swipes (from any side or center of the touchpad), and a pinch for a total of 19 potential swipes.


<p class="caption">Picture of the first mouse</p>
![Picture of the first mouse]({{ url_for('static', filename = 'bpmfirstmouse.jpg')}})

I clicked 20 times in 18.20 seconds, double clicked 20 times in 19 seconds, right clicked 18 times in 18.24 seconds, dragged 20 times in 26.15 seconds, and swiped 20 times in 20 seconds. 

<table class="tg" style="margin-left: auto; margin-right: auto;">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Taps/clicks</th>
    <th class="tg-0lax">Double clicks</th>
    <th class="tg-0lax">Right clicks</th>
    <th class="tg-0pky">Drags</th>
    <th class="tg-0lax">Swipes</th>
    <th class="tg-0pky">Totals</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky"># of Inputs</td>
    <td class="tg-0pky">640</td>
    <td class="tg-0lax">640</td>
    <td class="tg-0lax">640</td>
    <td class="tg-0pky">408,960</td>
    <td class="tg-0lax">19</td>
    <td class="tg-0pky">410,899</td>
  </tr>
  <tr>
    <td class="tg-0pky">Input Speed</td>
    <td class="tg-0pky">1.099</td>
    <td class="tg-0lax">1.05</td>
    <td class="tg-0lax">0.986</td>
    <td class="tg-0pky">0.764</td>
    <td class="tg-0lax">1.0</td>
    <td class="tg-0pky">Average: 0.98</td>
  </tr>
  <tr>
    <td class="tg-0pky">Bits/min</td>
    <td class="tg-0pky">615</td>
    <td class="tg-0lax">587</td>
    <td class="tg-0lax">552</td>
    <td class="tg-0pky">855</td>
    <td class="tg-0lax">255</td>
    <td class="tg-0pky">2,864</td>
  </tr>
</tbody>
</table>
<br>
##### Mouse+Screen Total Bits/min: 2,864

<hr>

## Keyboard
<p class="caption">Physical keyboard, reduced because it doesn't have the numpad on the right.</p>
![Physical keyboard, reduced because it doesn't have the numpad on the right.]({{ url_for('static', filename = 'bpmkeyboard.jpg')}})

I'll be using my Macbook Air keyboard, which is quite similar to the one shown above. I'm counting single keypresses for typing and not typing separately, and also combination keypresses (Control, Alt/Option, Command, Function, or Shift + any other keys).

Believe it or not, there are 78 keys on the keyboard! I expected way less. I can type at 80 WPM on a good day, which is 400 keys/min assuming an average word length of 5 characters a word. I'm going to count each key that actually types a symbol in a normal text editor, which is 49 keys. Since holding shift doubles each key, this makes 98 inputs at 400 keys/min. Including the spacebar after every word, that's 480 keys/min, or 8/sec.

That leaves 14 function keys, which I can press 20 times in 5 seconds. 

There are 7 combination keys (separating the left and right Command and Alt/Option) which can be pressed down in any combination with any typing or nontyping key. There are 69 of those keys. It's unrealistic to expect to be able to press any combination of the keys though (Imagine holding down all 7!), so we'll cap it at 3 combo keys at most. We also have to subtract out Shift + the 49 typing keys, since we already counted those in the typing test.

For 1 combo key, we have 7 options. For 2, we have 21. For 3, we have 35 options. In total, that gives us 63x69=4347 options for input. I can press 20 combinations in 14 seconds. 

<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax">Single (typing)</th>
    <th class="tg-0lax">Single (other)</th>
    <th class="tg-0lax">Combo</th>
    <th class="tg-0lax">Totals</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky"># of Inputs</td>
    <td class="tg-0pky">98</td>
    <td class="tg-0lax">14</td>
    <td class="tg-0lax">4,347</td>
    <td class="tg-0pky">4,459</td>
  </tr>
  <tr>
    <td class="tg-0pky">Input Speed</td>
    <td class="tg-0pky">8</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">1.429</td>
    <td class="tg-0pky">Average: 4.48</td>
  </tr>
  <tr>
    <td class="tg-0pky">Bits/min</td>
    <td class="tg-0pky">3175</td>
    <td class="tg-0lax">914</td>
    <td class="tg-0lax">1036</td>
    <td class="tg-0pky">5,125</td>
  </tr>
</tbody>
</table>
<br>
##### Physical Keyboard Total Bits/min: 5,125

<hr>


<p class="caption">Table of information transfer rates of all research devices</p>
![Table of information transfer rates of all research devices]({{ url_for('static', filename = 'bpmITRResearch.png')}})


# List of Experimental Input Devices
These are research devices that are still working out the kinks, and don't work incredibly reliably yet. I'm including voice control because it's a biometric device instead of a button input like the earlier ones, and doesn't work for everyone's voice yet.


<hr>

## Voice Control (Diction)
<p class="caption">Voice control or diction button on an iPhone keyboard</p>
![Voice control or diction button on an iPhone keyboard]({{ url_for('static', filename = 'bpmdiction.jpg')}})

I used Google's voice to text function to dictate the sentence "Google's free service instantly translates words, phrases, and web pages between English and over 100 other languages." At 114 characters (118 with punctuation) in 7.37 seconds, this yields a whopping 165 WPM, or 957 characters/min. Apple's diction feature took the same amount of time, which was how long it took me to read the sentence.

Since voice diction cannot detect punctuation or capital letters (except at the beginning of sentences), this is out of the 10 numbers, 26 letters, and spacebar. That leaves us with 37 unique input keys. 


##### # of Inputs: 37
##### Input Speed: 15.47 characters/sec
##### Bits/min: 4,835

<hr>

## Fingerprint/Face recognition
This is probably a special class of "input", but I thought it'd be cool to include. 

### Fingerprints
[NIST](https://www.nist.gov/news-events/news/2004/07/nist-study-shows-computerized-fingerprint-matching-highly-accurate) says fingerprint scanners only give false positives 0.01% of the time. Assuming this is consistent, the fingerprint scanner reliably can differentiate you and 700,000 others from everyone else on earth, which is 10,000 other groups of 700,000 people. I'll say that's 10,000 inputs. My phone takes around 1 second to scan, but sometimes fails, so I'll say it operates at 1.5/sec

##### # of Inputs: 10,000
##### Input Speed: 1.5/sec
##### Fingerprint Scanner Bits/min: 1196

### Face
Also from NIST, the best face recognition has a false positive rate of 0.08%, which is much higher than the fingerprint scanner. You'll be reliably recognized along with 5,600,000 others by the best face recognition, which is 1/1250 groups. It is much faster than a fingerprint scanner though, at least on the iPhone.

##### # of Inputs: 1250
##### Input Speed: 1/sec
##### Face Recognition Bits/min: 617

<hr>


## Eye tracking

<p class="caption">Screenshot of someone using a Tobii Eye Tracker. The big blob is the predicted gaze location, which takes up about 10% of the screen</p>
![Screenshot of someone using a Tobii Eye Tracker. The big blob is the predicted gaze location, which takes up about 10% of the screen]({{ url_for('static', filename = 'bpmtobii.png')}})

Eye tracking uses your gaze location as input, usually to steer your cursor, but also for indicating attention. Tobii is one of the largest eye-tracking companies, selling hardware that just plugs into your computer and reports your gaze. However, it has a large inaccuracy which isn't mentioned on the website, and refuses to even mention accuracy specs for any of their products. 

If you watch anybody using it on YouTube like [here](https://www.youtube.com/watch?v=uM0QtujhjcA), you'll see the large spot size which indicates its approximate confidence zone. The frame was originally 850x475 pixels, and the size of the green square is 75x60 for an error margin of about 15% (geometric mean of x and y error). 

If this is the minimum spot size, we can do a similar calculation to the touchscreen section and find that there are around 90 differentiable squares on the screen. However, this doesn't include clicking, and the number of flicks an eye can do in a second. If I use my touchpad click, then I can look and click at 10 locations in 9.34 seconds. If I use a blink (which some eye trackers do use), then I can do 10 blinks in 6.68 seconds. 

The newest Tobii tracker polls at around 33Hz, but has a lot of smoothing going on. I'm going to say it updates the spot at 10Hz, because I don't notice it lagging at all whenever the eye flicks from one spot to another.


##### # of Inputs: 90
##### Input Speed: 1.07 clicks/sec, 1.5 blinks/sec
##### Eye Tracker Bits/min: 417 clicking, 584 blinking

<hr>

## Brain-computer interfaces (EEG)

There's a few different ways to detect what someone's thinking of. I'll go over both the P300 and SSVEP.

### P300
The [P300](https://en.wikipedia.org/wiki/P300_(neuroscience)) is a signal that arises when your expectation of what you're seeing is different from what you expect it to be. These BCIs work by flashing a grid of objects (letters, labeled buttons) and removing one object each time. If you ever don't see the one you're trying to select, then your brain emits a P300. It needs a lot of averaging across many trials to be done reliably though, and it's a very unintuitive way to select things. 

From this [review paper from 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5924393/), the average bits/min of P300 BCIs is around 30. The [best one](https://pubmed.ncbi.nlm.nih.gov/25080406/) incorporated your brain's reaction to a familiar face to help you select a target more robustly, and hit 80 bits/min with an accuracy of 81.25%. 


<p class="caption">A flowchart of SSVEP brain signal processing</p>
![A flowchart of SSVEP brain signal processing]({{ url_for('static', filename = 'bpmssvep.jpg')}})


### SSVEP
The [SSVEP](https://en.wikipedia.org/wiki/Steady_state_visually_evoked_potential) is a signal that is also evoked by visual stimulus, but in this case it's caused by repeated flashes of light. It can be reliably detected for flickering between 10 and 20Hz. To use the SSVEP as input, you create an LED display or use a monitor with many buttons on it which are each flashing at a different frequency. Then, you look at the buttons for a short window of time. The frequency spectrum of the recorded EEG signal will have a peak at the frequency of the button you were focusing on, and the computer will know which one you want to select.

The tradeoff here is a longer window raises accuracy but lowers the bits/min transferred, with a minimum of about 3s of data needed to detect it reliably. The best SSVEP ITR I found is from [this paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5783827/), where they reached a mean of 325 bits/min. I believe this is the offline ITR though, so when they actually measured people using it live they got an ITR of 199 bits/min.

##### # of Inputs: Variable
##### Input Speed: 2/sec (max)
##### BCI Bits/min: 199

<hr>

# Discussion
The computer (trackpad + screen + keyboard) has undoubtedly the highest input rate of any device, clocking in at 7,989 bits/min. It seems that bits/min comes more from an interface which registers button presses quickly than one that offers many simultaneously available options. 

The game controller did better than I expected, beating out the smartphone handily, but that's just on input speed. The game controller offers much less analog control than the touchscreen, and has fewer available applications. You also must remember that the game controller does not have a high-density screen built-in, and must rely on there being one available.

BCIs really need some work, seeing as their best technique clocks in under a thermostat. 

# Both Tables

<p class="caption">Table of information transfer rates of all common devices</p>
![Table of information transfer rates of all common devices]({{ url_for('static', filename = 'bpmITRCommon.png')}})

<p class="caption">Table of information transfer rates of all research devices</p>
![Table of information transfer rates of all research devices]({{ url_for('static', filename = 'bpmITRResearch.png')}})
