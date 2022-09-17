#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    
    def __init__(self, height, width):
        """ constructs a new Board object by initilizing attributes 
            height, width, and slots. 
            
            -Attributes-
            height: the number of rows in the board 
            width: number of columns
            slots: refers to 2D list with height rows and width cols
                   stores the current contents of the board. Each slot 
                   contains space ' ', 'X', or 'O'
        """ 
        self.height = height 
        self.width = width 
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        
        # line of dashes 
        s += '-' * (2 * (self.width) + 1)  # creates an odd # of '-' depending on board width
        s += '\n'
        
        # numbers that label each column
        s += ' ' # 1st character is a space
        numbers = '0123456789'
        
        for col in range(self.width):
            number = col % 10 # number must be in mod 10 
            s += numbers[number] # add appropriate number...
            s += ' ' # ...followed by a space

        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        
        row = 0 
        while self.slots[row][col] == ' ' and row < (self.height - 1): 
            row += 1 # keep going down until you reach a non-empty slot, or the bottom
        
        if self.slots[row][col] == ' ':  # if the col is empty, put a checker in it
            self.slots[row][col] = checker
        else: 
            self.slots[row - 1][col] = checker # if the col has something, put checker on top of what's there 

    ### add your reset method here ###
    
    def reset(self):
        """ reset the Board object on which it is called by setting all 
            slots to contain a space character.
        """ 
        # use the same code that creates the blank board again! 
        self.slots = [[' '] * self.width for row in range(self.height)]
        
        
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    
    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the 
            column col on the calling Board object. Otherwise, it 
            should return False.
        """
        # 1st condition: is col too low/high? Check if in valid range
        if col in range(self.width):  
            
            # 2nd condition: If 1st condition is true, is the top row empty? 
            if self.slots[0][col] == ' ':
                return True # all good to put checker there! 
            else:
                return False # No! col is full!
        
        else: 
            return False # No! col is too low/high
    
    
    def is_full(self):
        """ returns True if the called Board object is completely 
            full of checkers, and returns False otherwise.
        """
        
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False # if you can add to it, it isn't full 
        
        return True # if can't add to any col, it is full
        
    
    def remove_checker(self, col):
        """ removes the top checker from column col of the called 
            Board object. If the column is empty, then the method should do nothing. 
        """
        
        # reused code from add_checker to find the highest non-space entry in col
        row = 0 
        while self.slots[row][col] == ' ' and row < (self.height - 1): 
            row += 1 # keep going down until you reach a non-empty slot, or the bottom
        
        # whether it's an X or O, make it a space
        self.slots[row][col] = ' ' # if already space, this changes it to what it already is; no effect.
    
    # helper functions for is_win_for()
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                    self.slots[row][col + 2] == checker and \
                    self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                    self.slots[row + 2][col] == checker and\
                    self.slots[row + 3][col] == checker:
                    return True
                    
        return False
        
    
    def is_down_diagonal_win(self, checker):
        """ Checks for a down diagonal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                    self.slots[row + 2][col + 2] == checker and\
                    self.slots[row + 3][col + 3] == checker:
                    return True
                    
        return False
        
    
    def is_up_diagonal_win(self, checker):
        """ Checks for an up diagonal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row - 1][col + 1] == checker and \
                    self.slots[row - 2][col + 2] == checker and\
                    self.slots[row - 3][col + 3] == checker:
                    return True
                    
        return False
    
    def is_win_for(self, checker):
        """ returns True if there are four consecutive slots containing 
            checker on the board. Otherwise, it should return False.
            input:  a parameter checker that is either 'X' or 'O' 
        """
        assert(checker == 'X' or checker == 'O')
        # call the helper functions and use their return values to
        # determine whether to return True or False
        
        # checks each possible win, and if none of them are true, returns false
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False

        
    
    
    
    
    
