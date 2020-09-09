title: Privacy screen
date: 2020-09-09
label: blog
tags: [facerecognition, miniprojectlog]
snippet: Only cool kids can see this laptop!


Howdy! I saw a meme when I was in high school that was a picture of a man. Superimposed onto his bottom text was the phrase "This meme is a red square when you're not looking," the joke being that you wouldn't be able to see it if you weren't looking. Anyway, since then I've had this desire to really implement it, to make some kind of billboard/house sign that nonresidents wouldn't be able to see, perhaps to display the weekly dinner schedule or WiFi password.

Using a Raspberry Pi, raspicam, and downloading dlib's face recognition models, we were able to get it to run at <b>0.5 FPS</b>. When someone it recognized from the "VIP Faces" folder was in view of the camera, it would turn the screen back on. Otherwise, the Raspberry Pi would black out the screen using some display power management functions invoked from the command. 

This FPS is a little useless since it can't black out the screen fast enough, so I ported it over to my Mac. Here, it runs at \~10 FPS, so it can feasibly block out someone trying to view your screen. Another benefit is it blacks out the screen while you aren't looking at it (since it can't see your face), saving power (Assuming the display turn off and turn on don't cost any extra energy, which they probably do). Anyway, it only took a few hours to write, so here's all the code: 

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><table><tr><td><pre style="margin: 0; line-height: 125%"> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62</pre></td><td><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">import</span> <span style="color: #0e84b5; font-weight: bold">face_recognition</span>
<span style="color: #008800; font-weight: bold">import</span> <span style="color: #0e84b5; font-weight: bold">cv2</span>
<span style="color: #008800; font-weight: bold">import</span> <span style="color: #0e84b5; font-weight: bold">subprocess</span> <span style="color: #008800; font-weight: bold">as</span> <span style="color: #0e84b5; font-weight: bold">sp</span>
<span style="color: #008800; font-weight: bold">import</span> <span style="color: #0e84b5; font-weight: bold">os</span>
<span style="color: #008800; font-weight: bold">import</span> <span style="color: #0e84b5; font-weight: bold">glob</span>
<span style="color: #008800; font-weight: bold">import</span> <span style="color: #0e84b5; font-weight: bold">numpy</span> <span style="color: #008800; font-weight: bold">as</span> <span style="color: #0e84b5; font-weight: bold">np</span>
<span style="color: #008800; font-weight: bold">from</span> <span style="color: #0e84b5; font-weight: bold">functools</span> <span style="color: #008800; font-weight: bold">import</span> <span style="color: #007020">reduce</span>

<span style="color: #888888"># Start webcam stream</span>
video_capture <span style="color: #333333">=</span> cv2<span style="color: #333333">.</span>VideoCapture(<span style="color: #0000DD; font-weight: bold">0</span>)

<span style="color: #888888"># Load approved users</span>
known_face_encodings <span style="color: #333333">=</span> <span style="color: #007020">dict</span>()

rootdir <span style="color: #333333">=</span> os<span style="color: #333333">.</span>path<span style="color: #333333">.</span>dirname(__file__) <span style="color: #333333">+</span> <span style="background-color: #fff0f0">&quot;/faces/&quot;</span>
<span style="color: #008800; font-weight: bold">for</span> fl <span style="color: #000000; font-weight: bold">in</span> os<span style="color: #333333">.</span>listdir(rootdir) :
    <span style="color: #008800; font-weight: bold">if</span> fl<span style="color: #333333">.</span>endswith(<span style="background-color: #fff0f0">&quot;.jpg&quot;</span>) <span style="color: #000000; font-weight: bold">or</span> fl<span style="color: #333333">.</span>endswith(<span style="background-color: #fff0f0">&quot;.jpeg&quot;</span>) <span style="color: #000000; font-weight: bold">or</span> fl<span style="color: #333333">.</span>endswith(<span style="background-color: #fff0f0">&quot;.png&quot;</span>) :
        image <span style="color: #333333">=</span> face_recognition<span style="color: #333333">.</span>load_image_file(rootdir <span style="color: #333333">+</span> fl)
        known_face_encodings[fl] <span style="color: #333333">=</span> face_recognition<span style="color: #333333">.</span>face_encodings(image)[<span style="color: #0000DD; font-weight: bold">0</span>]
known_face_encodings <span style="color: #333333">=</span> <span style="color: #007020">list</span>(known_face_encodings<span style="color: #333333">.</span>values())

