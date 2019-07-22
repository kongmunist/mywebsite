title: Eye-Tracking Mouse
date: 2019-07-06
label: project
timespan: May-June 2019
pic: eyetrackthumbnail.png
description: An easy-to-use, handless mouse utilizing a laptop's built-in webcam and some CNNs.

<div style="text-align:center;" class="d-block mx-auto"><iframe style="max-width: 50vw;" width="560" height="315" src="https://www.youtube.com/embed/iV9ZkvdsL7I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

The mouse sucks. It only exists for changing screens and navigation; all real work done on a computer requires the keyboard. It is time to throw away the mouse as the main means of navigating around computers.

I first stumbled across the eye-tracking mouse back in May on an online shop, and was astounded that I had never heard of it before. This invention had the ability to change the way we browse the internet, allowing us to move around as quickly as we can see. The only problem was its price. 

However, being an enterprising CS student, I realized that I could make the same thing for free. Once you know enough, most products can be replaced by custom-designed solutions made by yourself. My first prototype involved an accelerometer and ultrasonic sensor taped to some glasses and wired to an Arduino. Sadly, I realized that cheap accelerometers weren't precise enough to give consistent measurements, and neither was one ultrasound sensor. 
<img class="d-block mx-auto" src="{{ url_for("static",filename="badglasses.png") }}"/>

My next attempt involved machine learning. Thanks to Andrew Ng, I now knew enough to implement a CNN. Using a library called face_exploration, I harvested a few thousand images of my left eye to train a model. The images were all scaled to 50x100, grayscaled, and fed into a Neural Net. The structure was 

Conv->ReLU->BatchNorm->MaxPool->FC->FC->FC

The final layer was a single real number that showed percentage of screen travelled. Multiplied by the width or height, it gave the pixel location I was looking at. 

I decided to make two separate models for x and y coordinates. I trained an abundance of models all hitting around 60-90 pixel accuracy, which is around 6-10% error compared to my screen width and height. I was hoping to create an ensemble capable of much better, but it only improved to 51 pixel error for the x classifier and 60 pixel error for the y classifier. 

<img class="d-block mx-auto" src="{{ url_for('static',filename='eyedrawnname.png') }}" />

The models performed worse in real-world conditions. The lighting was different, the angle I looked at my screen with was different, and my squintiness would change depending on how I felt. I'm sure the model was very confused. In the end, I added a 25 timestep moving average to calm down the predicted eye placements. No more jitter! Then with my newly tamed eye-tracking models, I drew my name and a star. 

<img class="d-block mx-auto" src="{{ url_for('static',filename='stareye.png')}}" />
