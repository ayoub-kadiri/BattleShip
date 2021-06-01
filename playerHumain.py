from board import Board
from game import Game
import random, pygame
class PlayerHumain:

    flotte = []
    
    def choose_ship_to_place(self, mousePos):
        mousePos = pygame.mouse.get_pos()
        if Game.sousMarin.get_rect(topleft=(60,620)).collidepoint(mousePos):
            self.addShip('sousMarin')
        pass

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


    def addShip(self, ship):
        pass


    
    
      

    