# Questions for this class
# Do you collect the user input? Not sure, maybe not
# Should the user class collect the input, we could pass the move instance to
# the user method so they know available moves
# What do you need to know to take in a move? A row and a position
# RED GREEN REFACTOR is our mantra now 

class Moves():
    """Object to hold state of moves made and ones that are available. 
       There would be one instance of this class per game. Game Logic will
       prompt players to submit their move and then logic will send that move
       to this class which will verify it, and either update the state or send 
       error message to Game Logic instance"""

    def __init__(self):
        self.state = {'top':{'l':0,'m':0,'r':0},
                      'mid':{'l':0,'m':0,'r':0},
                      'bot':{'l':0,'m':0,'r':0}}

    def showAvailMoves(self):
        response = {'topRow':[], 
                    'midRow': [],
                    'botRow': []}
        for k,v in self.state['top'].items():
            if v == 0:
                response['topRow'].append(k)
        for k,v in self.state['mid'].items():
            if v == 0:
                response['midRow'].append(k)
        for k,v in self.state['bot'].items():
            if v == 0:
                response['botRow'].append(k)
        return response

    def acceptMove(self, move):
        '''accepts a move which is dict with key for row and player.
           move value is 1 of l,m,r and player is value of 1 or 2'''
        if 'top' in move.keys():
            if self.state['top'][move['top']] == 0:
                self.state['top'][move['top']] = move['player'] 
            else:
                raise InputError('move is already taken')

        if 'mid' in move.keys():
            if self.state['mid'][move['mid']] == 0:
                self.state['mid'][move['mid']] = move['player'] 
            else:
                raise InputError('move is already taken')
        if 'bot' in move.keys():
            if self.state['bot'][move['bot']] == 0:
                self.state['bot'][move['bot']] = move['player'] 
            else:
                raise InputError('move is already taken')

class InputError(Exception):
    """Class to raise error when unacceptable moves are submitted"""
    def __init__(self, message):
        self.message = message
