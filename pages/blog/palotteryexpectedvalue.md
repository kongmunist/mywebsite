title: Calculating the expected value of the PA scratch offs
date: 2021-02-04
label: log
tags: [lottery, wasteofmoney, probability]
snippet: It's ok, all proceeds pay for the benefits of older residents of Pennsylvania

Hi! Yesterday I had a dream where I won a math prize (unlikely) and received a prize of 200 million dollars (even more unlikely). I then woke up, and decided that I needed to lose 20 dollars immediately on the Pennsylvania lottery (I think the odds of this one are the most unlikely out of all three occurences). 

After getting a bunch of scratch off dust all over my bedroom carpet, I ended up $20 poorer, and decided to calculate the expected value of each game I played. The [website](https://www.palottery.state.pa.us/Scratch-Offs/Active-Games.aspx) lists the chances of winning at all (usually around 1:3 to 1:5), then also has a pdf in each page that lists "Chances of Winning" for that game in particular. 

A brief aside, some lotteries will show your odds instead of chances. This is SIGNIFICANTLY different. Odds are wins:losses, instead of wins/(wins+losses), which in this case would change 1:3 to 1/4. 

<p class="caption">An example "Chances of Winning" pdf from a real active game in PA as of 2/4/21</p>
![An example "Chances of Winning" pdf from a real active game in PA as of 2/4/21]({{ url_for('static', filename = 'palotterychances.png')}})

PA Lottery offers scratch-offs that cost 1, 2, 3, 5, 10, 20, and 30 dollars. I took the most recent game of each value, and added up the expected values (prize amount * probability of winning prize). I know it doesn't generalize well since I'm only using one of each cost level, but YOU try to scrape a PDF with variable rows. Have fun with that. This data was collected on 2/3/21 from the [PA Lottery site](https://www.palottery.state.pa.us/Scratch-Offs/Active-Games.aspx).


<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;margin-left: auto; margin-right: auto;}
.tg td{border-color:white;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:white;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Scratch-Off Game</th>
    <th class="tg-0pky">Cost</th>
    <th class="tg-0pky">Expected Value</th>
    <th class="tg-0pky">Net Loss</th>
    <th class="tg-0pky">% Change</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">3 Mil Extra</td>
    <td class="tg-0pky">$30</td>
    <td class="tg-0pky">$23.10</td>
    <td class="tg-0pky">-$6.9</td>
    <td class="tg-0pky">-23%</td>
  </tr>
  <tr>
    <td class="tg-0pky">1 Mil Jack</td>
    <td class="tg-0pky">$20</td>
    <td class="tg-0pky">$15.01</td>
    <td class="tg-0pky">-$4.99</td>
    <td class="tg-0pky">-25%</td>
  </tr>
  <tr>
    <td class="tg-0pky">WIN WIN WIN</td>
    <td class="tg-0pky">$10</td>
    <td class="tg-0pky">$7.31</td>
    <td class="tg-0pky">-$2.69</td>
    <td class="tg-0pky">-26.9%</td>
  </tr>
  <tr>
    <td class="tg-0lax">Leprechaun</td>
    <td class="tg-0lax">$5</td>
    <td class="tg-0lax">$3.52</td>
    <td class="tg-0lax">-$1.48</td>
    <td class="tg-0lax">-29.6%</td>
  </tr>
  <tr>
    <td class="tg-0lax">Wild Cash</td>
    <td class="tg-0lax">$3</td>
    <td class="tg-0lax">$1.98</td>
    <td class="tg-0lax">-$1.02</td>
    <td class="tg-0lax">-34%</td>
  </tr>
  <tr>
    <td class="tg-0lax">O'Lucky Coin</td>
    <td class="tg-0lax">$2</td>
    <td class="tg-0lax">$1.31</td>
    <td class="tg-0lax">-$0.69</td>
    <td class="tg-0lax">-34.5%</td>
  </tr>
  <tr>
    <td class="tg-0lax">Clover All Over</td>
    <td class="tg-0lax">$1</td>
    <td class="tg-0lax">$0.71</td>
    <td class="tg-0lax">-$0.29</td>
    <td class="tg-0lax">-29%</td>
  </tr>
</tbody>
</table>

<br>

Results seem as expected, the more you pay, the less you lose proportionally, though not in raw cash. And, of course, house always wins. The calculated chances also reflect this, with the $30 dollar games offering the highest chances of winning anything. 

Weirdly enough, it seems that the loss from $1 games is the same as loss from $5 games, which makes you feel like you should buy 5x 1$ games instead of 1x 5$ game. Whatever gets you going, I guess. You lose money either way.




