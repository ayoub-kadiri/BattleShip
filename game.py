from board import Board
import pygame
class Game:

    bateau_a_afficher = []
    ships = []

    def __init__(self, fenetre):
        self.fenetre = fenetre
    
    flotte_ennemie_partie1 = pygame.image.load('images/enemy_fleet_panel_part1.png')
    flotte_ennemie_partie2 = pygame.image.load('images/enemy_fleet_panel_part2.png')

    sousMarin = pygame.image.load('images/imageonline-co-split-image.png')
    torpilleur = pygame.image.load('images/imageonline-co-split-image (1).png')
    destroyer = pygame.image.load('images/imageonline-co-split-image (2).png')
    croiseur = pygame.image.load('images/imageonline-co-split-image (3).png')
    porteAvion = pygame.image.load('images/imageonline-co-split-image (4).png')

    flotte_carac = {
        'Torpilleur' : ['images/torpilleurImage.png', 2, 'verticale'],
        'Destroyer' : ['images/destroyerImage.png', 2, 'verticale'],
        'Sous-Marin' : ['images/sousMarinImage.png', 3, 'verticale'],
        'Croiseur' : ['images/croiseurImage.png', 4, 'verticale'],
        'Porte Avion' : ['images/porteAvionImage.png', 5, 'verticale']
    }

    
    def drawFlotteEnnemie(self):

        self.fenetre.blit(self.flotte_ennemie_partie1, (700,620))
        self.fenetre.blit(self.flotte_ennemie_partie2, (740,700))


    def drawFlotteJoueur(self):
        self.fenetre.blit(self.sousMarin, (60,620))
        self.fenetre.blit(self.torpilleur, (60+self.sousMarin.get_width(),620))
        self.fenetre.blit(self.destroyer, (60+self.sousMarin.get_width()+self.torpilleur.get_width(), 620))
        self.fenetre.blit(self.croiseur, (75,700))
        self.fenetre.blit(self.porteAvion, (75+self.croiseur.get_width(), 700))

    def drawInstruction(self):
        pass
