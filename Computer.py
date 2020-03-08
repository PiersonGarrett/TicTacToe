from random import randint

class Computer:
    marker = "O"
    
    # generates random move on board
    def get_player_move(self):
        return [randint(0,2), randint(0,2)]
    
    def get_player_marker(self):
        return self.marker
