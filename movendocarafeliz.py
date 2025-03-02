import pygame 
pygame.init()

screen =pygame.display.set_mode([800,600]) 
keep_going = True
pic = pygame.image.load("Crazysmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy= 0
BLACK = (0,0,0)
pic = pygame.transform.scale(pic, (100, 150))
timer = pygame.time.Clock() #timer para a animação


while keep_going: #loop de jogo
    for event in pygame.event.get():
      if event.type ==pygame.QUIT:
         keep_going = False  
      
      picx +=10         #Move a figura
      picy +=10
      
      
    screen.fill((BLACK)) #Limpa a tela
    screen.blit(pic,(picx,picy))   
    pygame.display.update()
    timer.tick(60)  #Limite para 60 frames por segundo

pygame.quit()