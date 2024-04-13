title: "Optimizing Morse Code For Speed"
date: 2024-04-12
label: blog
tags: [morse, communications, human-computer bandwidth]
snippet: "Faster dits and dahs"

Hello! Recently I completed Google's [Morse Typing Trainer](https://morse.withgoogle.com/learn/) (I highly recommend it) and read a lot about the history of International Morse Code.

The inventor of Morse code mentions counting the occurrences of letters in printer's type in order to dole out the shorter codes to more commonly used letters. E and T are both single-symbol, while something like Z requires 4.

I was interested in seeing just how good Morse got his frequencies down pat, so I got a letter frequency and the Morse code chart and correlated them against each other.

{{ add_pic("omorse/0.png", "") }}

Further right is more common, further up is longer Morse character. We see some glaring gaps — O should possibly be a 2-char symbol instead of 3, maybe replacing M? But overall this follows the trend of less-common letters getting the longer end of the Morse code. 

I also wanted to know if the time length of each Morse letter also matched the letter frequency — the idea being that more common letters are easier to type if they are shorter in duration. Morse dots are 1 "unit" of time, usually around 50ms. Dashes are mandated to be 3x longer than a dot, and the gap between each symbol is also 1 dot long. Here is the same graph as above, but instead of char length I'm plotting time length. 

{{ add_pic("omorse/1.png", "") }}

{{ add_pic("omorse/2.png", "") }}

{{ add_pic("omorse/3.png", "") }}

{{ add_pic("omorse/4.png", "") }}

nd now I'm interested in using Morse code to transmit information through the skin. However, the current receiver rates of Morse code are not high enough to be worth pursuing. From my cursory searches, the top human speeds of deciphering Morse are around 50-60 words per minute. This requires a lot of attention, probably too much to allow the operator to do anything else. For comparison, typical reading speeds are ~300wpm, and English speech is ~150wpm. 

I read that after a while, Morse operators get "Instant Character Recognition" or ICR — this is necessary to pass the 5 wpm mark. After a longer while, they acquire some "instant word recognition" skills as well, allowing them to transcribe a Morse word from the beeps directly. 
