import pygame
from spritesheet import Spritesheet

#Cursor class
class Cursor(object):
    def __init__(self, screen):  
        ss = Spritesheet('spritesheets/cursor.bmp')
        self.screen = screen
        self.pos_x = 0
        self.pos_y = 0
        self.location = (self.pos_x,self.pos_y)
        self.image = ss.image_at((0, 0, 40, 40))

    def get_location(self):
        return self.pos_x, self.pos_y

    def update(self, buttonpress):  
        if buttonpress == 'up':
            self.pos_y -= 40
        if buttonpress == 'down':
            self.pos_y += 40            
        if buttonpress == 'left':
            self.pos_x -= 40
        if buttonpress == 'right':
            self.pos_x += 40
        self.location = (self.pos_x,self.pos_y)
         
    def draw(self):
        self.screen.blit(self.image, self.location)
