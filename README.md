## Store Baduk
A repository with experimental methods for hashing a game of Go/Baduk/Weiqi to allow for pattern based search. 

## Project Description 
The inspiriation for this project was the waltheri Go database (http://ps.waltheri.net/), as it's something I played around with when I first started playing the game. Nowadays the site is rarely updated with any games, and since the project is not open source the methods it uses to create the database is unclear. 

Although a platform and an inteface for this project undecided as of now, the infastructure can be built using any of the algorithms and data storage methods outlined below and may have interesting applications in hashing matrix data.

## Methods and theory 
When starting the project, the first thought which came to my mind was simply to store each game as a string of some sort and filter when querying for games. This would be quite easy as the game and move notation in Go is standardized, where each intersection on the 19x19 board can be represented by two letters. 

<picture of go board with alphabetic coordinates>

And thus a game could be a represented by a string of all the moves played in it. However there are two big flaws with this implementation, and the biggest hurdle for any potential implementation, is that symmetry and transposition are unaccounted for. Let's address them one at a time. 

Symmtery is fairly self-explanatory. Suppose you have two games that consist of just one move. 

<two pictures of opposite star points>

The game strings would be "bb" and "aa", for pictures 1 and 2 respectively. And let's say all games starting with move "aa" were queryed. In this scenario, the game with string "bb" would be discluded, despite the fact that it is an isomorphism to "aa", the perspective of the board is just different. 

And because of this, one might say that each position has 3 additional counterparts (because you can rotate a board 3 times) however you also have to take into account boards which are "flipped upside down". 

<picture of two boards, one with stone at 16-15, the other with a stone at 4-15>
    
So in total each position has 7 possible "transformations".
    
Transpostion refers to the idea that a different order of moves can lead to the same position. For instance the position below can be reached with either sequence as labeled. 
<transposition example>

My first intuition for solving the issue of transposition was to simply hash each move to where it was on the board. Meaning that the board would be represented by a 19 by 19 array, storing values 1 through 361. And each position could be iterated through as such:

n = 19
p = (alternates between 363 and 373)
hash = 0
for i=1..n
  for j=1..n
    hash=p*hash+A[i][j]
    
Resulting in a unique hash for each possible position. The reason why prime number "p" has to alternate between two prime numbers is that a black move on a square cannot be hashed the same why a white move can on a square, otherwise positions such as the ones below, would be treated as the same.
<Two polar opposite positions>
    
The larger question is how to solve 
    
    
    
