title: Digital Holograms
date: 2020-06-18
label: blog
tags: [projectlog]
snippet: Displaying 3D images on a 2D computer screen

I was reading about holograms and realized that I could emulate it on a computer. Basically, screen objects don't shift perspective like real objects do (showing a different side when you look from the left vs. right, etc.) 

<img class="d-block mx-auto" src={{ url_for("static", filename = 'digitalholocube.png') }} width="400" />
<p class="caption">[image credit](https://light2015blogdotorg.wordpress.com/2015/11/05/holography-art-with-light/)</p>

However, with head tracking, the computer can compute what new angle your eyes are looking from and recalculate the image view. This can be used for looking at CAD models, or on websites for a more 3D experience, or for hiding information on the sides of a usually unviewable object (like a scavenger hunt or something), or creating a head whose eyes literally follow you around. 

I made a little demo of this, and I'm going to do some more work with eye tracking in-browser soon. I know this concept has been done before, just not with a computer's built-in webcam.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Hologram displayed on flat computer screen <a href="https://t.co/efOuGUr61W">pic.twitter.com/efOuGUr61W</a></p>&mdash; Andy (@redlightguru) <a href="https://twitter.com/redlightguru/status/1271007318927241216?ref_src=twsrc%5Etfw">June 11, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
