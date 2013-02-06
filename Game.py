import os, sys, pygame
from background import Background
from unit import Unit
from cursor import Cursor
 
#Main  
pygame.init()
screenwidth = 640
screenheight = 480
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption('Game')

#game clock
FPS = 20
clock = pygame.time.Clock()

trooper = Unit(screen, 'trooper', 'spritesheets/trooper.bmp')
background = Background(screen)
cursor = Cursor(screen)

cursor_x, cursor_y = (0,0)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_z:
                trooper.action()
            elif event.key == pygame.K_UP:
                cursor.update('up')
            elif event.key == pygame.K_DOWN:
                cursor.update('down')
            elif event.key == pygame.K_LEFT:
                cursor.update('left')
            elif event.key == pygame.K_RIGHT:
                cursor.update('right')

    cursor_x, cursor_y = cursor.get_location()

    
    
    trooper.update( cursor_x, cursor_y )
    background.draw()        
    trooper.draw()
    cursor.draw()
    pygame.display.flip()

    moveflag = 0
    clock.tick(FPS)
