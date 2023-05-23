import pygame,os
pygame.init()
from pygame.locals import *
s='\\'

screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Matura-Projekt')

def is_input(key): #Zum Bestimmen ob gerade ein input durchgeführt wird
    return(key!='')

class Background(pygame.sprite.Sprite):
    def __init__(self):
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+"textures"+s+"Map"+s+"Map.png")
        self.x=-2000
        self.y=-2000

    def print(self):
        screen.blit(self.surf, (self.x,self.y))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+"textures"+s+"Characters"+s+"character1_0.png")
        self.surf=pygame.transform.scale(self.surf, (125,125))
        self.face="right"
        self.leg=10

    def print(self):
        screen.blit(self.surf, (438,438))

    def walk(self, key):
        if key=="w":
            if background.y<0:
                background.y+=10
        elif key=="s":
            if background.y>-4000:
                background.y-=10
        elif key=="a":
            if background.x<0:
                background.x+=10
                if self.face=="right":
                    self.surf=pygame.transform.flip(self.surf, True, False)
                    self.face="left"
        elif key=="d":
            if background.x>-4000:
                background.x-=10
                if self.face=="left":
                    self.surf=pygame.transform.flip(self.surf, True, False)
                    self.face="right"

    def walk_animation(self):
        if self.leg>=30:
            self.leg=10
        if self.leg<20:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+"textures"+s+"Characters"+s+"character1_1.png")
        else:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+"textures"+s+"Characters"+s+"character1_2.png")
        self.surf=pygame.transform.scale(self.surf, (125,125))
        if self.face=="left":
            player.surf=pygame.transform.flip(player.surf, True, False)
        self.leg+=1

background=Background()
player=Player()
clock=pygame.time.Clock()

menu=False #Für das Menü
gameon=True #Für den Game-Loop
key='' #Für die Inputs

while gameon:
    
    background.print()
    player.print()
    if is_input(key):
        player.walk_animation() #Für die Geh-Animation
    player.walk(key) #Movement

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                menu=True

            if event.key == K_w:
                key='w'
            if event.key == K_s:
                key='s'
            if event.key == K_a:
                key='a'
            if event.key == K_d:
                key='d'

        if event.type == KEYUP:
            key=''
            player.surf=pygame.image.load(os.path.dirname(__file__)+s+"textures"+s+"Characters"+s+"character1_0.png")
            player.surf=pygame.transform.scale(player.surf, (125,125))
            if player.face=="left":
                player.surf=pygame.transform.flip(player.surf, True, False)

        elif event.type == QUIT:
            gameon=False

    clock.tick(30)
    pygame.display.flip()