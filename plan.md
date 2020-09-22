TIC TAC TOE Game
================

Game includes:
* a board to place moves on
** A board has a set number of places to hold a player move
** A players move is represented by either an X or an O on the board, all moves by a player are the same symbol
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


