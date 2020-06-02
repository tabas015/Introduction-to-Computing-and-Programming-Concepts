#Name - Fahia Tabassum

import random

#Problem A- Collatz
#==========================================================================
# Purpose:
#  making a sequence of numbers from n to 1 
# Input Parameter(s):
#   n = any positive single integer value.
# Return Value(s):
#   the list of numbers in the collatz sequence from n to 1, inclusive.
#==========================================================================

def collatz(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + collatz(n//2)
    else:
        return [n] + collatz(n*3+1) 


#Problem B- Finding the Minimum
#=======================================================================
# Purpose:
#  finding the minimum value from a list
# Input Parameter(s):
#   num_list = a list of integers 
# Return Value(s):
#   the minimum value in the list
#========================================================================

def find_min(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        min_val = num_list[0]
        min_num = find_min(num_list[1:])

        if min_num < min_val:
            min_val = min_num
        return min_val
                           

#Problem C. (Playing Tic-Tac-Toe Perfectly)        

#=====================================================================
# Purpose:
#   Determines whether a player has won tic-tac-toe, given the board
# Input Parameter(s):
#   board - a 9 element list representing the 9 spots on a tic-tac-toe board
# Return Value(s):
#   returns 'X' if X won the game
#   returns 'O' if O won the game
#   returns 'D' if the game has ended in a draw
#   returns '-' if no player has won and the game isn't over
#======================================================================
def winner(board):
    wins = [[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] == 'X':
            return 'X'
        if board[win[0]] == board[win[1]] == board[win[2]] == 'O':
            return 'O'
    if '-' in board:
        return '-'
    return 'D'

#=====================================================================
# Purpose:
#   Gets a list of all of the indexes of empty slots on a tic-tac-toe board
# Input Parameter(s):
#   board - a 9 element list representing the 9 spots on a tic-tac-toe board
# Return Value(s):
#   returns a list of integers, representing the indexes that are empty
#======================================================================
def open_slots(board):
    ret = []
    for i in range(len(board)):
        if board[i] == '-':
            ret.append(i)
    return ret

#======================================================================
# Purpose:
#   Prints out a tic-tac-toe board in standard 3x3 grid style
# Input Parameter(s):
#   board - a 9 element list representing the 9 spots on a tic-tac-toe board
# Return Value(s):
#   None
#=======================================================================
def display_board(board):
    for i in range(3):
        print(' '.join(board[3*i:3*i+3]))
    print()

#==========================================
# Purpose:
#   Plays a single game of tic-tac-toe, with random moves
# Input Parameter(s):
#   None
# Return Value(s):
#   'X' if X won the game
#   'O' if O won the game
#   'D' if the game ended in a draw
#==========================================
def tic_tac_toe():
    board = ['-']*9
    turn = 'X'
    while winner(board) == '-':
        slots = open_slots(board) 
        pick = random.choice(slots)
        
        if turn == 'X':
            board[pick] = 'X'
            turn = 'O'
        elif turn == 'O':
            min_state = 1
            min_ind = 0
            for i in open_slots(board):
                new_board = board[:]
                new_board[i] = 'O'
                a = force_win(new_board)
                if a < min_state :
                    min_state = a
                    min_ind = i
                turn = 'X'
            board[min_ind] = 'O'
    return winner(board)

#==========================================================
# Purpose:
#   Plays many games of tic-tac-toe, and prints out the results
# Input Parameter(s):
#   n - an integer representing the number of games to play
# Return Value(s):
#   None
#=============================================================
def play_games(n):
    winnars = []
    for i in range(n):
        game = tic_tac_toe()
        winnars.append(game)
    print("X wins:",winnars.count('X'))
    print("O wins:",winnars.count('O'))
    print("Draw:",winnars.count('D'))


# Purpose:
#   making a much better tic-tac-toe AI that never loses.
# Input Parameter(s):
#   board = a list representation of a tic-tac-toe board
# Return Value(s):
#   returns an integer that represents the current state of the board.
#========================================================================
def force_win(board):
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    elif winner(board) == 'D':
        return 0

    if len(open_slots(board))% 2 == 0:
        current_player = 'O'
    elif len(open_slots(board))% 2 !=0:
        current_player = 'X'

    a = []    
    for i in open_slots(board):
        new_board = board[:]
        new_board[i] = current_player
        a.append(force_win(new_board))
    if current_player == 'X':
        return max(a)
    else:
        return min(a)


    
    
