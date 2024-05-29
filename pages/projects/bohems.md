title: Through-Hand Electrical Nerve Stimulation
date: 2024-05-28
label: project
timespan: Summer 2021
pic: bohems/boh_nella10boards.jpeg
description: Shocking VR research!

[<h1>Paper Link Here!</h1>](https://dl.acm.org/doi/full/10.1145/3544548.3581382)

Welcome to my writeup for some research I worked on in 2021! 

{{ add_pic("bohems/boh_hero.jpeg", "") }}

For COVID summer 2021, I worked with Prof. Pedro Lopes and the Human-Computer Integration lab at UChicago. I ran small electrical currents through my hands in order to find interesting touch sensations. We wanted to reproduce the feeling of touching real stuff using electricity so we could feel virtual objects the same way we feel real ones. 

# Background
Around 2020, I bought a TENS unit because I was curious what it felt like to have a device override control of your muscles, and discovered that it was also a fun device to bring to parties. When I showed it to my friend Cathy, she suggested I reach out to Prof. Pedro since his PhD explored electrical muscle stimulation for HCI. 

{{ add_pic("bohems/andyelectrocuting.jpg", "Administering my TENS unit on innocent partygoers") }}

My own explorations were unstructured but broad. I activated big and small muscle groups, and tried to target single muscles for more precise control. I did a few group sessions, and learned anatomy by seeing what fingers jumped for a given electrode position. But I hadz hit a cap in what could be explored with my little TENS unit since it could only do continuous pulse trains at frequencies from 2-100Hz. I definitely still had curiosities to satisfy. 

I met with Pedro a few times online and we got along pretty well, so we decided it could be viable for me to come to Chicago that summer to work on something. His lab had more electrode pads than I could ever need, and cool digitally-controlled precision muscle stimulation devices to play with

# Things that happened

- Worked closely with Yudai
{{ add_pic("bohems/boh_yudai3.jpeg", "Yudai enjoying the Chicago summer") }}

- Developed a high-voltage constant current board named after a restaurant we frequented after work
{{ add_pic("bohems/boh_nella_assembled1.jpeg", "Nella stimulator boards, assembled") }}
{{ add_pic("bohems/boh_nella10boards.jpeg", "10 Nella stimulator boards, ready for full-hand stimulation") }}


- Wrote a Processing GUI for participants to report hand sensation location
{{ add_pic("bohems/boh_gui.png", "GUI for participants, basically drawing canvas overlaid on hand image") }}


- Found electrode pad placement on the back of the hand which resulted in sensation on the front
{{ add_pic("bohems/boh_padplacement.jpeg", "Pad placement for eliciting sensations on the front of the hand") }}
{{ add_pic("bohems/boh_nella_fullhand2.jpeg", "Full-hand setup for back-of-hand stimulation. Yeowch!") }}

- Found a location + waveform which created pressure sensations without "vibrating" sensations, required per-user per-session tuning into the microamps
{{ add_pic("bohems/boh_pressure_placement.jpeg", "Very sensitive to position and strength, but somewhere near 8Hz this feels like pressure ONLY ") }}


- Tried out the [Traxion effect](../../blog/traxionreproduction/)
{{ add_pic("bohems/boh_traxion1.jpeg", "") }}
{{ add_pic("bohems/boh_traxion2.png", "") }}


- Tried out the Kajimoto high-density fingertip stimulator
{{ add_pic("bohems/boh_kaji1.jpeg", "Tingly fingers device. Taught me principles of high voltage w/ high voltage shift register") }}

# Conclusion
It was a blessing to work with such cool and interesting people during a summer where everyone else was alone. I learned so much about how the human body's sensory system works, and it still comes in handy now. 





