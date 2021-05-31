import pygame

pygame.init() 
fenetre = pygame.display.set_mode( (1200,600) ) 
pygame.display.set_caption("BattleShip Game")
run = True
clock = pygame.time.Clock()
posLettre = (20,55)

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
      
    for n in range(65,75):
        arialfont = pygame.font.SysFont("arial",40)
        txt = arialfont.render(chr(n),True,(127,255,0))
        posLettre = (posLettre[0],posLettre[1]+1*(n-65))
        fenetre.blit(txt,posLettre)
        pygame.display.flip()
pygame.quit()
