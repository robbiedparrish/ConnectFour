#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player:
    """ a data type that represents a player of the 
        Connect Four game"""
        
    def __init__(self, checker):
        """ constructs a new Player object by initializing 
            the following two attributes: 
                
            checker: a one-character string that represents 
                     the gamepiece for the player
                     
            num_moves: an integer storing the number of moves 
                       a player has made so far (starts at 0)
        """
        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker 
        self.num_moves = 0
        
        
    def __repr__(self):
        """ returns a string representation of a Player object
            that indicates which checker the Player object is using.
        """
        string = 'Player '
        string += self.checker
        
        return string
    
    def opponent_checker(self):
        """ returns one-character string representing the checker of 
            the Player object's opponent. X's foe is O, O's foe is X.
            Assume no other possible checkers besides X and O.
        """
        
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self, b):
        """ asks user to enter a column number representing where the user 
            wants to place a checker on the board. Returns the column where
            the player wants to make the next move (if the entry is valid) and
            increments the number of moves Player has made. 
            
            input b: a Board object 
        """
        
        self.num_moves += 1 
        
        while True:
            col = int(input('Enter a column: '))
            
            if b.can_add_to(col) == True:
                break
            
            print('Try again!')
            
        return col 
        
        
        
    
