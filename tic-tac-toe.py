class ai():
    def __init__(self):
        pass

class game():
    def __init__(self):

        self.gameboard = [
            [-1,-1,-1],
            [-1,-1,-1],
            [-1,-1,-1],
        ]

        #This is set to default, None 
        #It will change depending on if the user wants to make the first move or not
        self.user_symbol = None
        self.ai_symbol = None

        #A variable to check the number of available cells left
        self.num_freespots = 9

    def input(self, user_input:(int,int) ) -> bool:
        """

        Parameters:
            - user_input : 2-d tuple containing the coordinates of their move

        Returns:
            - bool : If the move was valid 

        This function takes in a user-input with some error checking
        and based off of that, will return a boolean.
            1. True - user_input was valid and now the AI will make its move
            2. False - user_input was invalid
                2a. user_input may be out of bounds
                2b. user_input may have made a selection that was already filled
        """

        #Variables holding the coordinates of the user's move
        x, y = user_input
        
        #ERROR CHECK: If the move is out of bounds
        if x not in range(0,3) or y not in range(0,3):
            return False

        #ERROR CHECK: If the move that the user wants to make is already filled
        if self.gameboard[x][y] == -1:
            return False
        
        #If there are not errors, update the gameboard and return True
        self.gameboard[x][y] = self.user_symbol
    
    def check_gameboard(self, symbol:str) -> bool:
        """

        Parameters:
            - symbol : Either an 'X' or 'O' depending on who made the last move

        Returns:
            - bool : The user who made the previous move has won or the game state is a tie

        This function will automatically be called after every move.
        It will check for two conditions:
            1. If there is a winning game state
            2. If the board is filled and the game is a tie
        
        There are only 8 available ways to win, so all of those winning conditions will just be hardcoded
            -First three rows, first three columns, and the two diagonals 
        """

        #Checks the first three rows
        for row in self.gameboard:
            if row.count(symbol) == 3:
                print("Player {s} has won".format(s=symbol))
                return True
        
        #Checks the first three columns
        for column in range(3):
            column_to_be_checked = [self.gameboard[0][column],self.gameboard[1][column],self.gameboard[2][column]]
            if column_to_be_checked.count(symbol) == 3:
                print("Player {s} has won".format(s=symbol))
                return True

        #Checks the two diagonals
        # \
        backslash = [self.gameboard[0][0],self.gameboard[1][1],self.gameboard[2][2]]
        # /
        slash = [self.gameboard[0][2],self.gameboard[1][1],self.gameboard[2][0]]
        if backslash.count(symbol) == 3 or slash.count(symbol) == 3:
            print("Player {s} has won".format(s=symbol))
            return True
        
        #Checks for a tie
        if self.num_freespots == 0:
            print("The board has resulted in a tie")
            return True
        
        #If none of the winning/ tie conditions are met, return False
        return False






    def restart(self):
        """
        Clears out the board and restarts the game
        """
        self.gameboard = [
            [-1,-1,-1],
            [-1,-1,-1],
            [-1,-1,-1],
        ]

        self.num_freespots = 9

        self.run()
    
    def run(self):
        """

        """
        pass

if __name__ == "__main__":
