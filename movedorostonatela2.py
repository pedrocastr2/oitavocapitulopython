import pygame 
pygame.init()

screen =pygame.display.set_mode([800,600]) 
pygame.display.set_caption("Animação Suave")


keep_going = True
pic = pygame.image.load("crazysmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
pic = pygame.transform.scale(pic, (100, 150))

picx,picy= 0,0
speed_x ,speed_y = 5,5
BLACK = (0,0,0)

timer = pygame.time.Clock() #timer para a animação


while keep_going: #loop de jogo
    for event in pygame.event.get():
       if event.type ==pygame.QUIT:
         keep_going = False  
      
    picx +=speed_x         #Move a figura
    picy +=speed_y
      
    if picx <=0 or picx + pic.get_width() >=600:
        speed_x = -speed_x
          
    if picy <=0 or picy + pic.get_height() >=800:
        speed_y = -speed_y
        
    screen.fill((BLACK)) #Limpa a tela
    screen.blit(pic,(picx,picy))   
    pygame.display.update()
    timer.tick(60)  #Limite para 60 frames por segundo

pygame.quit()
