# Questions for this class
# Do you collect the user input? Not sure, maybe not
# What do you need to know to take in a move? A row and a position
# 

class Moves():
    """Object to hold state of moves made and ones that are available"""

    def __init__(self):
        self.topRow = {'l':0,'m':0,'r':0}
        self.midRow = {'l':0,'m':0,'r':0}
        self.botRow = {'l':0,'m':0,'r':0}

    def showAvailMoves(self):
        pass

    def acceptMove(self, move):
        pass

    def validateMove(self, move):
        pass
