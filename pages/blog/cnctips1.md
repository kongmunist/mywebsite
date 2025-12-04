title: "First lessons from ordering CNC parts from China"
date: 2025-12-04
label: log
tags: [cnc, chargerless]
snippet: "metal on tap"

I'm working on Chargerless, a minimal, self-powered health tracker for the wrist. In this post I'm gonna share some tacit knowledge I've acquired from doing several CNC orders

The Chargerless device is so small that the case needs to be super sturdy to tolerate daily stresses without popping out the spring bars that hold the band, so I've decided to make the enclosures out of metal. At first I went through a NYC company that does small batch investment casting for the enclosures (resin printed pos -> neg plaster mold -> pour brass/silver to make a final piece), but the gate cutting and polish/buffing is pretty expensive (measured in either time or money). I wasn't able to find Chinese shops to do small batch casting + finishing (MOQs usually around 300-1000 pc), so instead I started looking at Chinese CNC. 

I'd tried JLC or PCBWay's CNC services in the past, but for my model they would always charge an unreasonable price — for first prototypes this was fine, but later on I needed to be able to get a bunch of them. I took 3-4 suggestions for other CNC shops from friends and either got connected over email or just filled out the contact form. After a few emails back and forth, I would send my 3D model and the quantity, materials, postprocessing, and finishes that I wanted. After half a day they'd send back a quote (excel spreadsheet), I would sign and pay and send it back. 9 days later they'd say "hey your parts are out the door, thanks for doing business" and then I'd wait eagerly for the parts to arrive.

The main things I've learned from this are as follows:

- You just need to send a model, no drawing is necessary unless you have a critical dimension. 

- Aluminum is cheap, Stainless steel is expensiver, and Titanium is really expensive, followed ratios of roughly 1:2:3 in my experience

- There's only like 5 surface finishes, and since they're portable between shops you need to use them when asking for quotes. Listed in order of increasing smoothness: matte, satin, as-finished, glossy, and mirror-finish — the first few are done by sand or bead-blasting, the latter two are done by hand so are pretty expensive.

- CNC shops mess up sometimes, so the first job with a new vendor shouldn't be a huge order. My first model there were visible tool marks on flat surfaces, and certain holes were deburred way too much. By taking good pictures and sending them back to the agent, these problems were fixed in future orders. If you've gotten a model CNC'd before and had to correct things with the vendor, when you go to another shop send a little slideshow of the errors of past vendors just so they know what to avoid

- Price breaks happen around 10 and 100, you can feel free to ask for a quote with 10pc and 100pc of the same model just to see how future costs will scale

- Just like there are electronic parts where you don't care about where its from (jellybean components), CNC is a jellybean operation. If your prices are too high, get your model quoted elsewhere, nobody will mind

- Finishes are metal-specific: aluminum gets anodization (any color), steel gets PVD (any color), powder coat (any color), Cerakote (any color), chrome plate (silvery), blackened (black). Just know your options

- Anodization is a great way to color aluminum parts, but has its downsides. It can leave spots in surfaces, and it definitely will be a slightly different color each batch. But it is nonconductive

Ok that's all, just words this post! Cya around
