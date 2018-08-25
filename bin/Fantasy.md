# Fantasy Draft Script

## Usage

You must have [Python 3](https://www.python.org/downloads/), [pandas](https://pandas.pydata.org/pandas-docs/stable/install.html), and [numpy](https://scipy.org/install.html) installed.  

You must also have your data saved as a CSV from http://apps.fantasyfootballanalytics.net/projections/, where you can use their standard
projections or enter your league's settings to get more accurate results for your draft. If you create your own CSV you will need columns with headers: player, position, team, adp, and points

In the command line enter:  
```./fantasy-draft [league_size] [team_size] [data_file]``` where:
* league_size is the number of teams in your league
* team_size is the number of players on each team
* data_file is the CSV file with the projections

You will then be prompted with options: remove, adjust, draft, display, search, load, help and exit

### Remove
```remove [Player Name]``` or ```r [Player Name]```  
The name must be exactly as it is in the data, with proper capitalization. For defense's with only one word in the name you must add a space after name. The player will then be removed and will no longer show up in the "draft" or "display" commands
Note: Currently doesn't support players with the exact same name

### Adjust
```adjust [position] [multiplier]``` or ```a [position] [multiplier]```  
The position must be one of QB, RB, WR, TE, DST, or K. The VBD of all the players with the given position will be multiplied by the
multiplier and the players are resorted to reflect the change.

Sample Multiplier Matrix:

| Have            | Start 1 | Start 2 | Start 3 | Start 4 | Start 5+ |
|-----------------|---------|---------|---------|---------|----------|
| 0 of a position | 1.0     | 1.0     | 1.0     | 1.0     | 1.0      |
| 1 of a position | 0.8     | 1.0     | 1.0     | 1.0     | 1.0      |
| 2 of a position | 0.6     | 0.8     | 1.0     | 1.0     | 1.0      |
| 3 of a position | 0.4     | 0.6     | 0.8     | 1.0     | 1.0      |
| 4 of a position | 0.2     | 0.4     | 0.6     | 0.8     | 1.0      |

https://www.footballguys.com/05vbdrevisited.htm

### Draft
```draft [position]``` or ```dr [position]```  
The position must be one of ANY, QB, RB, WR, TE, DST, or K. You will be given the best available player (assuming you are removing players)
based on VBD

### Display
```display [position]``` or ```di [position]```  
The position must be one of ALL, QB, RB, WR, TE, DST, or K. You will be given the 10 best available players (assuming you are removing players)
based on VBD

### Search
```search [Player Name]``` or ```s [Player Name]```  
The name must be exactly as it is in the data, with proper capitalization. For defense's with only one word in the name you must add a space after name. You be given the average draft position, projected points, and VBD of the player.

### Load
```load [file]``` or ```l [file]```  
The file specified should either be original.csv or updated.csv, which are both outputted by this program. From this point the program will use the data that is in the file.

### Help
```help``` or ```h```  
The usage for this program will be printed

### Exit
```exit``` or ```e```  
The program will stop running

### Output
The program produces two files, "original.csv" and "updated.csv". original.csv is a condensed version of the original input file with a column for VBD.
updated.csv is the same as original.csv but is updated every time you remove a player.
