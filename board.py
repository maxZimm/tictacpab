
class Board():

    def __init__(self):
        self.p1 = 'X'
        self.p2 = 'O'

    def printBoard(self, moves):
        self.topRow(moves.topRow['l'],moves.topRow['m'],moves.topRow['r'])
        self.middleRow(moves.midRow['l'],moves.midRow['m'],moves.midRow['r'])
        self.bottomRow(moves.botRow['l'],moves.botRow['m'],moves.botRow['r'])

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
