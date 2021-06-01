import random
from board import Board
from ship import Ship
class Bot:

    flotte = []
    
    def __init__(self, level):
        self.level = level
        
    
    def shotFire(self):
        case = random.sample(Board.cases.keys(), 1)
        if Board.cases[case][2] != 'touché':
          return case
        else :
          shotFire(self)

    def did_hit(self, ships, case):
        for ship in ships:
            if case in ship.position:
                return True
        return False

        