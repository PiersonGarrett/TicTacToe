from random import randint
import time
from os import system, name
class Computer:
    marker = "O"
    
    # generates random move on board
    def get_player_move(self):
        self.loading_animation()
        return [randint(0,2), randint(0,2)]
    
    def get_player_marker(self):
        return self.marker
    
    def clear(self):
        # for windows
        if name == 'nt':
            system('cls')
        # for mac and linux
        else: 
            system('clear') 

    def loading_animation(self):
        for i in range(3):
            self.clear()
            
            print("Thinking .")
            time.sleep(.5)
            self.clear()
            
            print("Thinking ..")
            time.sleep(.5)
            self.clear()

            print("Thinking ...")
            time.sleep(.5)
            self.clear()
