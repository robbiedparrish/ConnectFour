#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ subclass of Player. This is a data type for a 
        computer player that checks the best options for 
        connect 4 moves, and picks the best move for leading
        it towards victory. 
    """ 
    
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object. Checks for valid inputs,
            and initializes the attributes checker, tiebreak, and lookahead.
            
            checker: a one-character string that represents 
                     the gamepiece for the player
            tiebreak: if there are multiple best-moves, tiebreak decides 
                     which best-move to pick (leftmost, rightmost, or any random one).
            lookahead: the number of future moves AIPlayer takes into account
                     before it makes a move on its turn. 
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        #self.num_moves = 0
        
    def __repr__(self): 
        """ returns a string representing an AIPlayer object that 
            overrides the __reper__ inherited from Player
        """
        added_part = ' (' + self.tiebreak + ', '+  str(self.lookahead) + ')'
        
        s = str(super().__repr__()) + added_part
        return s
    
    
    def max_score_column(self, scores):
        """ returns the index of the column with the maximum score. Applies 
            tiebreak if there's more than one max. 
            
            input scores: a list containing a score for each column of the board.
        """
        max_score = max(scores)
       
        max_list = [] 
        for col in range(len(scores)): # creates list of indices 
            if scores[col] == max_score: # if the given list's element equals the max...
                max_list += [col] # ...then add it to the list!
        
        if self.tiebreak == 'LEFT':
            return max_list[0] 
        
        elif self.tiebreak == 'RIGHT':
            return max_list[-1]
        
        else: # last choice is random
            return random.choice(max_list)
        
    
    def scores_for(self, b):
        """ determines the called AIPlayer's scores for the columns in b. Returns 
            a list with the scores for each column
        
            input b: a Board object.
        """
        scores = [50] * b.width # creates big enough list 
        
        for col in range(b.width):
            if b.can_add_to(col) == False: 
                scores[col] = -1 # if column full, -1, can't go there 
           
            elif b.is_win_for(self.checker):
                scores[col] = 100
                #print('win')
            
            elif b.is_win_for(self.opponent_checker()):
                scores[col] = 0
                #print('loss')
                
            elif self.lookahead == 0: #be careful of this if/elif and the item assignment!
                scores[col] = 50
                #print('tie')
            
            else: 
                b.add_checker(self.checker, col)
               
                #if col > 1 and col < 5: 
                    #print(b)
                                             
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                
                opp_scores = opponent.scores_for(b) # recursive call, see what opponent thinks 
                
                if max(opp_scores) == 0: # if this move makes opponent lose, it makes me win!
                    scores[col] = 100 
                  
                    
                elif max(opp_scores) == 50: # opponent would win, so I would lose
                    scores[col] = 50
                   
                    
                else:    # max(opp_scores) == 100:
                    scores[col] = 0
            
                b.remove_checker(col) 
            
        return scores
    
    
    def next_move(self, b):
        """ overrides inherited next_move method. Returns the called AIPlayer's judgment
            of the best possible move. Increments num_moves. 
            
            input b: a Board object.
        """
        
        best_move = self.max_score_column(self.scores_for(b)) # picks best move from its choices
        self.num_moves += 1
        
        return best_move
    

    
    
    
    
    
    