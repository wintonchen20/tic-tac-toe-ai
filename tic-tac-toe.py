import math

def print_board(board:[str]) -> None:
    """
    Parameters:
        - board : 9 x 1 array containing the current game state
    
    Prints a visualization of the game board    
    """
    print("{zero} | {one} | {two}".format(zero=board[0],one=board[1],two=board[2]))
    print("---------")
    print("{three} | {four} | {five}".format(three=board[3],four=board[4],five=board[5]))
    print("----------")
    print("{six} | {seven} | {eight}".format(six=board[6],seven=board[7],eight=board[8]))

def minimax(board:[str], depth:int, is_max_player:bool) -> int:
    """
    Parameters:
        - board : 9 x 1 array containing the current game state
        - depth: a int determining how far down the game tree it should look
        - is_max_player: a bool determining whether the it should find the max value possible or min value possible

    Returns:
        - int : return the best value possible depending if it is the maximizing player
    """

    
    if check_gameboard(board) == user_symbol:
        return -10
    elif check_gameboard(board) == ai_symbol:
        return 10
    elif check_gameboard(board) == "tie":
        return 0

    #List containing all of the available positions within the board
    free_moves = [index for index in range(0,9) if board[index] == -1]
    
    if is_max_player :
        bestVal = -math.inf
        #Iterates through the list of free positions 
        for move in free_moves :
            #Creates a copy of the board and inserts the new position and passes it to the minmax function
            new_board = board.copy()
            #Inserts the ai symbol into the board
            new_board[move] = ai_symbol
            value = minimax(new_board, depth+1, False)
            bestVal = max( bestVal, value) 
        return bestVal

    else :
        bestVal = math.inf 
        for move in free_moves:
            #Creates a copy of the board and inserts the new position and passes it to the minmax function
            new_board = board.copy()
            #Inserts the ai symbol into the board
            new_board[move] = user_symbol
            value = minimax(new_board, depth+1, True)
            bestVal = min( bestVal, value) 
        return bestVal
        
def find_bestmove(board:[str]) -> (int, int):
    """
    Parameters:
        - board : 9 x 1 array containing the current game state

    Returns:
        - (int, int) : containing the best move the ai is able to make
    """
    best_move = -1
    #List containing all of the available positions within the board
    free_moves = [index for index in range(0,9) if board[index] == -1]

    for move in free_moves:
        #Creates a copy of the board and inserts the new position and passes it to the minmax function
        new_board = board.copy()
        new_board[move] = ai_symbol
        if minimax(new_board, 0, False) > best_move:
            best_move = move
    
    return best_move

def user_input(user_input:int):
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
    
    #ERROR CHECK: If the move is out of bounds
    if user_input not in range(0,9):
        return False

    #ERROR CHECK: If the move that the user wants to make is already filled
    if gameboard[user_input] == -1:
        return False
    
    #If there are not errors, update the gameboard and return True
    gameboard[user_input] = user_symbol
    
def check_gameboard( board:[str] ) -> str:
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
    symbols = [user_symbol, ai_symbol]

    for symbol in symbols:
        #Checks the first three rows
        if board[0:3].count(symbol) == 3:
            return symbol
        if board[3:6].count(symbol) == 3:
            return symbol
        if board[6:9].count(symbol) == 3:
            return symbol
        
        #Checks the first three columns
        if [board[0],board[3],board[6]].count(symbol) == 3:
            return symbol
        if [board[1],board[4],board[7]].count(symbol) == 3:
            return symbol
        if [board[2],board[5],board[8]].count(symbol) == 3:
            return symbol

        #Checks the two diagonals
        # \
        backslash = [board[0],board[4],board[8]]
        # /
        slash = [board[2],board[4],board[6]]
        if backslash.count(symbol) == 3 or slash.count(symbol) == 3:
            return symbol
    
    #Checks for a tie
    if board.count(-1) == 0:
        return "tie"
    
    #If none of the winning/ tie conditions are met, return False
    return False

def restart():
    """
    Clears out the board and restarts the game
    """
    gameboard = [-1,-1,-1, -1,-1,-1, -1,-1,-1]

    #This is set to default, None 
    #It will change depending on if the user wants to make the first move or not
    user_symbol = None
    ai_symbol = None

if __name__ == "__main__":
    running = True
    user_symbol = "O"
    ai_symbol = "X"

    #The gameboard is flattened to a 1d array for easier processing
    gameboard = [-1,-1,-1, -1,-1,-1, -1,-1,-1]
    
    """
    #This is set to default, None 
    #It will change depending on if the user wants to make the first move or not
    user_symbol = None
    ai_symbol = None
    """


    while running:
        print_board(gameboard)
        user_input = input("What is your input: ")
        gameboard[int(user_input)] = user_symbol
        if check_gameboard(gameboard) != False:
            print_board(gameboard)
            print("This player has won {0}".format(check_gameboard(gameboard)))
            running = False
        print_board(gameboard)
        ai_move =  find_bestmove(gameboard)
        print("This is the ai's move: ", ai_move)
        gameboard[ai_move] = ai_symbol
        if check_gameboard(gameboard) != False:
            print_board(gameboard)
            print("This player has won {0}".format(check_gameboard(gameboard)))
            running = False