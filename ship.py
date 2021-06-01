import pygame
class Ship:
    sousMarin_image = pygame.image.load('images/torpilleurImage.png')
    sousMarin_image = pygame.transform.scale(sousMarin_image, (sousMarin_image.get_width(), 100))

    def __init__(self, name, size, position, orientation, hits): #position = liste de coordonnées
        self.size = size
        self.position = position
        self.name = name
        self.orientation = orientation
        self.hits = hits

    hits = [False for i in range(size)]

        
    
    def coule(self):
        if False not in self.hits :
            return True
        return False

    def is_hit(self, case):
        pass





    



    
    
