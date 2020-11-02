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
        response = {'topRow':[], 
                    'midRow': [],
                    'botRow': []}
        for k,v in self.topRow.items():
            if v > 0:
                response['topRow'].append(k)
        for k,v in self.midRow.items():
            if v > 0:
                response['midRow'].append(k)
        for k,v in self.botRow.items():
            if v > 0:
                response['botRow'].append(k)
        return response

    def acceptMove(self, move):
        # move is a dict has key that matchtes class attr
        # but that doesn't really help us
        
        pass

    def validateMove(self, move):
        pass

