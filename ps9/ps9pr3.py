#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

def process_move(p, b):
    """ prints a message for whose turn it is, obtains and apply's player
        p's next move to board b, prints board b, and checks if the move 
        causes either a win or a tie.
        
        Returns True if it's a win or tie, returns False otherwise.
        
        input p is a Player object.
        input b is a Board object.
    """
    which_turn = str(p) + "'s turn"
    print(which_turn)
    
    next_move = p.next_move(b) # stores p's next move
    
    b.add_checker(p.checker, next_move) # applys this move to the board
    
    print()
    print(b)

    
    if b.is_win_for(p.checker): # check for a winning move
        print() #blank line to make it look like example
        print(p, 'wins in', p.num_moves, 'moves.')
        print('Congratulations!')
        return True
    
    elif b.is_full(): # if board is full and no one won, it's a tie
        print() #blank line to make it look like example 
        print("It's a tie!")
        return True
    
    else: 
        return False
    
class RandomPlayer(Player): 
    """ subclass of Player. Data type representing a computer player that 
        chooses at random from the available columns """
    
    def next_move(self, b):
        """ overrides next_move method inherited from Player. This version
            chooses at random among the available columns in Board b. 
            
            Returns the index of the randomly selected column.
            
            Input b: a Board object
        """ 
        available_columns = [col for col in range(b.width) if b.can_add_to(col) == True]
    
        random_move = random.choice(available_columns) 
        
        self.num_moves += 1
        
        return random_move
        
    
    