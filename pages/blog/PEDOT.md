title: Everything I Know About PEDOT:PSS
date: 2021-08-05
label: blog
tags: [knowledge]
snippet: For now...

I've been reading about PEDOT, which is a conductive polymer. 

I first heard about its use in making flexible, tissue-conforming electrodes for EMG and EEG, but it is apparently good for making electro-osmotic devices as well (as well as a whole host of other things).

## Conductivity
The conductivity is quite good relative to other organic polymers, with several papers reaching a sheet resistance of 20Ω/sq [[1]](https://sci-hub.st/10.1016/j.orgel.2019.105451)[[2]](https://sci-hub.st/10.1002/elps.201000617). Compare this to a 1oz sheet of copper's sheet resistance of 0.5Ω/sq, and it's about the resistivity of titanium or lead. Raw PEDOT:PSS is something like 100kΩ/sq, so the dopants are really necessary.

## Usual forms
Usually aqeous solutions are around 1-4% PEDOT:PSS by weight, with some adding 5% diethylene glycol to increase the conductivity. The PSS is needed for enhanced solubility, though it negatively impacts the conductivity. The reference [1] above adds a graphene oxide solution as well, also to increase conductivity. It's sometimes confusing because they give the conductivity instead of the resistance, but I'm sure it's convertible.

Sigma-Aldrich sells it in dried pellets as well. Some guy on the cyan site said dissolving it in water will destroy its conductivity, but that's what [this paper](https://www.nature.com/articles/srep17045#Sec4) did with no problem. About a gram of this stuff costs $50, and people on ebay are no kinder ($50 for 30g of 1.1%)

## Working with it
Sheets of this stuff are made by pouring out a solution and letting it dry. Some people will fire it in an oven at 60C for a few hours to get all the water out. In the end, you get a flexible sheet of it. Kinda cool!

You can also remove the PSS after drying to increase conductivity. Dipping it in a solvent does the trick [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8071320/)

You can add PDMS to make it stretchier (up to 80%!), but you'll need to add this surfactant with the dope name Triton X-100. [Reference](https://sci-hub.st/10.1016/j.orgel.2019.105451)

## What I want to do with it
1. I want to deposit some and do a sheet resistance test, maybe with diethylene glycol or ethylene glycol
2. Since ethylene glycol does approximately the same thing as the much more poisonous diethylene glycol, maybe do a test with that instead [[paper]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8071320/)
3. Maybe since propylene glycol is even less poisonous than that, use it instead? It seems to work for conductvity if you soak PEDOT in it after drying it. 

<p class="caption">Ethylene Glycol > Diethylene Glycol</p>
![Ethylene Glycol > Diethylene Glycol]({{ url_for('static', filename = 'pedot_EGoverDEG.png')}})

## Conclusions

Ok so it's not much, but I hope it gives you some good leads. 

