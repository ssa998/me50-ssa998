"""
Tic Tac Toe Player
"""

from ast import Return
from asyncio.windows_events import NULL
import copy
from hashlib import new
import math
from tkinter import E
from xml.dom.minidom import Element

from numpy import Infinity

X = "X"
O = "O"
EMPTY = None
winner = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    count = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                count += 1
    if count%2 == 0 :
        return O
    else: return X


        

    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    count = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possible.add((row,col))
    return possible




    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    if terminal(board):
        raise ValueError("game over!!")
    
    new_board = copy.deepcopy(board)
    new_board[action[0] ][action[1]]=player(board)
    return new_board
    raise NotImplementedError


def winner(board):
   
    """
    Returns the winner of the game, if there is one.
    """

    if board[0][0] == board[0][1] == board[0][2] and board[0][2] != EMPTY:
        if board[0][2]==X:
            return X
        else: return 
    elif board[1][0] == board[1][1] == board[1][2] and board[1][2] != EMPTY:
        if board[1][2]==X:
            return X
        else: return O
    elif board[2][0] == board[2][1] == board[2][2] and board[2][2] != EMPTY:
        if board[2][0]==X:
            return X
        else: return O
    
    elif board[0][0] == board[1][0] == board[2][0]  != EMPTY:
        if board[2][0]==X:
            return X
        else: return O
    elif board[0][1] == board[1][1] == board[2][1]  != EMPTY:
        if board[2][1]==X:
            return X
        else: return O
    elif board[0][2] == board[1][2] == board[2][2]  != EMPTY:
        if board[0][2]==X:
            return X
        else: return O
    elif board[0][0] == board[1][1] == board[2][2] != EMPTY:
        if board[0][2]==X:
            return X
        else: return O
    elif board[0][2] == board[1][1] == board[2][0]  != EMPTY:
        if board[0][2]==X:
            return X
        else: return O  
    else : return None
    raise NotImplementedError


def terminal(board):
    if winner(board) !=None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    
    
    return True

    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner == X:
        return 1
    elif winner == O :
        return -1
    else : return 0
    raise NotImplementedError



def minimax(board):
    if board == [[EMPTY]*3]*3:
        return (1,1)
    if player(board)==X:
        score = -1000
        best_move = None
        for action in actions(board):
            move = minValue(result (board,action))
            if move > score:
                score = move
                best_move = action
    if  player(board)==O:
        score = 1000
        best_move = None
        for action in actions(board):
            move = maxValue(result(board,action))
            if move < score:
                score = move
                best_move = action
    return best_move

def minValue(board):
    if terminal(board):
        return utility(board)
    score = 1000
    for action in actions(board):
        score = min ( score, minValue(result(board,action)))

        return score
def maxValue(board):
    if terminal(board):
        return utility(board)
    score =-1000
    for action in actions(board):
        score =max (score, maxValue(result(board,action)))

    return score 
  