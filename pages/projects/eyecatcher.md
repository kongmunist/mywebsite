title: EyeCatcher
date: 2020-12-16
label: project
timespan: December 2020
pic: eyecatchercrop4.gif
description: A perspective into another world, made possible through real-time head tracking

A friend and I decided it'd be fun to do a real-time video art project that we could display on the lab's huge TV. The end result is a reactive screen showing a triple-torus floating in the aether, which turns as your head turns, and moves as your head moves. 

[Demo here!](https://karan-ahuja.com/fun_projects/eyecatcher/) [[Mirror]](https://eyecatcher.netlify.app/)

<img class="d-block mx-auto" src="{{ url_for('static',filename='eyecatchergif.gif') }}"/>


### Technical Implementation
It was pretty simple given the advanced state of Javascript. 3D graphics are simple with GL and Three.js, head tracking done with machine learning is made easy through Tensorflow.JS. 

We used Mediapipe's facemesh to get the head angles and position of a person walking by, then combined it with a great Three.js 3D demo by [David Lenaerts](https://twitter.com/DerSchmale) to make the torus turn according to your head geometry. 

I had done this before in Python [Summer 2020] but I like it much more in the web. It's so portable!