<span style="color: #888888"># Initialize some variables</span>
new_face_locations <span style="color: #333333">=</span> []
new_face_encodings <span style="color: #333333">=</span> []
turned_off <span style="color: #333333">=</span> <span style="color: #007020">False</span>
<span style="color: #008800; font-weight: bold">print</span>(<span style="background-color: #fff0f0">&#39;Starting privacy screen&#39;</span>)

<span style="color: #008800; font-weight: bold">while</span> <span style="color: #007020">True</span>:
    <span style="color: #888888"># Grab a single frame of video</span>
    ret, frame <span style="color: #333333">=</span> video_capture<span style="color: #333333">.</span>read()

    <span style="color: #888888"># Resize frame of video to 1/4 size for faster face recognition processing</span>
    small_frame <span style="color: #333333">=</span> cv2<span style="color: #333333">.</span>resize(frame, (<span style="color: #0000DD; font-weight: bold">0</span>, <span style="color: #0000DD; font-weight: bold">0</span>), fx<span style="color: #333333">=</span><span style="color: #6600EE; font-weight: bold">0.2</span>, fy<span style="color: #333333">=</span><span style="color: #6600EE; font-weight: bold">0.2</span>)

    <span style="color: #888888"># Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)</span>
    rgb_small_frame <span style="color: #333333">=</span> small_frame[:, :, ::<span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">1</span>]

    <span style="color: #888888"># Find all the faces and face encodings in the current frame of video</span>
    new_face_locations <span style="color: #333333">=</span> face_recognition<span style="color: #333333">.</span>face_locations(rgb_small_frame)
    new_face_encodings <span style="color: #333333">=</span> face_recognition<span style="color: #333333">.</span>face_encodings(rgb_small_frame, new_face_locations)

    matched <span style="color: #333333">=</span> <span style="color: #007020">True</span>

    <span style="color: #888888"># Loop over each face found in the frame to see if it&#39;s someone we know.</span>
    <span style="color: #008800; font-weight: bold">for</span> new_face_encoding <span style="color: #000000; font-weight: bold">in</span> new_face_encodings:
        match <span style="color: #333333">=</span> face_recognition<span style="color: #333333">.</span>compare_faces(known_face_encodings, new_face_encoding)
        matched <span style="color: #333333">=</span> matched <span style="color: #000000; font-weight: bold">and</span> <span style="color: #007020">bool</span>(<span style="color: #007020">sum</span>(match))

    matched <span style="color: #333333">=</span> matched <span style="color: #000000; font-weight: bold">and</span> (<span style="color: #007020">len</span>(new_face_locations) <span style="color: #333333">&gt;</span> <span style="color: #0000DD; font-weight: bold">0</span>) <span style="color: #888888"># Make sure someone&#39;s there</span>


    <span style="color: #888888"># Depending on the state of matched, toggle the screen on or off</span>
    <span style="color: #008800; font-weight: bold">if</span> <span style="color: #000000; font-weight: bold">not</span> matched:
        <span style="color: #888888"># sp.run([&quot;xset&quot;,&quot;dpms&quot;,&quot;force&quot;,&quot;off&quot;]) # Debian, for Raspi</span>
        sp<span style="color: #333333">.</span>run([<span style="background-color: #fff0f0">&quot;pmset&quot;</span>, <span style="background-color: #fff0f0">&quot;displaysleepnow&quot;</span>]) <span style="color: #888888"># MacOS</span>
        turned_off <span style="color: #333333">=</span> <span style="color: #007020">True</span>
    <span style="color: #008800; font-weight: bold">elif</span> turned_off:
        turned_off <span style="color: #333333">=</span> <span style="color: #007020">False</span>
        <span style="color: #888888"># sp.run([&quot;xset&quot;,&quot;dpms&quot;,&quot;force&quot;,&quot;on&quot;]) # Debian, for Raspi</span>

        sp<span style="color: #333333">.</span>run([<span style="background-color: #fff0f0">&quot;caffeinate&quot;</span>, <span style="background-color: #fff0f0">&quot;-u&quot;</span>, <span style="background-color: #fff0f0">&quot;-t&quot;</span>, <span style="background-color: #fff0f0">&quot;1&quot;</span>]) <span style="color: #888888"># MacOS, has to run twice to be reliable</span>
        sp<span style="color: #333333">.</span>run([<span style="background-color: #fff0f0">&quot;caffeinate&quot;</span>, <span style="background-color: #fff0f0">&quot;-u&quot;</span>, <span style="background-color: #fff0f0">&quot;-t&quot;</span>, <span style="background-color: #fff0f0">&quot;1&quot;</span>])
</pre></td></tr></table></div>

<br>

That's all! Pretty simple program, but taught me some stuff about display power management and the trickiness of installing dlib. Also, writing this post taught me about HTML formatting ([hilite.me](http://hilite.me/) is kinda nice)

