function getKeyByValue(object, value) {
return Object.keys(object).find(key => object[key] === value);
}

function makeGraph(){
dict = {result};
baked = Object.values(dict);
baked = baked.sort();
stuff = [];
for(var i = 0; i < baked.length; i++){
    stuff[i] = getKeyByValue(dict, baked[i]);
}

stuff = stuff.reverse()
baked= baked.reverse()
document.write(5+6)

var ctx = document.getElementById('myChart');
//   ctx.canvas.width = 3000;
//   ctx.canvas.height = 3000;
  var myChart = new Chart(ctx, {
      type: 'horizontalBar',
      responsive: true,
      // options: opt,
    //   showTooltips: false,
    //   maintainAspectRatio: true,
      data: {
          labels: stuff,
          datasets: [{
              label: 'Percent Match',
              data: baked,
              backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 159, 64, 0.2)'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(255, 159, 64, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          legend: {
              display: false
          },
          scales: {
            xAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Percent Match (%)'
                },

                  ticks: {
                      beginAtZero: true,
                      max: 100,
                      stepSize: 10
                  }
              }],

              yAxes: [{
                  scaleLabel: {
                      display: true,
                      labelString: 'Perscription'
                  }
              }]
          }
      }
  });
}
