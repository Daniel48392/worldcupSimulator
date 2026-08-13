# World Cup Simulator

## Overview
A Python simulation of a 210-team World Cup using a pure knockout format. Match outcomes are probabilistic and influenced by FIFA World Ranking points, allowing stronger teams to have a higher probability of winning while still allowing upsets.

## How it works
210 teams participate in the tournament and are randomly assigned opponents, then phase 1 of the knockout occurs resulting in 105 teams automatically qualifying to the next round. Phase 1 losers are then organised by FIFA World Ranking points the highest ranked 23 teams will re-enter the tournamnet to make a 128 team knockout for phase 2. Phase 2 then occurs knocking out half the competition and this repeats until stage 7 of the tournament. Stage 7 the winners will face eachother in the final and the losers will face eachother in the third place playoff. This then produces the top 4 teams.

## Probability calculation
Calculation: P(A) = 1 / (1 + 10^((RatingB - RatingA) / 400)) <br>
Code: odds = 1 / ( 1 + (10 ** ( (float(matchStats[1])-float(matchStats[0]))/400)) ) <br>
I use this calculation ELO equation that utilises fifa points rather than pure ranking, this is because pure order the gaps in skill between teams are not even, the difference between 200-201 is most likely not the same as 9-10 in the ranking. Therefore the use of fifa points gives a more accurate skill gap between teams therefore a more realistic probability of each teams chances of winning.

## Data
Team FIFA World Ranking points were obtained from [https://www.kaggle.com/datasets/lucasyukioimafuko/fifa-mens-world-ranking] and are used as the skill rating for each national team.
The rankings represent the data available at the time the project was created and may change over time.
A copy of the exact data set I used is stored in the project under the data directory

## Limitations
Fifa ranking points are the only measurement of team strength, therefore the simulation doesn't account for home field advantage, injuries, squad selection, tactics, mentality, ect...

## How to run
`git clone https://github.com/Daniel48392/worldcupSimulator.git` <br>
`cd worldcupSimulator` <br>
`python code/sim.py` <br>

## Example output
Winners: England <br>
Second: Netherlands <br>
Third: Brazil <br>
Fourth: Egypt
