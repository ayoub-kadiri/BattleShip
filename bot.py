import random
from board import Board
from Player import Player
from Ship import Ship
class Bot(Player):
    
    def __init__(self, level):
        self.level = level
        Player.__init__()
    
    # fonction pour tirer au hasard, niveau = easy
    def shotFire(self):
        case = random.sample(Board.cases.keys(), 1)
        if Board.cases[case][2] != 'touché':
          return case
        else :
          shotFire(self)

    # fonction pour savoir si le bot a touche
    def did_hit(self, ships, case):
        for ship in ships:
            if case in ship.position:
                return True
        return False

        
