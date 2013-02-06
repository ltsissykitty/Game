import pygame
from spritesheet import Spritesheet

#Unit class 
class Unit(object):
    def __init__( self, screen, unitname, spritesheet ):

        self.spritesheet = spritesheet
        self.unit_ss = Spritesheet( spritesheet )
        self.unit_sprite = (0, 0, 40, 40)
        self.unit_image = self.unit_ss.image_at( self.unit_sprite )
        
        self.move_tile_ss = Spritesheet('spritesheets/move_tile.bmp')
        self.move_tile_image = self.move_tile_ss.image_at((0, 0, 40, 40))
        
        self.screen = screen
        self.unitname = unitname
        
        self.frame = 0
  
        self.pos_x = 0
        self.pos_y = 0
        self.distance_x = 0
        self.distance_y = 0
        self.move_x = 0
        self.move_y = 0
        self.speed = 10
        self.unit_location = (self.pos_x, self.pos_y)
        
        self.state = 'idle'
        self.pressed_z = 0


    def get_data( self, unit, data ):
        self.i = 0
        self.char = ''
        self.value = 0
        
        self.path = "units/" + unit + "/" + unit + ".txt"
        self.tiledata = [ line.strip() for line in open( self.path, "r") ]

        if data == 'move_range':
            self.char = self.tiledata[1][13]
            self.value = int( self.char )

        return self.value


    def _move_diamond( self ):

        self.coordinates = []
        self.radius = self.get_data( self.unitname, 'move_range' )

        self.y = 0
        self.x = 0
        self.x_limit = 0

        self.x0 = self.pos_x
        self.y0 = self.pos_y + self.radius*40

        while self.y <= self.radius*2:
            while self.x <= self.x_limit:
                self.coordinates.append( ( self.x0 - self.x*40, self.y0 - self.y*40 ) )
                if self.y >= 0:
                    self.coordinates.append( ( self.x0 + self.x*40, self.y0 - self.y*40 ) )
                self.x += 1
            self.x = 0
            if self.y < self.radius:
                self.x_limit += 1
            elif self.y >= self.radius:
                self.x_limit -= 1
            self.y += 1

        return self.coordinates
        self.coordinates = []

        
    def update( self, cursor_x, cursor_y ):
        self.unit_ss = Spritesheet( self.spritesheet )
        
        if self.state == 'idle':
            self._animate('idle')
            if self.pressed_z and self.pos_x == cursor_x and self.pos_y == cursor_y:
                self.state = 'selected'
                self.pressed_z = 0
        elif self.state == 'selected':
            self._animate('selected')
            if self.pressed_z:
                self.state = 'moving'
        elif self.state == 'moving':
            self._animate('moving')
            self._move( cursor_x, cursor_y )

        self.pressed_z = 0
        self.unit_location = (self.pos_x,self.pos_y)
        self.unit_image = self.unit_ss.image_at( self.unit_sprite )


    def draw( self ):

        self.i = 0
        self.coordinates = self._move_diamond()
        
        while self.state == 'selected' and self.i < len(self.coordinates):
            self.screen.blit(self.move_tile_image, self.coordinates[self.i])
            self.i += 1
            
        self.screen.blit(self.unit_image, self.unit_location)
        
        
    def action( self ):
        self.pressed_z = 1

       
    def _move( self, cursor_x, cursor_y ):
        self.distance_x = cursor_x - self.pos_x
        self.distance_y = cursor_y - self.pos_y

        if self.distance_x == 0 and self.distance_y == 0:
            self.state = 'idle'

        if self.distance_x != 0:
            if self.distance_x > 0:
                self.pos_x += self.speed
            elif self.distance_x < 0:
                self.pos_x -= self.speed

        if self.distance_y != 0:
            if self.distance_y > 0:
                self.pos_y += self.speed
            elif self.distance_y < 0:
                self.pos_y -= self.speed


    def _animate( self, state ):
           
        if state == 'idle':
            if self.frame == 0:
                self.frame += 1
            else:
                self.frame = 0

        if state == 'selected' or state == 'moving':
            if self.frame < 5:
                self.frame += 1
            else:
                self.frame = 2

        self.unit_sprite = ( self.frame*40, 0, 40, 40 )
