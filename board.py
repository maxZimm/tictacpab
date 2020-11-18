
class Board():

    def __init__(self):
        self.p1 = 'X'
        self.p2 = 'O'

    def printBoard(self, moves):
        self.topRow(moves.state['top']['l'],moves.state['top']['m'],moves.state['top']['r'])
        self.middleRow(moves.state['mid']['l'],moves.state['mid']['m'],moves.state['mid']['r'])
        self.bottomRow(moves.state['bot']['l'],moves.state['bot']['m'],moves.state['bot']['r'])

    def topRow(self,l=0, m=0, r=0):
        print( f'{self.playerMove(l)}|{self.playerMove(m)}|{self.playerMove(r)}')

    def middleRow(self,l=0, m=0, r=0):
        print( f'{self.playerMove(l)}|{self.playerMove(m)}|{self.playerMove(r)}')

    def bottomRow(self,l=0, m=0, r=0):
        print( f'{self.playerMoveBrow(l)}|{self.playerMoveBrow(m)}|{self.playerMoveBrow(r)}')

    def playerMove(self,num):
        if num == 1:
            return self.p1
        elif num == 2:
            return self.p2
        else:
            return '_'

    def playerMoveBrow(self, num):
        return self.playerMove(num) if num > 0 else ' '
