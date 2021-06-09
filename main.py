import pygame
from board import Board
from bot import Bot
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
premier_click = False

arial25 = pygame.font.SysFont("arial",25)

def dessiner():
    fenetre.fill((0,0,0))
    g1.drawBoard()
    g2.drawBoard()
    game.drawFlotteEnnemie()
    game.drawFlotteJoueur()
    if not premier_click :
      game.drawInstruction()
    
    for i in game.flotte_joueur:
        img = pygame.image.load(i.image)
        if i.orientation == 'horizontale':
            fenetre.blit(pygame.transform.rotate(img, -90), (g1.cases[i.position[0]][0][0], g1.cases[i.position[0]][0][1]))
        else:
            fenetre.blit(img,(g1.cases[i.position[0]][0][0], g1.cases[i.position[0]][0][1])) 

    for i in game.bateau_a_afficher:
        img = pygame.image.load(i[0])
        img.set_alpha(170)
        if game.flotte_carac[i[2]][2] == 'verticale':
            fenetre.blit(img, (i[1]))
        else:
            fenetre.blit(pygame.transform.rotate(img, -90), (i[1]))

    for i in g2.cases.values():
        rect = pygame.Surface((50,50))  
        rect.set_alpha(128) 
        if i[2] == 'touche':
            rect.fill((255,0,0))           
            fenetre.blit(rect, (i[0][0][0], i[0][0][1]))
        elif i[2] == 'rate':
            rect.fill((0,255,0))           
            fenetre.blit(rect, (i[0][0][0], i[0][0][1]))

    for i in g1.cases.values():
        rect = pygame.Surface((50,50))  
        rect.set_alpha(128) 
        if i[2] == 'touche':
            rect.fill((255,0,0))           
            fenetre.blit(rect, (i[0][0][0], i[0][0][1]))
        elif i[2] == 'rate':
            rect.fill((0,255,0))           
            fenetre.blit(rect, (i[0][0][0], i[0][0][1]))

ready_to_play = False
pressed = False
while run:
    clock.tick(50)
    dessiner()
    if len(game.flotte_joueur) == 5:
        ready_to_play = True
    if ready_to_play == False: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and not click :
                moi.choose_ship_to_place(pygame.mouse.get_pos(), g1, fenetre)
                click = True

                m_pos = pygame.mouse.get_pos()

                if 276 <= m_pos[0] <= 904 and 385 <= m_pos[1] <= 472:
                    premier_click = True
                    bot = Bot('easy')
                    bot.random_placement(g2)
                
                elif 276 <= m_pos[0] <= 904 and 488 <= m_pos[1] <= 573 :
                    premier_click = True
                    bot = Bot('medium')
                    bot.random_placement(g2)
                
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
                    if  moi.can_place_ship(key[-1], moi.bateaux_ajoutes[key[-1]], game.flotte_carac[key[-1]][2], g1):
                        positions = moi.can_place_ship(key[-1], moi.bateaux_ajoutes[key[-1]], game.flotte_carac[key[-1]][2], g1)[1]
                        moi.addShip(key[-1], positions, game.flotte_carac[key[-1]][2], g1)
                    
            if event.type == pygame.KEYUP:
                pressed = False

    else:
        if game.flotte_non_coule()[0]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and not click :
                    if moi.get_target(pygame.mouse.get_pos(), g2):
                        if bot.level == 'easy':
                            bot.shotFire(g1)
                        else:
                            bot.shot_fire_lv2(g1)
                    click = True
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = False
        else:

            msg = 'Tu as {} !'.format(game.flotte_non_coule()[1])
            message = arial25.render(msg, True, pygame.Color(255,0,0))
            pygame.draw.rect(fenetre, (47, 79,79), ((540, 340), (150, 50)))
            fenetre.blit(message, (550,350))
            for i in game.flotte_bot:
                img = pygame.image.load(i.image)
                if i.orientation == 'horizontale':
                    fenetre.blit(pygame.transform.rotate(img, -90), (g2.cases[i.position[0]][0][0], g1.cases[i.position[0]][0][1]))
                else:
                    fenetre.blit(img,(g2.cases[i.position[0]][0][0], g2.cases[i.position[0]][0][1])) 
    
    pygame.display.flip()

pygame.quit()
