

class Player():

    def __init__(self):
        self.name = self.getName()

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
