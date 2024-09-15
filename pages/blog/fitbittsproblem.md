title: "Fitbit timestamps cannot be trusted"
date: 2024-01-15
label: log
tags: [personalinformatics, quantifiedself, data, complaint]
snippet: "Please recommend me alternatives"

Yesterday I slept kinda funny and discovered something horrible about Fitbit's data collection.

# The Story

On January 14th, I got tired early and slept from 8pm to midnight, then got up until I slept again from 5am-10am. In the afternoon, I noticed that my Fitbit's time was off — this happens if the battery is allowed to be dead for more than 1-2 days. It said 10:xx on January 13th (Sat), but the time was actually 4:xx on January 15th (Mon), meaning it was off by ~42 hours (or 54, not sure the am/pm). 

When I synced my Fitbit app from the phone, it usually fixes the time shift, so I did that. Then I looked at my sleep history and saw it. 

{{ add_pic("fitbittsproblem/0.png", "") }}

Here we see my two sleep sessions logged under Friday — but the times are totally wrong, 2pm-6pm then 11pm-3am. 

Consider that before I synced it, my Fitbit time was ~6 hours behind the real time (said 10, was 4). If we add 6 hours to the sleep logs, the times become correct (8pm-12am, 5am-9am). This is horrible!

# Why is it horrible?

I always assumed that if the Fitbit's clock was wrong and sleep data is recorded, the data's timestamps would get back-corrected when syncing with a true time source (smartphone). Instead, Fitbit just keeps the old (wrong!) timestamps of the data and corrects the device time for future data collection.

The way Fitbit handles this data logging is even worse than just deleting it — instead of no data (which cannot screw up your analyses), I have a incorrectly-recorded night of sleep data with the wrong timestamps (which can screw up your analyses). 

# Maybe it's not that often?

The Fitbit dies after a week, I leave it uncharged for long enough about 1/5 of the time. I don't sync my Fitbit very consistently, meaning up to ~4 days of data can have the wrong timestamps. 4/35 is more than 10% of my data, recorded with incorrect timestamps, completely uncorrectable and undetectable when doing sleep analysis on myself. Whatever the effects, it sure doesn't help me.

# What now?

I believed it was common sense to correct data timestamps that were recorded when the "true" time is unknown (e.g. waking up from dead battery), but it seems that collecting accurate data is not Fitbit's forte. First the thing about the <a href="../fitbitsleeptzcorrection">timezones</a>, now they're persisting incorrect timestamps — I'm officially in the market for a better fitness tracker. No Fitbit, all their trackers will share these same problems.

I would take the Apple Watch if it had less screen, and I'm considering Xiaomi but I haven't looked into if the data export is any better. Whoop looks good, but is a bit pricy for an unemployed boy like me. Oura also, but the ring is too chunky. Arghh, what happened to the market fulfilling my needs?

Anyway, please DM me if you know of an alternative tracker that DOESN'T ruin the data while collecting it. 
