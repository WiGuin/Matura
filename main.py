import pygame,os
pygame.init()
from pygame.locals import *
s='\\'

screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Matura-Projekt')

class Background(pygame.sprite.Sprite):
    def __init__(self):
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+"textures"+s+"Map"+s+"Map.png")
        self.x=-2000
        self.y=-2000

    def print(self):
        screen.blit(self.surf, (self.x,self.y))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+"textures"+s+"Characters"+s+"Character 1_1.2 ohne Items.png")
        self.surf=pygame.transform.scale(self.surf, (125,125))

    def print(self):
        screen.blit(self.surf, (438,438))

    def walk(self, key):
        if key=="w":
            background.y+=10
        if key=="s":
            background.y-=10
        if key=="a":
            background.x+=10
        if key=="d":
            background.x-=10
        #print(str(background.x) + " and " + str(background.y))

background = Background()
player = Player()

menu = False
gameon = True

while gameon:
    
    background.print()
    player.print()

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                menu=True

            if event.key == K_w:
                player.walk("w")
            if event.key == K_s:
                player.walk("s")
            if event.key == K_a:
                player.walk("a")
            if event.key == K_d:
                player.walk("d")

        elif event.type == QUIT:
            gameon=False

    pygame.display.flip()