from Player import Player
class Ship:
    def __init__(self, name, size, position, orientation): #position = liste de coordonnées
        self.size = size
        self.position = position
        self.name = name
        self.orientation = orientation

    hits = [False for i in range(size)]


    def coule(self):
        if False not in self.hits :
            return True
        return False

    def is_hit(self, case):
        pass


    



    
    
