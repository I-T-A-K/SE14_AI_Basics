"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    # Checking for plays
    count_X, count_O = 0, 0
    
    # Checking the Board and incremeting the plays
    for rows in board:
        for cell in rows:
            if cell == X:
                count_X += 1
            elif cell == O:
                count_O += 1
                
    # Checking player´s turn
    if not terminal(board) and count_X == count_O:
        return X
    elif count_X > count_O:
        return O
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    # Creating set of the available places
    places = set()
    
    # Checking available places
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                places.add((i, j))
    return places            
    
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    # Checking if action is valid
    if action not in actions(board):
        raise ValueError("Invalid action.")
    #elif terminal(board):
        #raise ValueError("Game over.")
    
    modified_board = copy.deepcopy(board)
    
    # Updating board state
    modified_board[action[0]][action[1]] = player(board)
    return modified_board
    
    #raise NotImplementedError

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Checking board cells
    if board[0][0] == board[0][1] == board[0][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[1][0] == board[1][1] == board[1][2] != None:
        if board[1][0] == X:
            return X
        else:
            return O
    elif board[2][0] == board[2][1] == board[2][2] != None:
        if board[2][0] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][0] == board[2][0] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][1] == board[1][1] == board[2][1] != None:
        if board[0][1] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][2] == board[2][2] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][1] == board[2][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][1] == board[2][0] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    else:
        return None
            
    # raise NotImplementedError

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    # Checking for winner
    if winner(board) != None:
        return True
    
    # Checking cells are filled
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

    #raise NotImplementedError

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    # Returning who is the winner
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else: 
        return 0
    # raise NotImplementedError

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if empty board is provided a input, return corner
    if board == [[EMPTY]*3]*3:
        return (0, 0)
      #  
    if player(board) == X:
        v = float("-inf")
        selected_action = None
        for action in actions(board):
            minValueResult = minValue(result(board, action))
            if minValueResult > v:
                v = minValueResult
                selected_action = action
    elif player(board) == O:
        v = float("inf")
        selected_action = None
        for action in actions(board):
            maxValueResult = maxValue(result(board, action))
            if maxValueResult < v:
                v = maxValueResult
                selected_action = action
    return selected_action
                
    # raise NotImplementedError
#    
def maxValue(board):
    """
    Returns minimum Value for the 
    """
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v

def minValue(board):
    """
    Returns maximum Value for the 
    """
    
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v
