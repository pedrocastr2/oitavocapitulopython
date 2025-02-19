
import pygame 
pygame.init()

screen =pygame.display.set_mode([800,600]) 
pic = pygame.image.load("Crazysmile.bmp")
pic = pygame.transform.scale(pic, (100, 150))
keep_going = True


while keep_going: 
    for event in pygame.event.get():
      if event.type ==pygame.QUIT:
         keep_going = False  
      
    screen.fill((255, 255, 255)) 
       
    screen.blit(pic,(100,100))
      
      
    pygame.display.update()
      

pygame.quit()