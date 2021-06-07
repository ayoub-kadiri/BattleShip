from board import Board
from game import Game
from ship import Ship
import random, pygame
class PlayerHumain:

    flotte = [] 
    bateaux_ajoutes = {}
    def choose_ship_to_place(self, mousePos, board, fenetre):
        mousePos = pygame.mouse.get_pos()
        if len(Game.bateau_a_afficher) == 0:
            if Game.sousMarin.get_rect(topleft=(60,620)).collidepoint(mousePos) and 'Sous-Marin' not in self.bateaux_ajoutes:
                Game.bateau_a_afficher.append([Game.flotte_carac['Sous-Marin'][0], 'A1','Sous-Marin'])
                self.placeShip('Sous-Marin','A1', board)
                self.bateaux_ajoutes['Sous-Marin'] ='A1'
                
            elif Game.torpilleur.get_rect(topleft=(208,620)).collidepoint(mousePos) and 'Torpilleur' not in self.bateaux_ajoutes:
                Game.bateau_a_afficher.append([Game.flotte_carac['Torpilleur'][0], 'A1','Torpilleur'])
                self.placeShip('Torpilleur','A1', board)
                self.bateaux_ajoutes['Torpilleur'] = 'A1'
            
            elif Game.destroyer.get_rect(topleft=(335,620)).collidepoint(mousePos) and 'Destroyer' not in self.bateaux_ajoutes:
                Game.bateau_a_afficher.append([Game.flotte_carac['Destroyer'][0], 'A1','Destroyer'])
                self.placeShip('Destroyer','A1', board)
                self.bateaux_ajoutes['Destroyer'] = 'A1'
            
            elif Game.croiseur.get_rect(topleft=(75,700)).collidepoint(mousePos) and 'Croiseur' not in self.bateaux_ajoutes:
                Game.bateau_a_afficher.append([Game.flotte_carac['Croiseur'][0], 'A1','Croiseur'])
                self.placeShip('Croiseur','A1', board)
                self.bateaux_ajoutes['Croiseur'] = 'A1'
            
            elif Game.croiseur.get_rect(topleft=(278,700)).collidepoint(mousePos) and 'Porte Avion' not in self.bateaux_ajoutes:
                Game.bateau_a_afficher.append([Game.flotte_carac['Porte Avion'][0], 'A1', 'Porte Avion'])
                self.placeShip('Porte Avion','A1', board)
                self.bateaux_ajoutes['Porte Avion'] = 'A1'
            

    def does_ship_fit_in_grid(self, shipSize, direction, startPos, board): #startPos : A1,A2,A3,...
        cases_prises = []
        if direction == 'verticale':
            
            for i in range(shipSize):
                cases_prises.append(chr(ord(startPos[0])+i)+startPos[1:])
        else:
            for i in range(shipSize):
                cases_prises.append(startPos[0]+str(int(startPos[1:])+i))

        for i in cases_prises:
            if i not in board.cases :
                return False
        return True, cases_prises


    def placeShip(self, ship, pos, board):
        pos_dessin = board.cases[pos][0][0], board.cases[pos][0][1]
        Game.bateau_a_afficher[0][1] = pos_dessin
        self.bateaux_ajoutes[ship] = pos
        


    def moveLeft(self, ship, pos, board):
        newpos = pos[0]+str(int(pos[1:]) - 1)
        if self.does_ship_fit_in_grid(Game.flotte_carac[ship][1],Game.flotte_carac[ship][2], newpos, board) :
           self.placeShip(ship, newpos, board)
        else:
            self.placeShip( ship, pos, board)
    
    def moveRight(self, ship, pos, board):
        newpos = pos[0]+str(int(pos[1:]) + 1)
        if self.does_ship_fit_in_grid(Game.flotte_carac[ship][1],Game.flotte_carac[ship][2], newpos, board) :
           self.placeShip( ship, newpos, board)
        else:
            self.placeShip( ship, pos, board)

    def moveDown(self, ship, pos, board):
        newpos = chr(ord(pos[0])+1)+pos[1:]
        if self.does_ship_fit_in_grid(Game.flotte_carac[ship][1],Game.flotte_carac[ship][2], newpos, board) :
           self.placeShip( ship, newpos, board)
        else:
            self.placeShip( ship, pos, board)

    def moveUp(self, ship, pos, board):
        newpos = chr(ord(pos[0])-1)+pos[1:]
        if self.does_ship_fit_in_grid(Game.flotte_carac[ship][1],Game.flotte_carac[ship][2], newpos, board) :
           self.placeShip( ship, newpos, board)
        else:
            self.placeShip( ship, pos, board)

    def rotateImage(self, ship, board):
        if Game.flotte_carac[ship][2] == 'verticale':
            Game.flotte_carac[ship][2] = 'horizontale'
            self.placeShip( ship, 'A1', board)
        else:
            Game.flotte_carac[ship][2] = 'verticale'
            self.placeShip( ship, 'A1', board)

        
        



    def addShip(self, ship, pos, orientation, board):
        del Game.bateau_a_afficher[0]
        if ship == 'Torpilleur':
            Game.flotte_joueur.append(Ship('images/torpilleurImage.png', 2,pos,orientation , []))
            self.update_board(board, pos, 2, orientation)
        if ship == 'Destroyer':
            Game.flotte_joueur.append(Ship('images/destroyerImage.png', 3, pos, orientation, []))
            self.update_board(board, pos, 3, orientation)
        if ship == 'Sous-Marin':
            Game.flotte_joueur.append(Ship('images/sousMarinImage.png', 3, pos, orientation, []))
            self.update_board(board, pos, 3, orientation)
        if ship == 'Croiseur':
            Game.flotte_joueur.append(Ship('images/croiseurImage.png', 4, pos, orientation, []))
            self.update_board(board, pos, 4, orientation)
        if ship == 'Porte Avion':
            Game.flotte_joueur.append(Ship('images/porteAvionImage.png', 5, pos, orientation, []))
            self.update_board(board, pos, 5, orientation)

    def update_board(self, board, pos, size, orientation):
        for i in pos:
            board.cases[i][2] = 'occupé'

    def can_place_ship(self, ship, pos, orientation, board):
        case = self.does_ship_fit_in_grid(Game.flotte_carac[ship][1],orientation, pos, board)[1]
        for i in case:
            if board.cases[i][2] != 'vide':
                return False
        return True, case
            
    

    def collide(self, mousepos, rect):
        if rect[0][0] <= mousepos[0] <= rect[1][0] and rect[0][1] <= mousepos[1] <= rect[1][1]:
            return True
        return False

    def bateau_touche(self, case, board):
        for ship in Game.flotte_bot:
            for pos in ship.position:
                if pos == case:
                    ship.hit(case, board)
                    return
        board.cases[case][2] = 'rate'


    def get_target(self, mousePos, board):
        choose = False
        for case, cord in board.cases.items() :
            if self.collide(mousePos, cord[0]) and not board.cases[case][1] and not choose:
                board.cases[case][1] = True
                choose = True
                self.bateau_touche(case, board)
                return True
        return False

    
