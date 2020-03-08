import numpy as np
import sys
from random import randint
from os import system, name
import time

class game:
    board = np.empty([3,3], dtype = str)
    num_player = 0
    cur_player = 0
    def __init__(self):
        self.cur_player = randint(0,1)
    
    def set_player_count(self,num_player):
        self.num_player = int(num_player)
    
    def set_player(self,num_player):
        self.cur_player = num_player
    
    def get_player_count(self):
        return self.num_player
    
    def get_player(self):
        return self.cur_player
    
    def get_board(self):
        return self.board

    def print_board(self):
        print(self.board)

    def print_player_turn(self):
        if self.get_player_count() == 2:
            print("It's Player",self.cur_player+1,"'s turn!")
        else:
           print("It's Your Turn!") if self.get_player() == 0 else print("It's the Computer's Turn!")

    def check_row(self,marker):
        for row, i in enumerate(self.board):    
            count = 0
            for item in self.board[row]:
                if (item == marker):count+=1 
            if count == 3:
                return 1
        return 0

    def check_col(self,marker):
        for col,i in enumerate(self.board):
            count = 0
            column = self.board[:,col]
            for item in column:
                if (item == marker):count+=1 
            if count == 3:
                return 1
        return 0
    
    def check_diag(self,marker):
        diag = np.empty([2,3],dtype = str)
        for i in range(3):
            diag[0,i] = self.board[i,i]
            diag[1,i] = self.board[i,2-i]
        count1 = 0
        count2 = 0
        for item1, item2 in zip(diag[0],diag[1]):
            if item1 == marker:count1+=1 
            if item2 == marker:count2+=1 
            if count1 == 3 or count2 == 3:return 1
        return 0
    
    def check_win(self,marker):
        if self.check_row(marker): return 1
        elif self.check_col(marker): return 1
        elif self.check_diag(marker): return 1
        else: return 0
    
    def check_location(self,location):
        return self.board[int(location[0]),int(location[1])] == ""
    #This function checks to see if a marker can be placed at a location
    # Moves were not being read in correctly as integers. Type casting fixed issue
    def add_move(self,location, cur_player_marker):
            self.board[int(location[0]),int(location[1])] = cur_player_marker
    
    def clear(self):
        # for windows 
        if name == 'nt': 
            system('cls') 
        # for mac and linux 
        else: 
            system('clear') 
    
class player:
    marker = ""
    def __init__(self,marker):
        self.marker = marker
    
    def get_player_marker(self):
        return self.marker
    
    def get_player_move(self):
        move = np.empty(2) 
        print("Press enter once you finish choosing.")
        check_bool = 0
    
        while(check_bool == 0):
            try:
                move[0] = int(input("Enter the row: "))-1
                check_bool = 1
            except ValueError:
                print("Please enter an integer from 1 to 3.")
                time.sleep(1)
                G1.clear()
                G1.print_board()
        check_bool = 0
        while(check_bool == 0):
            try:
                move[1] = int(input("Enter the column: "))-1
                check_bool = 1
            except ValueError:
                print("Please enter an integer from 1 to 3.")
                time.sleep(1)
                G1.clear()
                G1.print_board()
            
        return move

class computer:
    marker = "O"
    
    # generates random move on board
    def get_player_move(self):
        return [randint(0,2),randint(0,2)]
    
    def get_player_marker(self):
        return self.marker


        
# Main Game Loop

G1 = game()
win_state = 0
num_moves = 0

#This checks command line argument for non integers
try:
    arg1 = sys.argv[1]
    try:
        int(sys.argv[1])
        G1.set_player_count(sys.argv[1])
    except ValueError:
        G1.set_player_count(-1)
except IndexError:
    G1.set_player_count(-1)
    

player1 = player("X")
player2 = player("O")
computer_player = computer()



G1.clear()
print("Welcome to Tic Tac Toe!\n")
print("1) The objective of this game is to get three of your markers in a row either horizontally, vertically or diagonally.\n")
print("2) There are 3 rows and 3 columns on the board. You will be prompted to enter the row and column of where you would like to",
"put your marker.\n")
print("3) The rows and columns start indexing at 1 and end at 3.\n")
input("Press enter to start the game ... ")

# Player vs Computer
if G1.get_player_count() == 1:
    players = [player1,computer_player]
    print("You are playing against the computer!")
    time.sleep(2)
    G1.clear()
# Randomly selecting a first move for the computer
    if G1.get_player() == 1:
        print("The computer goes first!") 
        G1.add_move([randint(0,2),randint(0,2)],players[G1.get_player()].get_player_marker())
        G1.print_board()
        num_moves+=1
        time.sleep(2)
        G1.clear()
    else:
         print("You go first!")
         players[G1.get_player()].get_player_move()
         num_moves+=1
         time.sleep(2)
         G1.clear()
    
    G1.set_player(1) if G1.get_player() == 0 else G1.set_player(0)
    # Game Loop
    while(win_state == 0 and num_moves <= 9):
        G1.clear()
        G1.print_board()
        G1.print_player_turn()
        location = players[G1.get_player()].get_player_move()
    #This if statement checks to see a choosen location can be placed on and checks to see if the game is over.    
        if G1.check_location(location):
            G1.add_move(location,players[G1.get_player()].get_player_marker())
            num_moves +=1
            if num_moves > 9: 
                G1.clear()
                G1.print_board()
                print("It's a tie. Nobody wins :(")
                time.sleep(2)
                win_state == 1
                break
            if G1.check_win(players[G1.get_player()].get_player_marker()):
                G1.clear()
                G1.print_board()
                if G1.get_player() == 0:
                    print("Congratulations, You win!")
                else:
                    print("The computer wins, better luck next time!")
                time.sleep(2)
                win_state == 1
                break
            #This statement changes which player's turn it is
            G1.set_player(1) if G1.get_player() == 0 else G1.set_player(0)
        #This statement reminds the human player that you can not place a piece on an occupied position on the board.
        elif G1.get_player() == 0:
            print("There is a piece in row",location[0],"column",location[1],"!\nPlease enter a position with no piece on it.")
            time.sleep(2)
   

# Player vs Player
elif G1.get_player_count() == 2:
    players = [player1,player2]
    print("Player",G1.get_player()+1,"goes first!")
    time.sleep(2)
    # Game loop
    while win_state == 0 and num_moves < 9:
        G1.clear()
        G1.print_board()
        G1.print_player_turn()
        location = players[G1.get_player()].get_player_move()
        time.sleep(1)
        if G1.check_location(location):
           G1.add_move(location,players[G1.get_player()].get_player_marker())
           num_moves +=1
           if num_moves == 9: 
               print("It's a tie. Nobody wins :(")
               time.sleep(2)
               win_state == 1
           if G1.check_win(players[G1.get_player()].get_player_marker()):
                G1.clear()
                G1.print_board()
                print("Congratulations Player",G1.get_player()+1,", You win!")
                time.sleep(2)
                win_state == 1
                break
           #This statement changes which player's turn it is
           G1.set_player(1) if G1.get_player() == 0 else G1.set_player(0)
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
        except ValueError:
            print("That's not a number!")
            time.sleep(2) 
        if player_input < 0: 
            print("You can not have a negative number of players!")
            time.sleep(2)