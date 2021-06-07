import random
from board import Board
from ship import Ship
from game import Game
class Bot:

    flotte = []
    targets = []
    def __init__(self, level):
        self.level = level
        

        
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
                return False, cases_prises
        return True, cases_prises

    def can_place_ship(self, ship, pos, orientation, board):
        case = self.does_ship_fit_in_grid(Game.flotte_carac[ship][1],orientation, pos, board)[1]
        for i in case:
            if board.cases[i][2] != 'vide':
                return False
        return True

    def update_board(self, board, pos, size, orientation):
        for i in pos:
            board.cases[i][2] = 'occupé'

    def addShip(self, ship, pos, orientation, board):
        if ship == 'Torpilleur':
            Game.flotte_bot.append(Ship('images/torpilleurImage.png', 2,pos,orientation , []))
            self.update_board(board, pos, 2, orientation)
        if ship == 'Destroyer':
            Game.flotte_bot.append(Ship('images/destroyerImage.png', 3, pos, orientation, []))
            self.update_board(board, pos, 3, orientation)
        if ship == 'Sous-Marin':
            Game.flotte_bot.append(Ship('images/sousMarinImage.png', 3, pos, orientation, []))
            self.update_board(board, pos, 3, orientation)
        if ship == 'Croiseur':
            Game.flotte_bot.append(Ship('images/croiseurImage.png', 4, pos, orientation, []))
            self.update_board(board, pos, 4, orientation)
        if ship == 'Porte Avion':
            Game.flotte_bot.append(Ship('images/porteAvionImage.png', 5, pos, orientation, []))
            self.update_board(board, pos, 5, orientation)

    def random_placement(self, board):
        
        for ship in list(Game.flotte_carac.keys()):
            ship_size = Game.flotte_carac[ship][1]
            positionne = False
            while not positionne :
                pos = random.sample(list(board.cases.keys()), 1)[0]
                orientation = random.sample(['verticale', 'horizontale'], 1)[0]
                cases = self.does_ship_fit_in_grid(ship_size, orientation, pos, board)[1]
                if self.does_ship_fit_in_grid(ship_size, orientation, pos, board)[0] and self.can_place_ship(ship, pos, orientation, board):
                    self.addShip(ship, cases, orientation, board)
                    positionne = True
               

    def shotFire(self,board):
        case = random.sample(board.cases.keys(), 1)[0]
        if not board.cases[case][1] :
            board.cases[case][1] = True
            self.bateau_touche( case, board)
            if self.level != 'easy':
                return case
        else :
            self.shotFire(board)


    def bateau_touche(self, case, board):
        board.cases[case][1] = True
        for ship in Game.flotte_joueur:
            for pos in ship.position:
                if pos == case:
                    ship.hit(case, board)
                    if self.level != 'easy':
                        if self.did_hit(Game.flotte_joueur, case):
                            self.cases_autour(board, case)
                    return
        board.cases[case][2] = 'rate'

    def did_hit(self, ships, case):
        for ship in ships:
            if case in ship.position:
                return True
        return False


    def cases_autour(self, board, case):
        en_haut = chr(ord(case[0])-1)+case[1:]
        en_bas = chr(ord(case[0])+1)+case[1:]
        a_gauche = case[0]+str(int(case[1:])-1)
        a_droite = case[0]+str(int(case[1:])+1)
        
        if en_haut in board.cases and not board.cases[en_haut][1] and en_haut not in self.targets:
            self.targets.append(en_haut)
        
        if a_gauche in board.cases and not board.cases[a_gauche][1] and a_gauche not in self.targets:
            self.targets.append(a_gauche)
        
        if en_bas in board.cases and not board.cases[en_bas][1] and en_bas not in self.targets:
            self.targets.append(en_bas)
        
        if a_droite in board.cases and not board.cases[a_droite][1] and a_droite not in self.targets:
            self.targets.append(a_droite)
        

        

    def shot_fire_lv2(self, board):
        for i in self.targets:
            if board.cases[i][1]:
                self.targets.remove(i)
        if len(self.targets) == 0:
            case = self.shotFire(board)
            if self.did_hit(Game.flotte_joueur, case):
                self.cases_autour(board, case)
        else:
            self.bateau_touche(self.targets[0], board)
            del self.targets[0]
        
        print(self.targets)
        

        
