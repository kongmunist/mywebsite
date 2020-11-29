title: Javascript Libraries
date: 2020-11-28
label: blog
tags: [webdev, javascript]
snippet: What do you mean everything is a global???

I am writing a rather complex Javascript project at the moment, and needed to include two different Javascript libraries. One is [p5.js](https://p5js.org/), which is just Processing ported to HTML and used for drawing and a lot of visual display stuff. The other is [mlweb](https://mlweb.loria.fr/), which is a machine learning library written in pure Javascript. 

<u>__One of the cursed things about using Javascript is that most libraries are written exclusively as a global import__</u>, so importing two large libraries is a nightmare if any of their functions overlap. While the ES6 standard (2015 major update to Javascript) recommends libraries encapsulate their functions into their own namespace, older ones or lazy ones still don't do it.

This is annoying in Javascript, but isn't a problem at all in Python. Importing a library by default forces you to use their import name before any function or variable from that library (think `cv2.imread()` from `import cv2`, or `os.walk` from `import os`). 

In my case, `sin` and `tan` and a few other math functions overlapped. Though both functions do the same thing, the problem arises because of the format that they each return. If the p5.js function returns their own P5 class of int or Array, then the mlweb function calling it wouldn't be able to parse its output and crash. 

### Maybe there's already a fix for it?
I couldn't find anything after an hour of looking, so I made a [post about it on SO](https://stackoverflow.com/questions/64730996/how-can-i-include-a-javascript-library-with-a-namespace-without-manually-exporti). It was my first post, and was answered in 4 minutes in the negatory. Turns out there's no way to import Javascript like this: 

`<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>`

And have it callable by module namespace. Wack!

### Is there anything we can do?
For small libraries, it's doable. You can wrap your entire library.js file in a module declaration and then export each function you want to be able to use [(source)](https://www.typescriptlang.org/docs/handbook/namespaces-and-modules.html):

`declare module "SomeModule" {`<br>
&emsp;`	 export function fn(): string;`<br>
`}`


But this doesn't work for large libraries, since there are so many variables and functions and all kinds of stuff, and as far as I know there's no automatic tool for it. However, I think you could write something simple that would just parse a javascript file and export everything for you. 

Now that I think about it, I did something like this for my [Webcam Heartrate](https://andykong.org/projects/heartratemonitor/) project. I ported a C++ package to Node.js using Emscripten, then used Browserify to port that to a script that I could just include. Then to call it, I added some lines around the library to expose it as a variable, and had to reference that variable to call its functions. May be useful for me to go back through and see if I can't throw together a quick solution...

### Final fix
In the end, it turns out p5.js DOES conform to ES6, and can be wrapped in a big function wherever you call its functions and variables to not leak into the global namespace. With this solution, I stopped looking further into it. You can also invoke p5.js whenever you want in your javascript, if the problem is just the order in which the functions overlap (lazier, but easier).

A Javascript encapsulator script would be really useful if Javascript continues being the norm for web stuff and people push more and more code into Javascript. It doesn't seem super hard, but for now there's not much of a fix and I'm busy. Summer project, anyone?
