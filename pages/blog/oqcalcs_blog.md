title: Quantum Optics Calculators
date: 2025-08-23
label: project
tags: [wip]
snippet: Calculators for light

Hey Max! Here's some calculators to make our lives easier.




<hr>
### Wavelength diff to frequency calculator
<!-- (c / 780.241 nm ) - (c / 780.2442 nm) -->
<form id="wavelengthForm">
	<table style="width:100%">
		<tr>
			<td>Wavelength 1:</td>
			<td><input id="wavelength1" type="number" step="0.01" value="780.241"> nm</td>
		</tr>
		<!-- <tr>
			<td>Wavelength 2:</td>
			<td><input id="wavelength2" type="number" step="0.01" value=""> nm</td>
		</tr> -->
		<tr>
			<td>Picometers offset:</td>
			<td><input id="picometers" type="number" value="3.6"> pm</td>
		</tr>
		<tr>
			<td>Distance:</td>
			<td><input id="result" style="background-color:lightgray" type="text" readonly> GHz</td>
		</tr>
	</table>
</form>

<br>
### Reverse Wavelength Calculator
<form id="reverseWavelengthForm">
	<table style="width:100%">
		<tr>
			<td>Wavelength:</td>
			<td><input id="wavelength" type="number" step="0.0001" value="780.241"> nm</td>
		</tr>
		<tr>
			<td>Frequency Difference:</td>
			<td><input id="frequencyDiff" type="number" step="0.0001" value="1.7633"> GHz</td>
		</tr>
		<tr>
			<td>Picometers offset:</td>
			<td><input id="picometersResult" style="background-color:lightgray" type="text" readonly> pm</td>
		</tr>
	</table>
</form>

<hr>


<script> /////////////// Solves the calculators equations 
function calculateResult() {
	const wavelength1 = parseFloat(document.getElementById("wavelength1").value);
	const picometers = parseFloat(document.getElementById("picometers").value);

	// TODO: Replace this with your calculation logic
	let result = (299702547000000000 / wavelength1) - (299702547000000000 / (wavelength1+picometers/1000));
	result = result/10**9

	document.getElementById("result").value = result.toFixed(4);
}
document.getElementById("wavelengthForm").oninput = calculateResult;
calculateResult(); // Initial calculation



const c = 299792458; // speed of light in m/s

function calculatePicometers() {
	const wavelength = parseFloat(document.getElementById("wavelength").value);
	const frequencyDiff = parseFloat(document.getElementById("frequencyDiff").value);

	// Convert wavelength to meters
	const wavelengthMeters = wavelength * 1e-9;

	// Calculate frequency of the first wavelength
	const frequency1 = c / wavelengthMeters;

	// Calculate the second frequency
	const frequency2 = frequency1 - frequencyDiff * 1e9;

	// Calculate the second wavelength
	const wavelength2Meters = c / frequency2;

	// Calculate the difference in picometers
	const picometersDiff = (wavelength2Meters - wavelengthMeters) * 1e12;

	document.getElementById("picometersResult").value = picometersDiff.toFixed(4);
}

document.getElementById("reverseWavelengthForm").oninput = calculatePicometers;
calculatePicometers(); // Initial calculation

</script>