import time
from os import system, name
import numpy as np
class Player:
    marker = ""

    def __init__(self,marker):
        self.marker = marker
    
    def get_player_marker(self):
        return self.marker
    
    def get_player_move(self):
        move = np.empty(2)
        print("Press enter once you finish choosing.")
        check_bool = 0
        # checks the input to make sure it is a positive integer from 1 to 3
        while(check_bool == 0):
            try:
                move[0] = int(input("Enter the row: "))-1
                if move[0] < 0 or move[0] > 2: raise ValueError
                check_bool = 1
            except ValueError:
                print("Please enter an integer from 1 to 3.")
                time.sleep(1)
                self.clear()
                
        check_bool = 0
        while(check_bool == 0):
            try:
                move[1] = int(input("Enter the column: "))-1
                if move[1] < 0 or move[1] > 2: raise ValueError
                check_bool = 1
            except ValueError:
                print("Please enter an integer from 1 to 3.")
                time.sleep(1)
                self.clear()
                
        return move
   
    def clear(self):
        # for windows
        if name == 'nt':
            system('cls')
        # for mac and linux
        else: 
            system('clear') 
