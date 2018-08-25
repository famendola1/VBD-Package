# Fantasy Football Value Based Drafting
Last Updated: 8/25/2018

## [What is Value Based Drafting (VBD)?](https://www.fantasypros.com/2017/06/what-is-value-based-drafting/)
If the goal were just to find the highest scoring players every year, you would draft a team full of quarterbacks—they were 23 of the top 30 in fantasy points last year. Obviously, no league is set up this way.

In most leagues, you can only start one quarterback, so the key question becomes how much better your quarterback is than your opponent’s. And how much better your two running backs are than your opponent’s running backs. And so on.

Enter VBD. In short, the idea is that a player’s value isn’t based on how many total points he scores. Rather, it is based on how much more he scores than the “baseline” player at his position. VBD encapsulates a number of different ways to set that baseline, but for our purposes, there are three types of VBD:

* Value Over Replacement Player (VORP): How much better is [insert RB] than the best running back available on waivers?
* Value Over Last Starter (VOLS): How much better is [insert RB] than the last starting running back?  
* Value Over Next Available (VONA): How much better is [insert RB] than the best running back available at your next pick?

VBD isn’t perfect. It relies on generating accurate player projections and choosing the correct baseline, both Herculean tasks (if Hercules was an Excel nerd). And even the best projections can’t account for the unpredictability of an NFL season.

VBD also leaves out a lot of the nuance required to build a balanced team, and mostly ignores ADP in calculating “value.” VBD is a useful concept despite these flaws. It serves as just one of many ways you should be preparing for your draft.

## [Calculating VBD using VORP](https://www.fantasypros.com/2017/06/what-is-value-based-drafting/)
You generate VBD rankings by creating projections for every player, setting a baseline at each position, then calculating the difference between the two for each player.

For example, [insert RB] is projected to score 289.8 fantasy points. A standard 12 team league has 180 players drafted, and [the consensus ADP](https://www.fantasypros.com/nfl/adp/qb.php) shows X running backs being drafted in the top 180. That makes the (X+1)th running back, [insert RB] and his projected 67.1 fantasy points, the baseline for running backs using a VORP calculation. [first RB]’s VORP—his projected points minus [second RB]’s projected points—ends up a whopping 222.7.

## Installation 
```shell  
$ pip install vbd  
```

## Usage
```python  
from vbd import VBD

data = VBD(num_of_teams, num_players_per_team, data_file)
```
``` data_file ``` should be a CSV downloaded from http://apps.fantasyfootballanalytics.net/projections/, where you can use their standard projections or enter your league's settings to get more accurate results for your draft. If you create your own CSV you will need columns with headers: player, position, team, adp, and points.

### Remove
Remove a player from the dataset
```python
data.remove("player_name")
```

### Draft
Get the best player at a given position
```python
data.draft(position) # position is one of [QB, RB, WR, TE, DST, K, ANY]
```

### Top
Get the top n players at a given position
```python
data.top(n, position) # position is one of [QB, RB, WR, TE, DST, K, ALL]
```

### Search
Search for a player in the dataset
```python
data.search("player_name")
```

### Adjust
Adjust the VBD values for a position by a certain multiplier
```python
data.adjust(position, multiplier) # position is one of [QB, RB, WR, TE, DST, K]
```

### Load
Load a data file
```python
data.load("filename")
```

### Save
Save to a file
```python
data.save("filename")
```
