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
        # this is ugly should find a better way
        # check across a row
        if self.moves.topRow['l'] == self.moves.topRow['m'] and  self.moves.topRow['l'] == self.moves.topRow['r']:
            return self.moves.topRow['l'] 
        if self.moves.midRow['l'] == self.moves.midRow['m'] and  self.moves.midRow['l'] == self.moves.midRow['r']:
            return self.moves.midRow['l'] 
        if self.moves.botRow['l'] == self.moves.botRow['m'] and  self.moves.botRow['l'] == self.moves.botRow['r']:
            return self.moves.botRow['l'] 
        # check across column
        if self.moves.topRow['l'] == self.moves.botRow['l'] and  self.moves.midRow['l'] == self.moves.botRow['l']:
            return self.moves.botRow['l'] 
        if self.moves.topRow['m'] == self.moves.botRow['m'] and  self.moves.midRow['m'] == self.moves.botRow['m']:
            return self.moves.botRow['m'] 
        if self.moves.topRow['r'] == self.moves.botRow['r'] and  self.moves.midRow['r'] == self.moves.botRow['r']:
            return self.moves.botRow['r'] 
        # then 2 diagonals 
        if self.moves.topRow['l'] == self.moves.botRow['r'] and  self.moves.midRow['m'] == self.moves.botRow['r']:
            return self.moves.botRow['r'] 
        if self.moves.topRow['r'] == self.moves.botRow['l'] and  self.moves.midRow['m'] == self.moves.botRow['l']:
            return self.moves.botRow['l'] 



