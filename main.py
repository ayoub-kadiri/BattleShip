import pygame

pygame.init() 
fenetre = pygame.display.set_mode( (1200,600) ) 
pygame.display.set_caption("BattleShip Game")
run = True
clock = pygame.time.Clock()
lettres_position ={chr(i):(20, 55+50*(i-65)) for i in range(65,75)} 
arialfont = pygame.font.SysFont("arial",40)
while run:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    fenetre.fill((0,0,0))
    for i in range(11):
        
        pygame.draw.line(fenetre, (127,255,0), (60+i*50,53), (60+i*50,556),4)
        pygame.draw.line(fenetre, (127,255,0), (60,54+i*50), (560,54+i*50),4)
      
        pygame.draw.line(fenetre, (127,255,0), (660+i*50,53), (660+i*50,556),4)
        pygame.draw.line(fenetre, (127,255,0), (660,54+i*50), (1160,54+i*50),4)

    
    
    for lettre in lettres_position.keys():
        l = arialfont.render(lettre,False,(127,255,0))
        fenetre.blit(l,lettres_position[l])
    pygame.display.flip()
pygame.quit()
