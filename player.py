from board import Board
from ship import Ship
class Player:
    score = 0
    def __init__(self, name):
        self.name = name
    
    # fonction pour savoir si on peut placer le bateau
    def does_ship_fit(self, shipSize, direction, startPos): #startPos : A1,A2,A3,...
        cases_prises = []
        if direction == 'verticale':
            for i in range(shipSize):
                cases_prises.append(chr(ord(startPos[0]+i)+startPos[1])) 
        else:
            for i in range(shipSize):
                cases_prises.append(startPos[0]+str(int(startPos[1])+i))

        for i in cases_prises:
            if i not in Board.cases :
                return False
        return True, cases_prises

    
    def placeShip(self, ship):
        pass
   


