import unittest
import numpy as np
from Computer import Computer
from Player import Player
from Game import Game
from random import randint

class TestCheckMethods(unittest.TestCase):
    marker = "X"
    computer = Computer()
    player = Player(marker)
    game = Game()
    # Testing if the program can recognize 3 in a row in each row
    def test_row_check(self):
        case_empty = np.empty([3, 3], dtype=str)
        case_row1 = np.empty([3, 3], dtype=str)
        case_row2 = np.empty([3, 3], dtype=str)
        case_row3 = np.empty([3, 3], dtype=str)
        for i in range(3):
            case_row1[0,i] = self.marker
            case_row2[1,i] = self.marker
            case_row3[2,i] = self.marker
        
        self.game.set_board(case_empty)
        row_bool_empty = self.game.check_row(self.marker)
        self.assertFalse(row_bool_empty)
        
        self.game.set_board(case_row1)
        row_bool1 = self.game.check_row(self.marker)
        self.assertTrue(row_bool1)

        self.game.set_board(case_row1)
        row_bool2 = self.game.check_row(self.marker)
        self.assertTrue(row_bool2)
        
        self.game.set_board(case_row1)
        row_bool3 = self.game.check_row(self.marker)
        self.assertTrue(row_bool3)
    
    def test_col_check(self):
        case_empty = np.empty([3, 3], dtype=str)
        case_col1 = np.empty([3, 3], dtype=str)
        case_col2 = np.empty([3, 3], dtype=str)
        case_col3 = np.empty([3, 3], dtype=str)
        for i in range(3):
            case_col1[i,0] = self.marker
            case_col2[i,1] = self.marker
            case_col3[i,2] = self.marker
        
        self.game.set_board(case_empty)
        col_bool_empty = self.game.check_col(self.marker)
        self.assertFalse(col_bool_empty)
        
        self.game.set_board(case_col1)
        col_bool1 = self.game.check_col(self.marker)
        self.assertTrue(col_bool1)

        self.game.set_board(case_col2)
        col_bool2 = self.game.check_col(self.marker)
        self.assertTrue(col_bool2)
        
        self.game.set_board(case_col3)
        col_bool3 = self.game.check_col(self.marker)
        self.assertTrue(col_bool3)
    
    # Testing if method returns True for 3 in a row diagonally and False for no 3 in a row diagonally
    def test_diag_check(self):
        case_empty = np.empty([3, 3], dtype=str)
        case_diamatch = np.empty([3, 3], dtype=str)
        case_diag2 = np.empty([3, 3], dtype=str)
        for i in range(3):
            case_diamatch[i, i] = self.marker
            case_diag2[i, 2-i] = self.marker
        
        self.game.set_board(case_empty)
        diag_bool_empty = self.game.check_diag(self.marker)
        self.assertFalse(diag_bool_empty)
        
        self.game.set_board(case_diamatch)
        diag_bool1 = self.game.check_diag(self.marker)
        self.assertTrue(diag_bool1)

        self.game.set_board(case_diag2)
        diag_bool2 = self.game.check_diag(self.marker)
        self.assertTrue(diag_bool2)
    
    # Testing if method returns True for an available space and False for an unavailable space
    def test_check_location(self):
        row_test = randint(0,2)
        col_test = randint(0,2)
        case_empty = np.empty([3, 3], dtype=str)
        case1 = np.empty([3, 3], dtype=str)
        case1[row_test,col_test] = self.marker
        
        self.game.set_board(case_empty)
        location_bool = self.game.check_location([row_test,col_test])
        self.assertTrue([row_test,col_test],case_empty)

        self.game.set_board(case1)
        location_bool = self.game.check_location([row_test,col_test])
        self.assertFalse(location_bool)

   
        
if __name__ == '__main__':
    unittest.main()