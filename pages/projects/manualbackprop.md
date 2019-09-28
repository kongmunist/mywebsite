title: Manual Backpropagation
date: 2019-09-27
label: project
timespan: March 2019
pic: backprop.png
description: Manually implementing backpropagation to prove that I know how it works

When I first completed Andrew Ng's [course](https://www.coursera.org/learn/machine-learning), I realized that the coding homeworks had babied me. The structure was already in-place, the matrix operations were trivial in MATLAB, and I didn't really have to understand how the backprop algorithm worked in order to implement it in the exercises. To prove to myself that I knew how to do it, I needed to implement it myself, with only a little help from Python and numpy.

Also, for whatever reason, implementing machine learning in PyTorch was trivial and unimpressive to a lot of people. That kind of peeved me, since tuning hyperparameters is no trivial task. Staging layers for CNNs was also not easy to figure out. 

I started by watching 3Blue1Brown's video on the backprop [algorithm](https://www.youtube.com/watch?v=Ilg3gGewQ5U&t=709s), which really helped me understand what order to do the math in. I wrote a ReLU function in Python, then either imported or created all the variables (a', z, etc.) and multiplied a bunch of matrices together. I trained on the MNIST handwritten digits dataset, and got 86% accuracy on the test set after validating on a 20% subset. 

<img class="d-block mx-auto" src="{{ url_for("static",filename="manualbackpropcode.png") }}"/>

This post is short because the code is not very neat to look at or think about. Machine learning really is just a bunch of matrices multiplying themselves. I meant to implement gradient checking to make sure I had taken the derivatives properly, but I was much too lazy. This whole project took about 8 hours, and doing the same thing in PyTorch would have taken less than 1. I just thought it was a fun, personal challenge, and now will never take PyTorch for granted again.



