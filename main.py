import pygame

pygame.init() 
fenetre = pygame.display.set_mode( (600,600) ) 
pygame.display.set_caption("BattleShip Game")
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    fenetre.fill((0,0,0))
    pygame.draw.line(fenetre, (255,255,255), (50,0), (50,600),4)
    pygame.display.flip()

pygame.quit()