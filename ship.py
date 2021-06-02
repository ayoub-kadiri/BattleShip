import pygame
class Ship:



    def __init__(self, image, size, position, orientation, hits): #position = liste de coordonnées
        self.size = size
        self.position = position
        self.image = image
        self.orientation = orientation
        self.hits = hits

        hits = [False for i in range(size)]

        
    
    def coule(self):
        if False not in self.hits :
            return True
        return False

    def is_hit(self, case):
        pass





    



    
    
