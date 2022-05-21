import random 

class Player:
    ''' 
    This is parent (base) class
    '''    
    def __init__(self, letter):
        self.letter = letter
        
    def get_move(self):
        pass
    
    
class HumanPlayer(Player):
    '''
    This is human player. It inherits Player base (parent) class 
    in order to use it's parent attributes and properties
    '''
    
    def __init__(self, letter):
        super().__init__(letter)
    
        
    def get_move(self, game):
        valid_square = False
        val = None
        
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val        

        
        
class RandomComputerPlayer(Player):
    '''
        This is computer player.
    '''
    
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

  
        