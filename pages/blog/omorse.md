title: "Is Morse Code Letter-Frequency Optimal?"
date: 2024-04-12
label: blog
tags: [morse, communications, human-computer bandwidth]
snippet: "Most common letters vs. Morse code length"

Hello! Recently I completed Google's [Morse Typing Trainer](https://morse.withgoogle.com/learn/) (I highly recommend it) and read a lot about the history of International Morse Code.

The inventor of Morse code mentions counting the occurrences of letters in printer's type in order to dole out the shorter codes to more commonly used letters. For example, E and T are both single-symbol, while something like Z requires 4 symbols.

I was interested in seeing just how good Morse got his letter frequencies, so I got a letter frequency table and the Morse code chart and correlated them against each other.

# Morse Code Char-Length vs. Letter Frequency

{{ add_pic("omorse/0.png", "") }}

Further right is more common, further up is longer Morse sequences. We see some glaring gaps — O should possibly be a 2-char symbol instead of 3, maybe replacing M? But overall this follows the trend of less-common letters getting the longer end of the Morse code. 

<hr>
# Morse Code Time-Length vs. Letter Frequency
Then I also wanted to know if the time length of each Morse letter also matched the letter frequency — the idea being that more common letters should be shorter in duration to make them easier to type. Morse is defined around the duration of a single dot — inter-symbol gaps are a dot long, and a dash is 3 dots long.

{{ add_pic("omorse/1.png", "") }}

Here is the same graph as above, but instead of Morse symbol length I'm plotting time length for each letter. The gaps here are even more extreme. "O" is typed out as "___", taking 11 dots of time despite being the 4th most common letter. "I" (..) appears less often than "A" (._), but is shorter to type. 

It's obvious that Morse code is clearly un-optimized for typing speed, which suggests that transmit speed wasn't actually that important in practical use. It is kinda frustrating that they didn't add such a simple improvement even though it would have helped a decent amount (10-20% I'm estimating).

<hr>
# Morse Transmit Speed Optimization
While I know Morse was developed for terrible communication channels and could only transmit one tone, I couldn't help but think about the potential improvements especially in regards with multi-tone. If two tone were possible, a dash could be converted from a long symbol into a short dot in the other frequency.

This graph compares the transmit time-lengths for each letter if dashes were 3 or 1 dots long. Y-axis is frozen for easier comparing. By adding one tone we can decrease time for any letter with a dash.
{{ add_pic("omorse/3.png", "") }}

Here's a harder-to-read improvements chart
{{ add_pic("omorse/2.png", "") }}


Finally, the approximate speedup offered by switching dashes to dots, and then further even removing the spaces between letters.
{{ add_pic("omorse/4.png", "") }}
{{ add_pic("omorse/morsespeedup.png", "") }}

So the total improvement isn't nuts, around 50% in optimal cases with dashes being 1 dot long. This doesn't even account for possible improvements when properly staggering the Morse length vs. letter frequency. 

<hr>
# Who cares, why are you learning outdated radio speak?
I'm currently pretty interested in transmitting information through the skin, and I think Morse code would be a neat way to do it. I want to use vibration motors for producing this haptic info, and they can't render speech directly but can usually make a single buzz as required by Morse code. However, the vibromotors usually can also produce a couple of discernible vibrations which can make up our 2-tone Morse code. 

I realized after making all these graphs that optimizing transmit times doesn't necessarily make it any easier to receive Morse signals faster. However, my hope is that the brain's short-short-term cache would have more retention to hear the receiver signal if the letters are transmitted faster.

That's all for now, cya!