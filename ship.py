import pygame
class Ship:



    def __init__(self, image, size, position, orientation, hits): #position = liste de coordonnées
        self.size = size
        self.position = position
        self.image = image
        self.orientation = orientation
        self.hits = hits

        self.hits = [False for i in range(size)]

        
    
    def coule(self):
        if False not in self.hits :
            return True
        return False

    def hit(self, case, board):
        if not self.coule():
            self.hits[self.position.index(case)] = True
            board.cases[case][2] = 'touche'
        else:
            pass





    



    
    
