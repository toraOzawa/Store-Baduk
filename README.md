## Store Baduk
A repository with experimental methods for hashing a game of Go/Baduk/Weiqi to allow for pattern based search. 

## Project Description 
The inspiriation for this project was the waltheri Go database (http://ps.waltheri.net/), as it's something I played around with when I first started playing the game. Nowadays the site is rarely updated with any games, and since the project is not open source the methods it uses to create the database is unclear. 

Although a platform and an inteface for this project undecided as of now, the infastructure can be built using any of the algorithms and data storage methods outlined below and may have interesting applications in hashing matrix data.

## Methods and theory 
When starting the project, the first thought which came to my mind was simply to store each game as a string of some sort and filter when querying for games. This would be quite easy as the game and move notation in Go is standardized, where each intersection on the 19x19 board can be represented by two letters. 

*picture of go board with alphabetic coordinates*

And thus a game could be a represented by a string of all the moves played in it. However the biggest flaw with this implementation, and the biggest hurdle for any potential implementation, is the fact that symmetry is unaccounted for. 

Suppose you have two games that consist of just one move. 

*two pictures of opposite star points* 

The game strings would be "bb" and "aa", for pictures 1 and 2 respectively. And let's say all games starting with move "aa" were queryed. In this scenario, the game with string "bb" would be discluded, despite the fact that it is identical to "aa", the perspective of the board is just different. 
    
    
