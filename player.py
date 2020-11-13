

class Player():

    def __init__(self, _id):
        self.name = self.getName()
        self.id = _id 

    def getName(self):
        user_inp = input('Player Name: ').strip()
        user_inp = self.nameValidation(user_inp) 
        return user_inp 

    def nameValidation(self, name):
        if len(name) < 3:
            name = input('Name must be at least 3 letters: ').strip()
            return self.nameValidation(name)
        else:
            return name

    def getMove(self):
        '''Ask 2 questions which row which column, validate that the
           response is in acceptable format'''
        row = input('Row [top/mid/bot]: ').strip().lower()
        column = input('Col [l/m/r]: ').strip().lower() 
        out = self.validateMove(row, column)
        return out

    def validateMove(self, row, column):
        '''Confirm row and column are formatted correctly
           if true then return them in expected format for Moves'''
        valid_row = ('top', 'mid', 'bot')
        valid_col = ('l','m','r')
        if row in valid_row and column in valid_col:
            return {row: column, 'player': self.id}
        else:
            print('invalid entry try again\n')
            return self.getMove() 

        
