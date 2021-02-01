title: Physical Word Length Calculator 
date: 2021-01-31
label: blog
tags: [calculator, p5js, cursive]
snippet: Determine how much string you'll need to spell out a phrase

Hi! I'm making a neon sign with cursive on it, and wanted to know how much neon I'd need to spell out all the letters. To do this in real life, you'd need to cover each letter in string and measure the string, or draw it on a computer and count how long the curve was. 

I wasn't able to find the latter calculator anywhere, so I wrote this little p5.js sketch that you draw a letter onto and it tells you how many pixels long it is. Using this total pixel length and your neon wire length, you can calculate the inches/pixel and figure out how large your letters can be. 

## Instructions
Draw on this canvas and when you release the letter it'll tell you how many pixels long you drew. It doesn't matter how fast you draw, it'll be about the same length either way.

The old shapes are drawn in light grey so you can draw them to scale with each other. Press k to delete the last saved shape, or tap if you're on mobile.

<div id="sketch-holder">
</div>

<script src=https://cdn.jsdelivr.net/npm/p5@1.2.0/lib/p5.js></script>

<script type="text/javascript">
	var drawPt = [];
	var drawPtHistory = [];
	var dragged = false;
	var totalDist = 0;

	function setup() {
	  canvas = createCanvas(640, 360);
	  canvas.parent('sketch-holder');

	  textAlign(CENTER, CENTER);
	}

	function draw() {
	  background(255);
	  fill(0);
	  text("Press z or tap to erase the last shape", width/2, 40);

	  if (drawPt.length == 0){
	      text("Total length: " + nf(totalDist,0,2) + " pixels", width/2, 20);
	  } else {
	      stroke(0);
	      for (let i = 0; i < drawPt.length-1; i++){
	          line(drawPt[i][0], drawPt[i][1], drawPt[i+1][0], drawPt[i+1][1]);
	      }
	  }
	  
	  for (let i = 0; i < drawPtHistory.length; i++){
	      stroke(200);

	      let mhm = drawPtHistory[i];
	      //prletln("mhm len", mhm.createCanvas());
	      for (let j = 0; j < mhm.length-1; j++){
	          line(mhm[j][0], mhm[j][1], mhm[j+1][0], mhm[j+1][1]);
	      }
	  }
	}

	function keyPressed(){
	    if (key == 'z'){
	        drawPtHistory = drawPtHistory.slice(0,drawPtHistory.length-1)
	    }
	}

	function mouseDragged(){
	    drawPt.push([mouseX, mouseY]);
	}

	function mouseReleased(){
	    totalDist = 0;
	    for (let i = 0; i < drawPt.length-1; i++){
	        totalDist += dist(drawPt[i][0], drawPt[i][1],
	                          drawPt[i+1][0], drawPt[i+1][1]);
	    }

	    if (totalDist < 10){ // Remove on tap for mobile users
			drawPtHistory = drawPtHistory.slice(0,drawPtHistory.length-1)
	    } else{
	    	console.log("Total dist: " + totalDist);
		    drawPtHistory.push(drawPt);
		    drawPt = [];
	    }
	}

</script>

