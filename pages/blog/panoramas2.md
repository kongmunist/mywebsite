title: Creating panorama images manually, pt 2!
date: 2020-11-18
label: log
tags: [CV, OpenCV]
snippet: Better stitching by doing something really easy I just forgot to consider

Late last night I was greeted in my dreams by a green, ghastly spectre, who said unto me: "Instead of adding 1 image at a time, did you try stitching 2 and 2, then the two composites? This would greatly reduce the distortion suffered by the latter images," in a spooky voice. I said "No I didn't think of that," then woke up and tried it. It immediately looked way better. Here's the results

![Improved stitching]({{ url_for('static', filename = 'panorama2_betterstitch.jpg')}})

I think due to the distortion being lessened, the total features being found are much better for the two pairs than for adding one image at a time. Here's an example of the keypoints being connected across. 

![Keypoints comparison across the new method]({{ url_for('static', filename = 'panorama2_keypointcrossanalysis.jpg')}})

I guess divide and conquer really has its merits. 