title: Comparing The Sugar Percentage Of A Peach vs. Sugary Drinks
date: 2021-07-23
label: blog
tags: [refractometer, experiment]
snippet: Testing out a scientific device is sweet!

It's a shame: I've met many smart people who were never educated in the fine art of slapping a watermelon to determine their ripeness by their (usually immigrant) parents. I thought I could do these poor folks a great service by using technology to help them figure out a watermelon's sweetness for them.

<p class="caption">Refractometer on the left. The liquid goes on the blue part at the top. The bar chart on the right is what you see through the peephole. </p>
![Refractometer on the left. The liquid goes on the blue, tilted part. The bar chart on the right is what you see through the peephole. ]({{ url_for('static', filename = 'refractest_displaypic.png')}})


The first step is determining how sweet the watermelon is, so of course I had to go buy a refractometer. As it turns out, adding sugar to water changes how much light rays bend when they go through the water, AKA the index of refraction (IOR). A refractometer lets anyone look through a peephole to compare an unknown sugary liquid to water (0% sugar). By looking at where the new line of intersection is on the graph, we can figure out exactly how many degrees Brix there are. Brix is just a complex way to say % sugar by weight. 

<p class="caption">Arrangement of all the liquids I had to try</p>
![Arrangement of all the liquids I had to try]({{ url_for('static', filename = 'refractest_showcase.jpg')}})

After I got the refractometer, I really wanted to make sure it gave out accurate numbers for both fruit and regular liquids. It just so happened that there were several sugary drinks in my pantry leftover from a club party, which listed their grams of sugar and grams of total mass under Nutrition Facts. Using this, I'd be able to determine the proper sugar content before confirming it with my refractometer. 

<hr>
# Onto the results!!

In all, I measured 3 drinks (Caprisun, Coke, Izze Green Apple), 1 fruit (peach), and 1 syrup (Hershey Caramel). I'll present them in increasing order by sugar content

## Caprisun (7.9˚ Brix)
The refractometer hit this one on the head, which was helped by the fact that the Caprisun is so liquidy and has very few other ingredients

True sugar: Grams carbs / grams total = 14g / 177g = 7.9%<br>
Refractometer: 7.9% 

<p class="caption">Caprisun, Pacific Cooler edition</p>
![Caprisun, Pacific Cooler edition]({{ url_for('static', filename = 'refractest_caprisun.png')}})


## Izze Green Apple (9.7˚ Brix)
A little further off on this drink. It might have been because of the carbonation forming bubbles in the sample.

True sugar: 24g / 248g = 9.7% <br>
Refractometer: 9.4%
<p class="caption">Izze Green Apple. Tastes like green apple.</p>
![Izze Green Apple. Tastes like green apple.]({{ url_for('static', filename = 'refractest_izze.png')}})


## Regular Coke (10.5˚ Brix)
This number was a bit harder to find. Turns out a 12oz can of Coke is 355mL, but the density is a bit higher than that of water (1.042 g/mL), which affected the denominator. 

The change in density may also be the reason the Izze's reading is off. Using the density of Coke at the volume of Izze gives a true sugar rating of 9.39%, which is exactly what we got from the refractometer.

True sugar: 39g / 369.9g = 10.5%<br>
Refractometer: 10.3%
<p class="caption">Coke had the highest amount of sugar by weight, but not by much (~2.6% higher than the lowest, Caprisun)</p>
![Coke had the highest amount of sugar by weight, but not by much (~2.6% higher than the lowest, Caprisun)]({{ url_for('static', filename = 'refractest_coke.png')}})

## Peach (8.7˚ Brix)
I juiced a slice of this peach, but forgot to take a photo before beginning to eat the rest. No ground truth for this one. 

Refractometer: 8.7%
<p class="caption">So, still think fruit is healthy?</p>
![So, still think fruit is healthy?]({{ url_for('static', filename = 'refractest_peach.png')}})

## Hershey Caramel (61˚ Brix)
Because this liquid is so syrupy (it is syrup), I had to dilute it down. My refractometer range also stops at 38˚ Brix. I added 1 part caramel, 9 parts water and mixed it until uniform. I then added this liquid to the refractometer and read it. 

True sugar: 25g / 40g = 62.5%!<br>
Diluted 10x: 6.25%<br>
Refractometer: 6.1%
<p class="caption">Majority sugar caramel syrup</p>
![Majority sugar caramel syrup]({{ url_for('static', filename = 'refractest_hershey.png')}})


# Closing notes
## Refractometer Limitations
I had a lot of fun running these experiments, partly because I got to sip sugarly liquids while doing it. I'm also shocked at how accurately my Amazon refractometer performed. However, there were a few challenges with using the refractometer that I want to mention.

1. Sugar and salt are confounding; both raise the index of refraction at similar concentrations. This must be adjusted for in higher-salt liquids.
2. Carbonated drinks bubble up underneath the test plate, which can't be good for accuracy. 
3. Limited range of 0-38% sugar means dilution is necessary for some solutions, which can add error.
4. Lack of density knowledge about Izze or Coke may have also skewed my numbers. As I mentioned above, adjusting the weight of Izze using a higher density gave an alternate sugar percentage that matched exactly what I read on my refractometer.
5. No precision or digital readout means measurements are slow and annoying to perform manually. 

## Weird findings
The variance in the sugar % of drinks is surprisingly small. To be fair, I only did a small number of drinks, but they only varied by 2.6% despite tasting wildly different. 

Also, Caprisun is healthier than peaches if we're going by sugar percentage. Tell that to your mom next time she berates you for picking an "unhealthy" snack!

Now, onto the humble watermelon!
