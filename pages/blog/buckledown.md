title: "Buckle Down And Get It Done"
date: 2024-11-17
label: blog
tags: [thoughts, wip]
snippet: "How to finish something hard"


I've had the privilege of working on a few hard projects in my lifetime. In each case I can mention one subtask which was extremely annoying to do, yet necessary in the overall scope of the project. I hope this won't always be the case, but generally viewing the project as a few month endeavor made the bitter pill easier to swallow — oftentimes the thing that sucks must be done by hand. It will not respect your intellect or wit, or your exceptional ability to recognize patterns, but just your ability to do the same thing over and over again. I think a lot of scientific work hinges on this dirty, stupid, manual, yet essential task. 

If it were easy to automate, someone else would've tried it already to great success. If it were not ass to test, you wouldn't have to run it. Even better if it's multiple things that must be done manually together. .


Usually it's something on the edge of being automatable. each component is kinda possible to rig to a computer, but it'd take nearly just as long to do it by hand as by computer ,and possibly it wouldn't even work so consistently and it would still need to be managed by hand. This is the frontier of .

1. Early 2024 I published a paper about [power transmission over skin](../../projects/pos), which was largely based on work done by [Li et al](https://www.nature.com/articles/s41928-021-00592-y). This paper's core contribution is a resonant circuit which is not explained very well, and without a provided schematic I had a lot of trouble replicating it. Essentially, the receiver circuit needs a resonant LC shunt, and picking the values for L and C required a careful RF simulation of the input. I didn't know how to do this, and waffled on the task for four days because testing new values involved desoldering the old component, soldering the new one, and then manually measuring power transmission by shooting a video of a blinking LED and counting frames to measure its blink rate. One night I just decided to try every inductor I had in the box — binary searching my way through a Coilcraft inductor kit. It took 3 hours of braindead testing and I found one that worked best, then used that to back-calculate the circuit's input capacitance, which gave me a real-world data point which I could use to check my RF simulation was accurate.

2. 

