import sys, pygame
from spritesheet import Spritesheet

#Background class
class Background(object):
    def __init__(self, screen):  
        grass = Spritesheet('tiles/grass/grass.bmp')
        water = Spritesheet('tiles/water/water.bmp')

        self.grass = grass.image_at((0, 0, 40, 40))
        self.water = water.image_at((0, 0, 40, 40))

        self.tile = screen
        self.screen = screen
        
        self.mapdata = [line.strip() for line in open("maps/map0.txt", "r")]

        self.pos_x = 0
        self.pos_y = 0
        self.location = (self.pos_x, self.pos_y)

    def get_data( self, tile, data ):
        self.i = 0
        self.value = ''
        
        self.path = "tiles/" + tile + "/" + tile + ".txt"
        self.tiledata = [ line.strip() for line in open( self.path, "r") ]

        if data == 'symbol':
            self.value = self.tiledata[1][9]

        if data == 'walkable':
            while self.i < ( len(self.tiledata[2]) - 11 ):
                self.value += self.tiledata[2][11 + self.i]
                self.i+=1

        return self.value
   
    def draw(self):
        self.i = 0
        self.j = 0
        
        while self.i < len(self.mapdata):
            while self.j < len(self.mapdata[self.i]):
                self.pos_y = self.i*40
                self.pos_x = self.j*40
                self.location = ( self.pos_x, self.pos_y )
                if self.mapdata[self.i][self.j] == 'G':
                    self.tile.blit(self.grass, self.location)
                if self.mapdata[self.i][self.j] == 'W':
                    self.tile.blit(self.water, self.location)
                self.j += 1
            self.j = 0    
            self.i += 1
        self.i = 0

