import random

#==========================================
# Purpose:
#   Determines whether a player has won tic-tac-toe, given the board
# Input Parameter(s):
#   board - a 9 element list representing the 9 spots on a tic-tac-toe board
# Return Value(s):
#   returns 'X' if X won the game
#   returns 'O' if O won the game
#   returns 'D' if the game has ended in a draw
#   returns '-' if no player has won and the game isn't over
#==========================================
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


#==========================================
# Purpose:
#   Gets a list of all of the indexes of empty slots on a tic-tac-toe board
# Input Parameter(s):
#   board - a 9 element list representing the 9 spots on a tic-tac-toe board
# Return Value(s):
#   returns a list of integers, representing the indexes that are empty
#==========================================
def open_slots(board):
    ret = []
    for i in range(len(board)):
        if board[i] == '-':
            ret.append(i)
    return ret

#==========================================
# Purpose:
#   Prints out a tic-tac-toe board in standard 3x3 grid style
# Input Parameter(s):
#   board - a 9 element list representing the 9 spots on a tic-tac-toe board
# Return Value(s):
#   None
#==========================================
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
            board[pick] = 'O'
            turn = 'X'
    return winner(board)

#==========================================
# Purpose:
#   Plays many games of tic-tac-toe, and prints out the results
# Input Parameter(s):
#   n - an integer representing the number of games to play
# Return Value(s):
#   None
#==========================================
def play_games(n):
    winnars = []
    for i in range(n):
        game = tic_tac_toe()
        winnars.append(game)
    print("X wins:",winnars.count('X'))
    print("O wins:",winnars.count('O'))
    print("Draw:",winnars.count('D'))

