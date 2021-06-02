import pygame
class Board :
   
    lettre = 'ABCDEFGHIJ'
    lettreImage = pygame.image.load('images/lettre.png')
    lettreImage = pygame.transform.scale(lettreImage, (50, 500))
    chiffresImages = pygame.image.load('images/chiffres.png')
    chiffresImages = pygame.transform.scale(chiffresImages, (500, 46))
    
    def __init__(self, xStartPos, cases, fenetre):
    
        self.xStartPos = xStartPos
        self.cases = cases
        self.fenetre = fenetre
        for i in range(10):
            for j in range(1,11):
                cases[self.lettre[i]+str(j)] = [pygame.Rect((xStartPos+(j-1)*50, 53+i*50), (xStartPos+(j-1)*60+60,53+4+i*60+60 )), False, 'vide']
        
    
    def update(self, case):
        cases[case][1] = True


    def drawBoard(self):
        for i in range(11):
            pygame.draw.line(self.fenetre, (127,255,0), (self.xStartPos+i*50,53), (self.xStartPos+i*50,556),4)
            pygame.draw.line(self.fenetre, (127,255,0), (self.xStartPos,54+i*50), (500+self.xStartPos,54+i*50),4)
        
        self.fenetre.blit(self.lettreImage, (self.xStartPos-48,57))
        self.fenetre.blit(self.chiffresImages,(self.xStartPos,560))
