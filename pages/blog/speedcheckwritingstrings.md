title: Speed Check
date: 2020-05-10
label: blog
tags: [projectlog, speedcheck]
snippet: What's the fastest way to record a stream of strings in Python?


I'm trying to record a stream of string data coming from a Teensy microcontroller over USB Serial. I chose a high baud rate so I can transfer and save the data quickly, but I don't want to drop any elements from the stream while I'm trying to write it down. So I wrote a little test script to see which method is fastest. 

### Results

For each method, I wrote the string "yaga," 10,000 times. 

Setting elements of a prealloc'd Python list works the fastest. I thought writing to a file would take less time, but it's actually around 3x slower. Python append works pretty fast too, but has the overhead of a list of changing size

<img src={{ url_for("static", filename = 'speedcheckStringWrite.png') }} width="400" class="d-block mx-auto"/>

<a href={{ url_for("static", filename="speedcheckStringWrite.py") }}>Link to code</a> 