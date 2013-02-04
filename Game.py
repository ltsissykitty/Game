import os, sys, pygame

#load sprite class
class Spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error, message:
            print 'Unable to load spritesheet image:', filename
            raise SystemExit, message
        
    #Loads image from ( x, y , x+offset, y+offset )
    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        image.set_colorkey((255,0,255))
        return image

#Background class
class Background(object):
    def __init__(self, screen):  
        ss = Spritesheet('images/background.bmp')
        self.screen = screen
        self.location = (0,0)
        self.image = ss.image_at((0, 0, 640, 480))

    def draw(self):
        self.screen.blit(self.image, self.location)

#Trooper class 
class Trooper(object):
    def __init__(self, screen):
        ss = Spritesheet('images/trooper.bmp')
        self.screen = screen
        self.movecounter = 0
        self.posx = 0
        self.posy = 0
        self.location = (self.posx,self.posy)
        self.stateflag = 0
        self.sprite = (0, 0, 40, 40)
        self.image = ss.image_at(self.sprite)

    def move(self, direction, distance):
        if self.movecounter < distance*40:
            if direction == 1:
                self.posy -= 2
                self.movecounter += 2
            elif direction == 2:
                self.posy += 2
                self.movecounter += 2
            elif direction == 3:
                self.posx -= 2
                self.movecounter += 2
            elif direction == 4:
                self.posx += 2
                self.movecounter += 2
            return 1
        else:
            self.movecounter = 0
            return 0
            

    def get_location(self):
        return self.posx, self.posy
        
    def update(self, updatetime, time):
        ss = Spritesheet('images/trooper.bmp')
        if time >= updatetime:
            if self.stateflag == 0:
                self.stateflag = 1
                self.sprite = (0, 0, 40, 40)
            elif self.stateflag == 1:
                self.sprite = (40, 0, 40, 40)
                self.stateflag = 0
        self.location = (self.posx,self.posy)
        self.image = ss.image_at(self.sprite)

    def draw(self):
        self.screen.blit(self.image, self.location)

#Cursor class
class Cursor(object):
    def __init__(self, screen):  
        ss = Spritesheet('images/cursor.bmp')
        self.screen = screen
        self.posx = 0
        self.posy = 0
        self.location = (self.posx,self.posy)
        self.image = ss.image_at((0, 0, 40, 40))

    def get_location(self):
        return self.posx, self.posy

    def update(self, direction):
        if direction == 1:
            self.posy -= 40
        if direction == 2:
            self.posy += 40            
        if direction == 3:
            self.posx -= 40
        if direction == 4:
            self.posx += 40
        self.location = (self.posx,self.posy)
            
    def draw(self):
        self.screen.blit(self.image, self.location)
        
#Main  
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Image Movement')

#game clock
FPS = 20
timercounter = 0
updatetime = 10
clock = pygame.time.Clock()

trooper = Trooper(screen)
background = Background(screen)
cursor = Cursor(screen)

moveflag = 0
direction = 0

while 1:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()     
            elif event.key == pygame.K_UP:
                cursor.update(1)
            elif event.key == pygame.K_DOWN:
                cursor.update(2)
            elif event.key == pygame.K_LEFT:
                cursor.update(3)
            elif event.key == pygame.K_RIGHT:
                cursor.update(4)
            elif event.key == pygame.K_w and moveflag == 0:
                moveflag = 1
                direction = 1
            elif event.key == pygame.K_s and moveflag == 0:
                moveflag = 1
                direction = 2
            elif event.key == pygame.K_a and moveflag == 0:
                moveflag = 1
                direction = 3
            elif event.key == pygame.K_d and moveflag == 0:
                moveflag = 1
                direction = 4
                
    if moveflag > 0:
        moveflag = trooper.move(direction, 1)
    trooper.update(updatetime, timercounter)
    background.draw()
    trooper.draw()
    cursor.draw()
    pygame.display.flip()
    clock.tick(FPS)
    timercounter += 1
    if timercounter > updatetime:
        timercounter = 0
