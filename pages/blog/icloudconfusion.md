title: iCloud Cleanup
date: 2023-06-06
label: blog
tags: [javascript, icloud, storage, mysteriesoflife]
snippet: Script for highlighting large videos in iCloud and a storage discrepancy

Hello!

Recently I received an email from Apple letting me know that my iCloud storage was full. 

{{ add_pic("ic_appleemail.jpg", "Kind letter from Apple requesting I purchase more storage") }}

Since the cost of 200GB vs. 1TB jumps more than threefold, I embarked on a great exploration of alternatives. Since photos made up the majority of my storage (~127GB), I figured I could just go into my Photos album and click Sort By File Size.

...

Except this is not a feature offered by Apple. It's not even a feature in the iCloud browser. I guess it's a bit too technical for Apple Photos, and unfortunately it would also make it too easy to avoid paying for more iCloud storage. 

Whatever the reason, I still wanted to go through my photos by file size. Several apps exist for going through your photos and highlighting duplicates, or into your videos and showing you the file size. The only problem — photos that have been offloaded to iCloud do not show up in these apps, so they're not actually super useful. Also, would you really want random apps to scan through all your photos? 


{{ add_pic("ic_photosbysize.png", "Screenshot from a photo file size viewing app, with non-downloaded photos represented as 0B") }}

## Janky JS solution

Instead, I went to the iCloud website and thought about what was possible. I navigated to Photos->Media Types->Videos, and zoomed out as far as I could. 

{{ add_pic("ic_icloudphotos.png", "Videos anonymized by slow internet loading") }}

We can see that each video has an accompanying duration box — as long as it's an HTML element, we can use JS to search and filter them. I found that every runtime box has the class `video-text-badge`. From there is was a simple matter to find all of them in the page, sort by their duration, and highlight the ones that were past some threshold. Here's the code:

<script src="https://gist.github.com/kongmunist/a598bcdd8c226c3a3159b1a918344977.js"></script>

Because iCloud only loads the elements that are on the page, I've made this into a function that runs on a timer so new elements get highlighted as they get scrolled into. Here's what it looks like:

{{ add_pic("ic_icloudphotoshighlighted.png", "Videos bigger than 20s are surrounded by a red box, making them much easy to pick out") }}

To use it, just open the Javascript console (right click page -> Inspect Element) and paste in the entire gist. Now you can easily select multiple big videos from iCloud and download them before deleting, moving them into longer-term storage: secret HDD under your mattress, other cloud storage, etc etc. 

<hr>

# The Mystery
So, I used this script to remove all my iCloud videos >30s. The interesting thing is, after I had removed all the "big videos" and downloaded them, it cleared ~55GB from my iCloud *despite only downloading 7GB of videos.* Herein lies the mystery.

{{ add_pic("ic_dl1info.png", "All downloaded videos take up 8GB of disk space") }}

{{ add_pic("ic_dl1afterdelete.png", "iCloud storage reduces from 199GB to 143GB after downloading 7GB of videos") }}

Somehow, those 7GB of video took up way more space in the cloud than on my hard drive. Interesting...

# Experiment 1

I wanted to test this further. First, I uploaded a 4K video with a lot of motion. This took up 281 MB. My storage looked like this after uploading it:

{{ add_pic("ic_dl2storagebefore.png", "4K video uploaded, iCloud says 145.33 GB used") }}

Then I downloaded it and deleted it. The file was still 281 MB. Here is the storage afterwards:

{{ add_pic("ic_dl2storageafter.png", "4K video deleted, iCloud says 145.6 GB used") }}

Removing a 281MB video frees up ~270MB. This adds up, which is puzzling. What about the other, older videos? 

# Experiment 2
I thought that maybe older videos could have multiple copies saved in iCloud, so I searched through my videos to see if I could find a shorter one that takes up a lot of storage space. I found one with a lot of graphs, iCloud said it took up 128 MB.

{{ add_pic("ic_dl3icloudinfo.png", "Older big video that takes up 128 MB") }}

When I downloaded it, the file was only 47 MB!

{{ add_pic("ic_dl3download.png", "Downloaded video file is 47 MB") }}

And here is my iCloud storage before and after

{{ add_pic("ic_dl3storagebefore.png", "iCloud storage before deleting the old video, 145.29 GB used") }}
{{ add_pic("ic_dl3storageafter.png", "iCloud storage before deleting the old video, 145.12 GB used, reduction of 170MB") }}

So iCloud says the video is 128MB, I download it and the video is actually 48MB, and my free storage increases by ~170MB when I deleted it. Interesting!

# Conclusion
It's weird that my storage freed up more than 7x the removed files size, and weirder still that old, big videos appear to have a much larger storage footprint in iCloud than in real life. 

I am mildly interested in finding out why this happens, but I am not interested/bored enough to do it myself. If one of you fine people figure it out, please let me know by emailing me.

Anyway, I have freed up >50GB to fill with more inane videos, and written a small script that allows me to do it again in the future. Hope this proves helpful to you, dear reader.

Cya later!