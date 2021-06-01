from board import Board
import pygame
class Game:
    
    flotte_ennemie_partie1 = pygame.image.load('images/enemy_fleet_panel_part1.png')
    flotte_ennemie_partie2 = pygame.image.load('images/enemy_fleet_panel_part2.png')

    sousMarin = pygame.image.load('images/imageonline-co-split-image.png')
    torpilleur = pygame.image.load('images/imageonline-co-split-image (1).png')
    destroyer = pygame.image.load('images/imageonline-co-split-image (2).png')
    croiseur = pygame.image.load('images/imageonline-co-split-image (3).png')
    porteAvion = pygame.image.load('images/imageonline-co-split-image (4).png')

    '''flotte_joueur = {
        sousMarin.get_rect() : 'Sous-Marin',
        torpilleur.get_rect() : 'Torpilleur',
        destroyer.get_rect() : 'Destroyer',
        croiseur.get_rect() : 'Croiseur',
        porteAvion.get_rect() : 'Porte Avion'
    }'''


    def drawFlotteEnnemie(self, fenetre):

        fenetre.blit(self.flotte_ennemie_partie1, (700,620))
        fenetre.blit(self.flotte_ennemie_partie2, (740,700))


    def drawFlotteJoueur(self, fenetre):
        fenetre.blit(self.sousMarin, (60,620))
        fenetre.blit(self.torpilleur, (60+self.sousMarin.get_width(),620))
        fenetre.blit(self.destroyer, (60+self.sousMarin.get_width()+self.torpilleur.get_width(), 620))
        fenetre.blit(self.croiseur, (75,700))
        fenetre.blit(self.porteAvion, (75+self.croiseur.get_width(), 700))

    def drawInstruction(self, fenetre):
        pass
