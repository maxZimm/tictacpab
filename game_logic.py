# Questions for this class
# Do you run automatically? Yes if you mean you don't have to instantiate me after sending me to python
# What do you do first? Create a player by askin for a name
# How many players? 2, perhaps just one and I'll play against you intead
# Who goes first? Good question, player1 for now
# What then? I ask player1 what move they would like to make
# How does p1 know whats a available? I show them the board, it'll be empty at this point
# How does p1 tell you there move? Good question, by typing in a format I'll recognize
# Whats the format? Still figuring it out, so it will need to be along the lines of ROW L|M|R (left middle right)
# perhaps TOP|MID|BOT asked first, then L|M|R asked second then the vars saved and combined internally
from player import Player
from moves import Moves
from board import Board

class GameLogic():
    """Class to control:
        * Player creation
        * Order in which players make moves
        * Send moves to board
        * Keep score and determine winners """

    def __init__(self):
        self.board = Board()
        self.moves = Moves()
        self.getPlayers()

    def startGame(self):
        # getPlayers
        # ask player_1 to make a move
        # accept player_1's move and validate that it is acceptable?
        # check if that move resulted in a win? This can't happen at the very least till 3 moves are made by a player
        # ask player_2 to make a move
        pass

    def getPlayers(self):
        print('Player 1')
        self.player_1 = Player(1) 
        print('Player 2')
        self.player_2 = Player(2) 

    def check_winner(self):
        rows = [self.check_row_win(row) for row in self.moves.state.keys()]
        cols = [self.check_col_win(col) for col in ['l','m','r']] 
        diag = self.check_diag_win()
        if diag is not None:
            return diag
        for item in rows:
            if item is not None:
                return item
        for item in cols:
            if item is not None:
                return item

    def check_row_win(self, row):
        cntr = list(self.moves.state[row].values())
        if cntr.count(1) == 3: 
            return 1
        elif cntr.count(2) == 3: 
            return 2

    def check_col_win(self, col):
        cntr = [self.moves.state[x][col] for x in self.moves.state.keys()]
        if cntr.count(1) == 3: 
            return 1
        elif cntr.count(2) == 3: 
            return 2

    def check_diag_win(self):
        cntr1 = [self.moves.state['top']['l'],self.moves.state['mid']['m'] ,self.moves.state['bot']['r'] ]
        cntr2 = [self.moves.state['top']['r'],self.moves.state['mid']['m'] ,self.moves.state['bot']['l'] ]
        if cntr1.count(1) == 3 or cntr2.count(1) == 3: 
            return 1
        elif cntr1.count(2) == 3 or cntr2.count(2) == 3: 
            return 2


