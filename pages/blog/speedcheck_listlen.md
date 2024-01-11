title: Speed Check — Generating a list of a range of a len
date: 2020-11-25
label: blog
tags: [speedcheck, matplotlib]
snippet: Why does matplotlib set_data not take an iterable :(

As part of my [PPG project](https://twitter.com/redlightguru/status/1331513267697676289?s=20), I had to create a live-updating plot. I'm most familiar with the matplotlib library, which has the same color scheme as MATLAB, so I'm using that. One problem is that they try to make a general-purpose plotting tool (matplotlib.pyplot) that also leaves you free to not worry about which window holds which figure and which renderer is drawing what, when. This is really bad because more general tools are more complex to use, and this is definitely the case here.

It's usually imported as `import matplotlib.pyplot as plt`. To create a 2-part plot involves creating Axes, which are done by `plt.subplot(rows, cols)`. Then you write `line = ax.plot(x,y)`, which doesn't seem bad until you try to *use* the `line` object you just created, and then you find out you have to call `line, _ = ax.plot(x,y)` since it gives multiple things back. 

I won't do a full rant since that's not the point, but basically it's annoying, and if you call `ax.plot()` again, it creates a new line that overlaps with the old line. It's a pain. I needed two live-updating plots, so you can save the `line` object as a variable and call `line.set_data(x,y)` to change the data without adding a new line onto the graph. 

Now, my data was time-series, and I just wanted the index of the array as the x axis. So for data like `[0.5, 1.3, 2.4]`, I wanted an x list that was `[1, 2, 3]`. This is easy enough, it's just `list(range(len(data)))`. And no, I tried using just `range(len(data))`. It has to be complete. I also thought of using enumerate, and taking only the first element in a list-comprehension. So I decided to compare them.

This was my first time using the `timeit` library, and as far as I could tell, it was kinda spotty in terms of consistency. Here's the code:

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
28</pre></td><td><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">import</span> <span style="color: #0e84b5; font-weight: bold">timeit</span>

uniqueTimes <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">10</span>
b <span style="color: #333333">=</span> [<span style="color: #0000DD; font-weight: bold">0</span>]<span style="color: #333333">*</span><span style="color: #0000DD; font-weight: bold">10000</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">lenList</span>(lst):
    <span style="color: #008800; font-weight: bold">return</span> [x1 <span style="color: #008800; font-weight: bold">for</span> x1,x2 <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">enumerate</span>(lst)]
<span style="color: #888888"># 0.7 ns/elem</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">lenList2</span>(lst):
    <span style="color: #008800; font-weight: bold">return</span> <span style="color: #007020">list</span>(<span style="color: #007020">range</span>(<span style="color: #007020">len</span>(lst)))
<span style="color: #888888"># 0.22 ns/elem</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">mapList3</span>(elem, count <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">0</span>):
    count <span style="color: #333333">+=</span> <span style="color: #0000DD; font-weight: bold">1</span>
    <span style="color: #008800; font-weight: bold">return</span> count<span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">1</span>
<span style="color: #888888"># 3.7 ns/elem</span>

functs <span style="color: #333333">=</span> [<span style="color: #008800; font-weight: bold">lambda</span> : lenList(b),
            <span style="color: #008800; font-weight: bold">lambda</span> : lenList2(b),
            <span style="color: #008800; font-weight: bold">lambda</span> : <span style="color: #007020">list</span>(<span style="color: #007020">map</span>(mapList3, b))]

timesEach <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">1000</span>
<span style="color: #008800; font-weight: bold">for</span> i <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">range</span>(<span style="color: #007020">len</span>(functs)):
    times <span style="color: #333333">=</span> []
    <span style="color: #008800; font-weight: bold">for</span> j <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">range</span>(uniqueTimes):
        times<span style="color: #333333">.</span>append(timeit<span style="color: #333333">.</span>timeit(functs[i], number<span style="color: #333333">=</span>timesEach))
    <span style="color: #008800; font-weight: bold">print</span>(i, <span style="background-color: #fff0f0">&quot;ns/elem:&quot;</span>, <span style="color: #007020">sum</span>(times)<span style="color: #333333">/</span>timesEach<span style="color: #333333">*</span><span style="color: #6600EE; font-weight: bold">1e6</span><span style="color: #333333">/</span><span style="color: #007020">len</span>(b))
</pre></td></tr></table></div>


Turns out the naive `list(range(len(x)))` solution was the fastest! Until next time, cya!