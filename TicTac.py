import numpy as np
import sys
from random import randint
from os import system, name
import time
from Game import Game

# Main Game Loop
G1 = Game()
win_state = False
num_moves = 0

# This checks command line argument for non integers
try:
    arg1 = sys.argv[1]
    try:
        int(sys.argv[1])
        G1.set_player_count(sys.argv[1])
    except ValueError:
        G1.set_player_count(-1)
except IndexError:
    G1.set_player_count(-1)


G1.clear()
print("Welcome to Tic Tac Toe!\n")
print("1) The objective of this game is to get three of your markers in a row either horizontally, vertically or diagonally.\n")
print("2) There are 3 rows and 3 columns on the board. You will be prompted to enter the row and column of where you would like to",
"put your marker.\n")
print("3) The rows and columns start indexing at 1 and end at 3.\n")
input("Press enter to start the game ... ")

# Player vs Computer
while(win_state == False):
    if G1.get_player_count() == 1:
        G1.set_game_mode(0)
        print("You are playing against the computer!")
        time.sleep(2)
        G1.clear()
    # Randomly selecting a first move for the computer
        if G1.get_cur_player() == 1:
            print("The computer goes first!") 
            G1.add_move([randint(0,2),randint(0,2)],G1.get_player().get_player_marker())
            G1.print_board()
            num_moves += 1
            G1.set_player(1) if G1.get_player() == 0 else G1.set_player(0)
            time.sleep(2)
            G1.clear()
        else:
            print("You go first!")
            time.sleep(2)
            G1.clear()

       
        # Game Loop
        while(win_state == False and num_moves <= 9):
            G1.clear()
            G1.print_board()
            G1.print_player_turn()
            location = G1.get_player().get_player_move()
        # This if statement checks to see a choosen location can be placed on and checks to see if the game is over.    
            if G1.check_location(location):
                G1.add_move(location,G1.get_player().get_player_marker())
                num_moves += 1
                if num_moves > 9:
                    G1.clear()
                    G1.print_board()
                    print("It's a tie. Nobody wins :(")
                    time.sleep(2)
                    win_state = 1
                    break
                if G1.check_win(G1.get_player().get_player_marker()):
                    G1.clear()
                    G1.print_board()
                    if G1.get_cur_player() == 0:
                        print("Congratulations, You win!")
                        time.sleep(2)
                        G1.clear()
                        win_state = True
                        break
                    else:
                        print("The computer wins, better luck next time!")
                    time.sleep(2)
                    win_state = True
                    break
                # This statement changes which player's turn it is
                G1.set_player(1) if G1.get_cur_player() == 0 else G1.set_player(0)
            # This statement reminds the human player that you can not place a piece on an occupied position on the board.
            elif G1.get_cur_player() == 0:
                print("There is a piece in row",location[0],"column",location[1],"!\nPlease enter a position with no piece on it.")
                time.sleep(2)


    # Player vs Player
    elif G1.get_player_count() == 2:
        G1.set_game_mode(1)
        print("Player",G1.get_cur_player()+1,"goes first!")
        time.sleep(2)
        # Game loop
        while win_state == False and num_moves < 9:
            G1.clear()
            G1.print_board()
            G1.print_player_turn()
            location = G1.get_player().get_player_move()
            time.sleep(1)
            if G1.check_location(location):
                G1.add_move(location,G1.get_player().get_player_marker())
                num_moves +=1
                if num_moves == 9: 
                    print("It's a tie. Nobody wins :(")
                    time.sleep(2)
                    win_state = True
                if G1.check_win(G1.get_player().get_player_marker()):
                        G1.clear()
                        G1.print_board()
                        print("Congratulations Player",G1.get_cur_player()+1,", You win!")
                        time.sleep(2)
                        win_state = True
                        break
                #This statement changes which player's turn it is
                G1.set_player(1) if G1.get_cur_player() == 0 else G1.set_player(0)
            #This statement reminds players that you can not place a piece on an occupied position on the board.
            else:
                print("There is a piece in row",location[0],"column",location[1],"!\nPlease enter a position with no piece on it.")
                time.sleep(2)
            
    # This block performs error checking on command line arguments              
    else:
        while (G1.get_player_count() != 1 and G1.get_player_count() != 2):
            G1.clear()
            player_input= input("Up to 2 players can play at a time.\nPlease enter the number of players: ")
            try:
                player_input = int(player_input)
                G1.set_player_count(player_input)
                G1.set_game_mode(player_input-1)
            except ValueError:
                print("That's not a number!")
                time.sleep(2) 
            if player_input < 0: 
                print("You can not have a negative number of players!")
                time.sleep(2)
            elif player_input == 0:
                    print("You must have at least one player!")
                    time.sleep(2)