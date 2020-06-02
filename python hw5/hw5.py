
#Name: Fahia Tabassum
import random



#Problem A (Detecting Wizards)
#========================================================================================================
# Purpose:
# Finding out the list of students who are wizards by having good grades, social life and sleep all together 
# Input Parameter(s):
# Grades-represents a list of students who get good grades
# Life- represents a list of students who have a social life
# Sleep- represents a list of students who get enough sleep
# Return Value(s):
# a list of all students who are clearly wizards 
#========================================================================================================

def wizards(grades, life, sleep):
    my_list = []
    i = 0
    while i < len(grades):
        j = 0
        while j < len(life):
            if grades[i] == life[j]:
                k = 0
                while k < len(sleep):
                    if grades[i] == life[j] == sleep[k]:
                         my_list.append(grades[i])
                          
                    k +=1
            j +=1
        i +=1

    return my_list
  

#Problem B(  Playing Tic-Tac-Toe Randomly)
#=====================================================================================================
# Purpose:
# showing the board list
# Input Parameter(s):
# a board list with a 9 element list
# Return Value(s):
# returns a list of the indexes which still contain a '-' 
#=====================================================================================================
def open_slots(board):
    my_list =[]
    i = 0
    while i < 9:
        if board[i] == '-':
            my_list.append(i)
        i +=1
    return my_list
        
        
#Problem B( Playing Tic-Tac-Toe Randomly)
#====================================================================================================
# Purpose:
# finding out who has won the game
# Input Parameter(s):
# board list with a 9 element list
# Return Value(s):
# returns a single character string that describes whether a player has won the game.
#====================================================================================================
def winner(board):
    if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        return 'O'
    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        return 'O'
    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        return 'O'
    elif board[0] == 'O' and board[3] == 'O' and board [6] == 'O':
        return 'O'
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        return 'O'
    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        return 'O'
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        return 'O'
    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        return 'O'
    elif board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        return 'X'
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        return 'X'
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        return 'X'
    elif board[0] == 'X' and board[3] == 'X' and board [6] == 'X':
        return 'X'
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        return 'X'
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        return 'X'
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        return 'X'
    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        return 'X'
    elif open_slots(board) == []:
        return 'D'
    else:
        return '-'

#Problem B( Playing Tic-Tac-Toe Randomly)
#================================================================================================================
# Purpose:
# simulating a single game of tic-tac-toe
# Input Parameter(s):
# no parameter
# Return Value(s):
# returns one character string that signifies the winner ('X', 'O', or 'D' for a draw)
#=================================================================================================================
def tic_tac_toe():
    board = 9*['-']
    next_move = random.choice(open_slots(board))
    i = 0
    while i <= 9:
        next_move = random.choice(open_slots(board))
        if open_slots(board) != []:
            if i%2 == 0:
                current_player = 'X'
            elif i%2 != 0:
                current_player = 'O'
        if current_player == 'X':
            board[next_move] = 'X'
        elif current_player == 'O':
            board[next_move] = 'O'
        if winner(board) != '-':
            return winner(board)
        
        i += 1
        
#Problem B( Playing Tic-Tac-Toe Randomly)
#=================================================================================================================
# Purpose:
# the total number of winning for X, O and draws seperately
# Input Parameter(s):
# an integer n representing the number of games to play
# Return Value(s):
# no return
#================================================================================================================
def play_games(n):
    m = 0
    i = 0
    j = 0
    k = 0
    while m < n:
        a = tic_tac_toe()
        if a == 'X':
            i +=1
        elif a == 'O':
            j += 1
        elif a == 'D':
            k +=1
        m +=1
    print('X wins:', str(i))
    print('O wins:' , str(j))
    print('Draws:', str(k))
    
