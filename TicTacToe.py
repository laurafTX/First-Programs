#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 23:56:05 2020

@author: laurafinger
"""
#---Global Variables---
#----I stopped the videa at 23:34 'Handle_turn error" 0/1
#Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]
#if game is still going
game_still_going = True 

#who won or tie?

winner = None  

#whose turn is it?

current_player = "X"

def display_board():
    print(board[0]  + "|" + board[1]  +  "|" + board[2])
    print(board[3]  + "|" + board[4]  +  "|" + board[5])
    print(board[6]  + "|" + board[7]  +  "|" + board[8])
    
def play_game():
    
    display_board()

    while game_still_going:

    
        handle_turn(current_player)
    
        check_if_game_over()
    
        flip_player()
    
def handle_turn():
    position = input('Choose a position from 1-9: ')
    position = int(position) - 1
    
    board[position] = "X"
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    #check columns
    #check diagonals
    #check rows
    return 

def check_if_tie():
    #check columns
    #check diagonals
    #check rows
    return 

def flip_player():
    return 

play_game()    