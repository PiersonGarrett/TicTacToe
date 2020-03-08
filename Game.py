from random import randint
import numpy as np
from os import system, name
from Computer import Computer
from Player import Player

class Game:
    board = np.empty([3, 3], dtype=str)
    num_player = 0
    cur_player = 0
    game_mode = 0
    player1 = Player("X")
    player2 = Player("O")
    computer_player = Computer()

    def __init__(self):
        self.cur_player = randint(0, 1)
        self.game_mode = 0
        
    def set_player_count(self, num_player):
        self.num_player = int(num_player)

    def set_player(self, num_player):
        self.cur_player = num_player
    
    def set_game_mode(self,game_mode):
        self.game_mode = game_mode
    
    def get_player_count(self):
        return self.num_player

    def get_player(self):
        # Depending on the game mode the players playing are either two humans or a human and the computer
        if self.game_mode == 0:
            self.players = [self.player1,self.computer_player]
        else:
            self.players = [self.player1,self.player2]
        return self.players[self.cur_player]
    
    def get_cur_player(self):
        return self.cur_player

    def get_board(self):
        return self.board

    def print_board(self):
        print(self.board)

    def print_player_turn(self):
        if self.get_player_count() == 2:
            print("It's Player",self.cur_player+1,"'s turn!")
        else:
           print("It's Your Turn!") if self.get_cur_player() == 0 else print("It's the Computer's Turn!")

    def check_row(self, marker):
        for row, i in enumerate(self.board):
            count = 0
            for item in self.board[row]:
                if (item == marker):
                    count += 1
            if count == 3:
                return True
        return False

    def check_col(self, marker):
        for col,  i in enumerate(self.board):
            count = 0
            column = self.board[:, col]
            for item in column:
                if (item == marker):
                    count += 1
            if count == 3:
                return True
        return False

    def check_diag(self, marker):
        diag = np.empty([2, 3], dtype=str)
        for i in range(3):
            diag[0, i] = self.board[i, i]
            diag[1, i] = self.board[i, 2-i]
        count1 = 0
        count2 = 0
        for item1, item2 in zip(diag[0], diag[1]):
            if item1 == marker:
                count1 += 1
            if item2 == marker:
                count2 += 1
            if count1 == 3 or count2 == 3:
                return True
        return False

    def check_win(self, marker):
        is_win = self.check_row(marker) or \
                 self.check_col(marker) or self.check_diag(marker)
        return is_win


    def check_location(self, location):
        return self.board[int(location[0]), int(location[1])] == ""
    # This function checks to see if a marker can be placed at a location
    # Moves were not being read in correctly as integers.
    # Type casting fixed issue

    def add_move(self, location, cur_player_marker):
        self.board[int(location[0]), int(location[1])] = cur_player_marker

    def clear(self):
        # for windows
        if name == 'nt':
            system('cls')
        # for mac and linux
        else: 
            system('clear') 