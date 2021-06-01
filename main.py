import pygame
from board import Board
from playerHumain import PlayerHumain
from game import Game
pygame.init() 
fenetre = pygame.display.set_mode( (1200,800) ) 
pygame.display.set_caption("BattleShip Game")
run = True
clock = pygame.time.Clock()
g1 = Board(60, {})
g2 = Board(660, {})

flotte_joueur = []
flotte_ennemie = []
moi = PlayerHumain()
game = Game()
click = False

sousMarin_image = pygame.image.load('images/torpilleurImage.png')
sousMarin_image = pygame.transform.scale(sousMarin_image, (58, 100))
while run:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not click:
            moi.choose_ship_to_place(pygame.mouse.get_pos())
            click = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = False
        
    fenetre.fill((0,0,0))
    g1.drawBoard(fenetre)
    g2.drawBoard(fenetre)
    game.drawFlotteEnnemie(fenetre)
    game.drawFlotteJoueur(fenetre)
    fenetre.blit(sousMarin_image, (64, 57))
    pygame.display.flip()

    
        
    
pygame.quit()
