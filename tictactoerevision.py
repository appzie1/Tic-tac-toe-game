# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:52:04 2020

@author: Arka Banerjee
"""

def display_board(board):
    print('\n'*100)
    print('   '+'|'+'   '+'|')
    print(' '+board[7]+' |'+' '+board[8]+' |'+' '+board[9])
    print('   '+'|'+'   '+'|')
    print('-----------')
    print('   '+'|'+'   '+'|')
    print(' '+board[4]+' |'+' '+board[5]+' |'+' '+board[6])
    print('   '+'|'+'   '+'|')
    print('-----------')
    print('   '+'|'+'   '+'|')
    print(' '+board[1]+' |'+' '+board[2]+' |'+' '+board[3])
    print('   '+'|'+'   '+'|')
    


def player_input():
    marker=''
    marker=input('Player 1-Choose X or O: ').upper()
    while(marker=='X' or marker=='O'):
        break
    while not(marker=='X' or marker=='O'):
        marker=input('Wrong input!-Player 1 Choose X or O: ').upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
    
def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    return((board[1]==board[2]==board[3]==mark) or
           (board[4]==board[5]==board[6]==mark) or
           (board[7]==board[8]==board[9]==mark) or
           (board[1]==board[4]==board[7]==mark) or
           (board[2]==board[5]==board[8]==mark) or
           (board[3]==board[6]==board[9]==mark) or
           (board[1]==board[5]==board[9]==mark) or
           (board[3]==board[5]==board[7]==mark))

import random

def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board,position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in[1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose your next position: '))
    return position

def replay():
    return input('Do you want to play again-Yes or No: ').lower().startswith('y')

print('Welcome to TIC TAC TOE!')
while True:
    theBoard=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+' goes first')
    
    play_game=input('Are you ready to play?-Yes or No: ')
    while play_game:
        if play_game.lower().startswith('y'):
            game_on=True
            break
        else:
            print('Waiting for you to be ready...')
            play_game=input('Are you ready to play?-Yes or No: ')
            continue
            
    
    while game_on:
        if turn=='Player 1':
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Player 1 has won..Congratulations!')
                game_on=False
                
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Its a tie Game!')
                    break
                else:
                    turn='Player 2'
                        
        else:
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)
            
            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('Player 2 has won..Congratulations!')
                game_on=False
                
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Its a tie Game!')
                    break
                else:
                    turn='Player 1'
            
    if not replay():
        print('Thank you for visiting our game, hoping to see you soon!')
        break
        
        
        

        


    
    
    
    