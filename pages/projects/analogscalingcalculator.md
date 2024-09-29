title: Analog Signal Scaling
date: 2020-12-12
label: project
timespan: December 2020
pic: analogscalinggraphic.png
description: Taming an unruly analog signal into a more manageable size.

<img class="d-block mx-auto" src="{{ url_for('static',filename='analogscalinggraphic.png') }}"/>
<p class="caption">Mapping analog voltages between two rails</p>


This webpage is the live calculator I made for the analog scaling problem I highlighted in [this blog post](/blog/analogscalingvoltages/). It solves the problem of moving an analog signal within one voltage range to another voltage range with one op-amp. 

Here, an example is set up scaling ±15V sensor output to 0-5V Arduino/microcontroller analogRead-able values.


<hr>
### Circuit setup
<img class="d-block mx-auto" src="{{ url_for('static',filename='scalingvoltage_nonumbers.png') }}"/>
<form id="voltageform">
	<table style="width:100%">
		<tr>
			<td style="text-align:center">
				Vin Ranges:</td><td> Low rail: <input id="1" size="8" value="-15"> V <br>High rail:<input id="2" size="8" value="15"> V
			</td>
		</tr>
		<tr><td>&nbsp</td></tr>
		<tr>
			<td style="text-align:center">
				Desired Vout Range: </td><td> Low rail: <input id="3" size="8" value="0"> V <br>High rail: <input id="4" size="8" value="5"> V
				<!-- Vout high rail: </td><td> Vout high rail: <input id="4"> -->
			</td>
		</tr>
		<br>
	</table>
</form>
<br>

<hr>
<h2>Solution</h2>
<table width="50%">
	<tr>
		<td>
			Vref: </td><td>
			<input id="vref" size=8 disabled> V
		</td>
	</tr>
	<tr>
		<td>
			R2/R1 ratio: </td><td>
			<input id="rratio" size=8 disabled>
		</td>
	</tr>
</table>
<br>

<hr>
### Practical Implementation:

To find real-world resistors that create this reference voltage or match this resistor ratio, you can visit [this other calculator](http://jansson.us/resistors.html), which I find invaluable. 

Happy scaling!
<br>

<hr>
## Update 7/11/21
I've used this calculator several times since I initially made this page, which makes it a success in my eyes. But I have had troubles selecting real components to make the actual circuit. The Vref is off by a few mV or the ratio is sorta right, but it's hard to tell how close is close enough by the numbers alone. 

This update adds the reverse calculation of output voltage rails given the input voltage rails, Vref, and resistor ratio of the real components you've got to give you an idea of how accurate the output rails will be. 

<form id="reverseform">
	<table style="width:100%">
		<tr>
			<td style="text-align:center">
				Vin rails: </td><td> Low rail: <input id="rev1" size="8" value="-15"> V <br> High rail:<input id="rev2" size="8" value="15"> V
			</td>
			<td>Vout rails: </td><td> Low rail: <input id="revo1" size="8" disabled> V <br> High rail:<input id="revo2" size="8" disabled> V</td>
		</tr>
		<tr>
			<td style="text-align:center">
				Vref: </td><td> <input id="rev3" size="8" value="2.14"> V 
			</td>
		</tr>
		<tr>
			<td style="text-align:center">
				R2/R1 ratio: </td><td> <input id="rev4" size="8" value="0.1666"> 
			</td>
		</tr>
	</table>
</form>

<br><br>



<script> /////////////// Solves the forward simultaneous equations 
		// Input order is vin_low, vin_high, vout_low, vout_high
	 function solveAnalogScaling(v1, v2, v3, v4){
	 	console.log("solving analog scale for vin_l, vin_h, vout_l, v_out_h: ", v1, v2, v3, v4);
	 	let v = (v2*v4 - v3*v1)/(v2 + v4 - v1 - v3);
	 	let r = (v-v3)/(v2 - v);
	 	console.log("Vref:", v, "Resistor ratio:", r);
	 	return [v, r]
	 }

	 function updateSoln(){
		v1 = parseFloat(document.getElementById("1").value);
	 	v2 = parseFloat(document.getElementById("2").value);
	 	v3 = parseFloat(document.getElementById("3").value);
	 	v4 = parseFloat(document.getElementById("4").value);
	 	if ([v1, v2, v3, v4].every(elem => !isNaN(elem))){
	 		tmp = solveAnalogScaling(v1, v2, v3, v4);
	 		document.getElementById("vref").value = tmp[0].toFixed(4);
	 		document.getElementById("rratio").value = tmp[1].toFixed(4);
	 	}
	 }
	// Attach an event handler to the form above
	document.getElementById("voltageform").oninput = updateSoln;
	// run initial solution with default vals
	updateSoln();



	////////////////// 7/11/21 Solves the reverse equations
	function updateReverseSoln(){
		vinHIGH = parseFloat(document.getElementById("rev1").value);
		vinLOW = parseFloat(document.getElementById("rev2").value);
		Vref = parseFloat(document.getElementById("rev3").value);
		rratio = parseFloat(document.getElementById("rev4").value);

		if ([vinHIGH, vinLOW, Vref, rratio].every(elem => !isNaN(elem))){
			lowRail = (Vref-vinHIGH)*rratio + Vref;
			highRail = (Vref-vinLOW)*rratio + Vref;
			document.getElementById("revo1").value = lowRail.toFixed(4);
			document.getElementById("revo2").value = highRail.toFixed(4);
		}
	}
	document.getElementById("reverseform").oninput = updateReverseSoln;
	updateReverseSoln();
</script>