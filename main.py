import pygame
from board import Board
from playerHumain import PlayerHumain
from game import Game
pygame.init() 
fenetre = pygame.display.set_mode( (1200,800) ) 
pygame.display.set_caption("BattleShip Game")
run = True
clock = pygame.time.Clock()
g1 = Board(60, {}, fenetre)
g2 = Board(660, {}, fenetre)
game = Game(fenetre)

moi = PlayerHumain()

click = False

def dessiner():
    fenetre.fill((0,0,0))
    g1.drawBoard()
    g2.drawBoard()
    game.drawFlotteEnnemie()
    game.drawFlotteJoueur()
    
    for i in moi.flotte:
        img = pygame.image.load(i.image)
        if i.orientation == 'horizontale':
            fenetre.blit(pygame.transform.rotate(img, -90), (g1.cases[i.position][0][0], g1.cases[i.position][0][1]))
        else:
            fenetre.blit(img,(g1.cases[i.position][0][0], g1.cases[i.position][0][1])) 
    for i in game.bateau_a_afficher:
        img = pygame.image.load(i[0])
        img.set_alpha(170)
        if game.flotte_carac[i[2]][2] == 'verticale':
            fenetre.blit(img, (i[1]))
        else:
            fenetre.blit(pygame.transform.rotate(img, -90), (i[1]))
ready_to_play = False
pressed = False
while run:
    clock.tick(50)
    dessiner()   
    if len(moi.flotte) == 5:
        ready_to_play = True
    if ready_to_play == False: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and not click :
                moi.choose_ship_to_place(pygame.mouse.get_pos(), g1, fenetre)
                click = True
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = False
            if event.type == pygame.KEYDOWN and len(game.bateau_a_afficher) == 1:
                pressed = True
                key = list(moi.bateaux_ajoutes.keys())
                if event.key == pygame.K_LEFT:
                    moi.moveLeft(key[-1], moi.bateaux_ajoutes[key[-1]], g1)
                if event.key == pygame.K_RIGHT:
                    moi.moveRight(key[-1], moi.bateaux_ajoutes[key[-1]], g1)
                if event.key == pygame.K_DOWN:
                    moi.moveDown(key[-1], moi.bateaux_ajoutes[key[-1]], g1)
                if event.key == pygame.K_UP:
                    moi.moveUp(key[-1], moi.bateaux_ajoutes[key[-1]], g1)
                if event.key == pygame.K_SPACE:
                    moi.rotateImage(key[-1], g1)
                if event.key == pygame.K_RETURN:
                    
                    moi.addShip(key[-1], moi.bateaux_ajoutes[key[-1]], game.flotte_carac[key[-1]][2])
                
            if event.type == pygame.KEYUP:
                pressed = False
            


    else:
        pass
        
    
    
    
        
    pygame.display.flip()

    
        
    
pygame.quit()
