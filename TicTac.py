import numpy as np
import sys
from random import randint
from os import system, name
import time
from Game import Game

# Initializing Game
match = Game()
win_state = False
num_moves = 0

# This checks command line argument for non integers.
# In the case of non integers a value that will be catched by later checks is assigned to the player count.
try:
    armatch = sys.argv[1]
    try:
        int(sys.argv[1])
        match.set_player_count(sys.argv[1])
    except ValueError:
        match.set_player_count(-1)
except IndexError:
    match.set_player_count(-1)


match.clear()
print("Welcome to Tic Tac Toe!\n")
print("1) The objective of this game is to get three of your markers in a row either horizontally, vertically or diagonally.\n")
print("2) There are 3 rows and 3 columns on the board. You will be prompted to enter the row and column of where you would like to",
"put your marker.\n")
print("3) The rows and columns start indexing at 1 and end at 3.\n")
input("Press enter to start the game ... ")

# Main Game Loop
while(win_state == False):
    # Player vs Computer
    if match.get_player_count() == 1:
        match.set_game_mode(0)
        print("You are playing against the computer!")
        time.sleep(2)
        match.clear()
        # Randomly selecting a first move for the computer
        if match.get_cur_player() == 1:
            print("The computer goes first!") 
            match.add_move([randint(0,2),randint(0,2)],match.get_player().get_player_marker())
            match.print_board()
            num_moves += 1
            match.set_player(1) if match.get_player() == 0 else match.set_player(0)
            time.sleep(2)
            match.clear()
        else:
            print("You go first!")
            time.sleep(2)
            match.clear()

       
        # Game Loop
        while(win_state == False and num_moves <= 9):
            match.clear()
            match.print_board()
            match.print_player_turn()
            location = match.get_player().get_player_move()
        # This if statement checks to see a choosen location can be placed on and checks to see if the game is over.    
            if match.check_location(location):
                match.add_move(location,match.get_player().get_player_marker())
                num_moves += 1
                if num_moves > 9:
                    match.clear()
                    match.print_board()
                    print("It's a tie. Nobody wins :(")
                    time.sleep(2)
                    win_state = 1
                    break
                # This if statement checks if the current player/computer has won
                if match.check_win(match.get_player().get_player_marker()):
                    match.clear()
                    match.print_board()
                    if match.get_cur_player() == 0:
                        print("Congratulations, You win!")
                        time.sleep(2)
                        match.clear()
                        win_state = True
                        break
                    else:
                        print("The computer wins, better luck next time!")
                        time.sleep(2)
                        win_state = True
                        break
                # This statement changes which player's turn it is
                match.set_player(1) if match.get_cur_player() == 0 else match.set_player(0)
            # This statement reminds the human player that you can not place a piece on an occupied position on the board.
            elif match.get_cur_player() == 0:
                print("There is a piece in row",int(location[0])+1,"column",int(location[1])+1,"!\nPlease enter a position with no piece on it.")
                time.sleep(3)


    # Player vs Player
    elif match.get_player_count() == 2:
        match.set_game_mode(1)
        print("Player",match.get_cur_player()+1,"goes first!")
        time.sleep(2)
        # Game loop
        while win_state == False and num_moves <= 9:
            match.clear()
            match.print_board()
            match.print_player_turn()
            location = match.get_player().get_player_move()
            time.sleep(1)
            # This if statement checks to see a choosen location can be placed on and checks to see if the game is over.
            if match.check_location(location):
                match.add_move(location,match.get_player().get_player_marker())
                num_moves +=1
                if num_moves == 9: 
                    print("It's a tie. Nobody wins :(")
                    time.sleep(2)
                    win_state = True
                # This checks if the current player has won
                if match.check_win(match.get_player().get_player_marker()):
                        match.clear()
                        match.print_board()
                        print("Congratulations Player",match.get_cur_player()+1,", You win!")
                        time.sleep(2)
                        win_state = True
                        break
                #This statement changes which player's turn it is
                match.set_player(1) if match.get_cur_player() == 0 else match.set_player(0)
            #This statement reminds players that you can not place a piece on an occupied position on the board.
            else:
                print("There is a piece in row",int(location[0])+1,"column",int(location[1])+1,"!\nPlease enter a position with no piece on it.")
                time.sleep(2)
            
    # This block performs error checking on command line arguments              
    else:
        while (match.get_player_count() != 1 and match.get_player_count() != 2):
            match.clear()
            player_input= input("Up to 2 players can play at a time.\nPlease enter the number of players: ")
            try:
                player_input = int(player_input)
                match.set_player_count(player_input)
                match.set_game_mode(player_input-1)
            except ValueError:
                print("That's not a number!")
                time.sleep(2) 
            if player_input < 0: 
                print("You can not have a negative number of players!")
                time.sleep(2)
            elif player_input == 0:
                    print("You must have at least one player!")
                    time.sleep(2)