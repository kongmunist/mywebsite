title: "Most-scanned bulletin boards at CMU"
date: 2024-04-15
label: blog
tags: [cmu, carnegiecalendar]
snippet: "Finally publicizing some sneaky data collection from 4 years ago"

Hello!

Back when I attended CMU, there were these massive bulletin boards around campus full of adverts from students and profs. Students usually promoted their app/club/org/student course, and professors pushed their classes.

{{ add_pic("cmuads/0.jpeg", "") }}

When I started putting my own ads on these boards, I was always curious which b-boards were the most frequently looked at. For instance, the board between the Sorrells library and the bathroom gets a lot of traffic, but the people walking there were probably pretty focused on studying. Whereas the UC bulletin boards get less foot traffic, but the people there seem calmer since they aren't walking fast to get to class.

Anyway, when I finished a campus events aggregator called [Carnegie Calendar](../../projects/carnegiecalendar) and wanted to promote it by putting up bulletins, I finally had my chance to determine the highest engagement b-board. I printed out 63 of these flyers promoting Carnegie Calendar, each with a unique QR code demarcated by this little number in the corner. Each QR code led to the same website with a different trailing URL argument, which my server recorded in a text file. 

{{ add_pic("CCzoomin.png", "") }}

I got a bunch of friends to help me put up the QR codes (Thanks Nancy Sam Ruijie and I think Nate?) and waited for the data to roll in.

I always wanted to sell this data to some overzealous student group that puts up a ton of flyers and cares about it, but after 4 years I'm realizing that's probably not gonna happen. So I've tabulated the results into this map below.

{{ add_pic("cmuads/1.png", "") }}

More granularly, the per-bulletin board data can be found [here](https://docs.google.com/spreadsheets/d/1T-BplbYhJhCCI-hyfR-BIS-O5AUM7uf--s4L8abqz_0/edit#gid=1010815453).

A day or two after all the flyers were up, I realized that it would be free traffic if I also advertised the website in the school Facebook groups. I made a separate URL extension for the group links and posted it. The single Facebook link received around 6x the visits to all in-person links despite only being up for like 8 hours. 

{{ add_pic("cmuads/2.png", "") }}

As with all deploys, some event I scraped the first day of public release ended up busting the website, and I didn't realize until noon the next day. I always wonder about those missed first impressions. Anyway, enough lore for the day. Cya next time!
