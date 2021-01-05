title: WAV file to clipboard
date: 2020-12-12
label: blog
tags: [wip]
snippet: Copy a wav's values to your clipboard so you can play them on an Arduino

<script>
	// source: https://gist.github.com/lihnux/2aa4a6f5a9170974f6aa
	// Original source: https://stackoverflow.com/questions/18729405/how-to-convert-utf8-string-to-byte-array

	// JavaScript Strings are stored in UTF-16. To get UTF-8, you'll have to convert the String yourself.
	function toUTF8Array(str) {
	    let utf8 = [];
	    for (let i = 0; i < str.length; i++) {
	        let charcode = str.charCodeAt(i);
	        if (charcode < 0x80) utf8.push(charcode);
	        else if (charcode < 0x800) {
	            utf8.push(0xc0 | (charcode >> 6),
	                      0x80 | (charcode & 0x3f));
	        }
	        else if (charcode < 0xd800 || charcode >= 0xe000) {
	            utf8.push(0xe0 | (charcode >> 12),
	                      0x80 | ((charcode>>6) & 0x3f),
	                      0x80 | (charcode & 0x3f));
	        }
	        // surrogate pair
	        else {
	            i++;
	            // UTF-16 encodes 0x10000-0x10FFFF by
	            // subtracting 0x10000 and splitting the
	            // 20 bits of 0x0-0xFFFFF into two halves
	            charcode = 0x10000 + (((charcode & 0x3ff)<<10)
	                      | (str.charCodeAt(i) & 0x3ff));
	            utf8.push(0xf0 | (charcode >>18),
	                      0x80 | ((charcode>>12) & 0x3f),
	                      0x80 | ((charcode>>6) & 0x3f),
	                      0x80 | (charcode & 0x3f));
	        }
	    }
	    return utf8;
	}

	var expose;
	var expose2;
	var expose3;

	function openFile(event) {
	    var input = event.target;
	    expose = input;

	    // Read each file
	    if (input.files.length != 1){
	    	console.log("selection invalid, returning");
	    	return;
	    }

    	let fileObject = input.files[0];
    	expose2 = fileObject
    	// start string at  d.indexOf("data") + 4 

    	fileObject.text().then(fileContents => {
            fileName = fileObject.name;
            console.log("processing", fileName)

            expose3 = fileContents;

            // Cut off the header
            let trimmedString = fileContents.slice(88);

            // Turn the string into an array of the bytes
            let byteArray = toUTF8Array(trimmedString)
            // const newArray = oldArray.filter( value => !Number.isNaN(value) );
            // const reducer = (accumulator, currentValue) => accumulator + currentValue;

            // const maxer = (acc, cur) => cur > acc ? cur : acc;
            // const miner = (acc, cur) => cur < acc ? cur : acc;
            // maxVal = expose3.reduce(maxer);
            // minVal = expose3.reduce(miner);
            

            // expose3 = byteArray;

            // f
            // Set the output 
            document.getElementById("output").innerText = byteArray.join(", ");


            // Do stuff here 

            console.log(fileName, " parsed");
        });
	}
</script>

<input type="file" onchange='openFile(event)'>

WAV dump: 
<textarea id="output" rows=50 cols=100></textarea>

