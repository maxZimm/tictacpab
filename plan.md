TIC TAC TOE Game
================

Game includes:
* a board to place moves on
** A board has a set number of places to hold a player move
** A players move is represented by either an X or an O on the board, all moves by a player are the same symbol
** A board should accept moves as input? And display them correctly
* at least one player
** if only one player created; The game will generate an opponent
** A player can create a move
** A move can only occupy an unselected space on the board
** A player can only make 1 move at a time before another player chooses
* Score Tracker, to record most wins by any player
** not part of MVP
* Game Logic
** Administers which player is making moves
** Those moves being sent to board
** Moves are valid
** Determines winner
* Moves
** Hold state of available moves on the board
** Accept a players move
** Validate whether a players move is acceptable
** Send players move to board?

Empty Board
_|_|_
_|_|_
 | |

1 Space occupied
_|_|_
_|X|_
 | | 

2 Moves placed
_|O|_
_|X|_
 | |

Winning moves
X|O|O
_|X|_
 | |X

_/__
I think a dictionary type for available board spaces is a way to pass
state of game between players game logic and the board

board = {'top':{'L': None, 'M': None, 'R': None}, 
         'mid':{'etc..' 

Or should I make a board moves class that can be passed between board player and game logic?

Idea for improvement
Makea an I/O class for the game that all the other class send their messages to
1 place to hold all that work instead of sneaking it into a bunch of different methods

cool thing with that would be making it possible to switch between pyqt and cli 

Other idea is figuring out how to play against the computer. Maybe pick at random if there is a shuffle like
method for lists. So put the remaining available rows in a list and then the columns, no that won't work
Generate all possible moves left, put that in a list, get the length of it and pick a random number from 0 to that length
Use that as index in list of moves and send to board.
