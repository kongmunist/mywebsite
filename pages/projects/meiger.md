title: Meiger Counters
date: 2023-05-30
label: project
timespan: October - November 2021
pic: meiger_hero.jpg
description: Geiger's 2nd most famous counter, the electromagnetic radiation detector

<p style="text-align: center;"><i>
    Artsy project done with the F21 Electronic Logics && Creative Practice class in IDeATe.
Not medical advice. </i></p>

<hr>


{{ add_pic("meiger_presentation.png", "", True) }} 

Living in developed countries means constant exposure to all kinds of dirty electrical noise and strong magnetic fields. While the human body mostly signals with chemicals and ions, our brain — the intellectual center and chief information processor — communicates via electricity. 

In the presence of electromagnetic (EM) fields, these signals and pathways can become muddled and interfere with maintenance and development of new neural pathways. 

{{ add_pic("meiger_hero.jpg", "", True) }}

That's why I invented the __Meiger Counter__, the first handheld device used by reasonable, cautious people all over the world to detect and isolate dangerous sources of electromagnetic noise that could be putting you or your loved ones at a higher risk for cancer [[1]](https://www.sciencedirect.com/science/article/abs/pii/S0013935121012883). 

{{ add_pic("meiger_andypresent1.jpg", "", True) }}

Each Meiger counter comes with a dial and speaker to alert you whenever a strong electrical field is nearby. Simply press the trigger while pointing our proprietary directional Efield Antenna at a source you suspect is poisoning the environment around you, and the rate of clicking will tell you the strength of the source.

{{ add_pic("meiger_case.jpg", "Meiger Counters in carrying case, v1 on the left and v2 on the right ") }}

The device is lightweight, portable, and easily rechargable. Each counter comes with a lifetime guarantee, no electrical field-induced death-causing cancer or your money back!

<div class="video-container">
        <iframe class="youtubevideo" src="https://www.youtube.com/embed/iLK8d7VIhHs"allowfullscreen></iframe>
</div>

<br><hr><br>

# Build details
The carrying case was scavenged from a Roboclub cleaning, it's a DeWalt case with no tools in it. Foam is from the cleaning as well. I cut it with a package opener, which is why it looks rather rough. 

{{ add_pic("meiger_dewalt.jpg", "") }}
{{ add_pic("meiger_foamcase.jpg", "") }}

Meiger counter handles are made from the case of a Metrologic MH290 handheld barcode scanner, one of the [first ones ever sold commercially](../../blog/barcodehistory/). The top part is 3D printed on an SLS printer. To try and make it look vintage, I printed it out of a clear resin and then overexposed it in UV light. My post-processing was pretty crude, but I think it looks pretty good. 

{{ add_pic("meiger_closeup1.jpg", "") }}
{{ add_pic("meiger_closeup2.jpg", "") }}
{{ add_pic("meiger_closeup3.jpg", "") }}

The Meiger counter ticks according to a Poissonian distribution, same as a Geiger counter. This makes the clicks sound eerily similar, and create a similar feeling of danger. The lambda of the Poisson distribution is determined by the variance of the analog readings on a wire antenna inside the counter. The higher the variance, the more frequent the clicks. This works pretty well for picking up electrical noise from power hubs, overhead lights, and large electronic devices. 




# Informational details

To make the presentation more convincing, I read several articles about the relationship between electromagnetic fields and various medical conditions. They presented some compelling correlations between weak magnetic fields and rates of leukemia in children, and many other conditions. The audience believed I had invented these studies, but they were quite real. Here are some screenshots from my slides:

{{ add_pic("meiger_bees.png", "") }}

{{ add_pic("meiger_humans.png", "") }}

{{ add_pic("meiger_iarc.png", "") }}

{{ add_pic("meiger_andypresent2.jpg", "") }}

Adding this to the list of things that make you go "huh!"


