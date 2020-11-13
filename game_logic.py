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
        # maybe this should just hold a call to getPlayers or another method to kick off game loop
        self.board = Board()
        self.moves = Moves()
        self.getPlayers()

    def startGame(self):
        pass

    def getPlayers(self):
        print('Player 1')
        self.player_1 = Player(1) 
        print('Player 2')
        self.player_2 = Player(2) 


        
