title: Power-over-Skin
date: 2024-10-22
label: project
timespan: December 2023 - October 2024
pic: poweroverskin/PoS_Snail.JPG
description: Battery-free wearables, powered through body contact!

{{ add_pic("poweroverskin/andytalking.jpg", "Andy talking at UIST") }}

Hello! Today I'd like to tell you about my first UIST paper, Power-over-Skin! First, let me get all the links out of the way

- Paper (open-access): [ACM Digital Library](https://dl.acm.org/doi/10.1145/3654777.3676394), [(mirror)](https://drive.google.com/file/d/17qtaXyanAeJqdw0Rrbnp-YJJgXEy5sqx/view?usp=sharing)
- Video: [YouTube](https://www.youtube.com/watch?v=5PEN04-jyCU)
- Talk: [YouTube](https://www.youtube.com/watch?v=gi56CEKdBYY)
- Layman explanation: [Twitter thread](https://x.com/oldestasian/status/1846292645707919531)
- Project page: [Figlab](https://www.figlab.com/research/2024/poweroverskin)
- Hardware: [GitHub](https://github.com/kongmunist/Power-Over-Skin-Hardware)

{{ add_pic("poweroverskin/PoS_Snail.JPG", "Snail-shaped blinker used to demo Power-over-Skin") }}

<hr>

# Why did you do this?

I could say many reasons to motivate this project, all of them true. 

- 1, I did this project because I wanted to wirelessly power wearable devices using the batteries that we already carry around, like those in our phone or headset. 
- 2, I did this project because I thought it was really cool, and I wanted to start doing backscatter but got nerdsniped by this instead.
- 3, I want to know every quantifiable feature of my body and mind at all times so I can learn things about the human body, and I don't want to have to think about charging or wearing a device that tracks all of this stuff for me, and I thought it would be most convenient to wear a battery-powered transmitter somewhere on the body and power all these battery-free implanted sensors that track my body for me, and this was the method that I thought would work, but actually it doesn't work because this technique requires an externally-coupled ground plane which you can't get from fully within the body, but that's ok because the technique still has useful outputs like powering wearables and transdermal implants which are half-in half-out of the body.  


# FAQ
### This is just thermal harvesting!
It's literally not, please read anything I ever wrote about it. I think people think this because we used a heatsink for the ground plane in the snail image, but this was just because it was copper and had high surface area. 

### This is like the matrix?
In the Matrix, they harvest power from like the humans in the pods. But we're not actually taking power from the body, we're putting it through the body using another battery-powered transmitter.

### Does this shit work through pants? 
This shit does work through pants! Power is reduced since there is a weaker capacitive coupling through clothing, but it does work!

### Can you transmit data too?
 there's a lot more prior work on transmitting data through the human body, this is a field known as Human Body Communication or Body Area Networks. This involves a powered receiver, however, and even companies like Ixana have to power both devices on the transmit and receive sides. I'm interested in extending this work to transmit data through backscatter on the skin —  if you have any interest in this, please reach out because I need a collaborator.  

<hr>
# Assorted ramblings which are not coherent but do explain how I started thinking about this 

### Background
I feel like I've talked this project to death by now, so in this post I'd like to explain why I worked on this. 

My last project before leaving Switzerland involved over-air power transfer, using the PowerCast transmitters which broadcast at 915 MHz. By holding a harvester board with a short wire antenna, we could pick up several milliwatts and use it to light up an LED.

This was already dope, but during my lit review I found something even doper. There was a Nature paper claiming that through-body power transmission was possible, using the human tissue as the wire! I rushed to replicate their circuit, and indeed got a little trickle of power over my skin.

### Personal info tracking
I have a special interest in personal informatics, which involves analyzing your own biological/cognitive/logistical data in order to do early diagnosis and health optimization. For example, a question one might answer is "how much does coffee increase my alertness compared to Adderall?" or "has my reaction time slowed down in the past 5 years?" — these questions require a lot of data, and it's better to start tracking early (especially since it's automatic).

In 2024, I'd been wearing a Fitbit for about 2 years. This gives me good bio data but there were shortcomings — mainly, the need to charge it regularly and the physical presence on my wrist. The presence was a problem because I didn't like that it got caught on things, and I didn't like that other people could see me tracking. Admittedly, a petty reason, but in a perfect world I would've preferred a hidden sensor that could do all the things that my smartwatch could do. Sounds like an implant, no?

### Modern implants are the same one as 10 years ago

I was really interested in hobbyist implants as a kid (~2014), and I started looking into them again to see if anyone had made a smartwatch replacement yet. How surprised I was to find them still selling the same old RFIDs and magnets! The field had not progressed at all, even though there were many more options for nanopower devices and sensor chips nowadays. The closest thing I could find to a fitness tracker was [Temptress](https://augmentationlimitles.ipage.com/temptress/) by Augmentation Limitless, which is an implantable NFC chip that reads off the temperature when you tap your phone to it. While cool, this was even less automatic than the Fitbit. 

When you think about it, the problem with implants has always been the difficulty of getting power through the skin into the implant. We've devised ways around this, for example wearing a battery pack immediately outside the implant (Eversense CGM) or just putting a battery in the implant which makes it either one-time use (Most CGMs) or require recharging (Guardian CGM). Neither of these appeal to me because they have the same problem as the Fitbit. 

This led me to energy harvesting and wireless power transmission to power an implanted device. [Lepht Anonym](https://sapiensanonym.blogspot.com/) has implanted an inductively-charged implant before, but the prospect of fitting a large inductive coil in my body kinda skeeved me out. The lessons from this are 1) inductive charging through the skin couples enough power to turn on a Raspberry Pi (not even a smaller Zero!) inside the body (power budget is a 1-5 watts), 2) WiFi works through the body. Incredible. Anyway, I wasn't doing that.

{{ add_pic("poweroverskin/lepht_lessons.png", "Lessons from Lepht Anonym's pirate box implant") }}




<script>
    document.addEventListener('DOMContentLoaded', function() {
        // If "l" is pressed, redirect to ../blog/lablunch2024
        document.addEventListener('keydown', function(event) {
            if (event.key === 'l') {
                window.location.href = "../../blog/lablunch2024";
            }
        });
    });
</script>