import pygame,os
pygame.init()
from pygame.locals import *
s='\\'

screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Matura-Projekt')

def key_input(key, search):
    key = key.replace(search, '')
    return key

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
        self.health=10

    def print(self):
        screen.blit(self.surf, (438,438))

    def walk(self, key):
        if key=="w":
            if background.y<0:
                background.y+=10
        elif key=="wa" or key=="aw":
            if background.y<0:
                background.y+=7
            if background.x<0:
                background.x+=7
                if self.face=="right":
                    self.surf=pygame.transform.flip(self.surf, True, False)
                    self.face="left"
        elif key=="wd" or key=="dw":
            if background.y<0:
                background.y+=7
            if background.x>-4000:
                background.x-=7
                if self.face=="left":
                    self.surf=pygame.transform.flip(self.surf, True, False)
                    self.face="right"
        elif key=="s":
            if background.y>-4000:
                background.y-=7
        elif key=="sa" or key=="as":
            if background.y>-4000:
                background.y-=7
            if background.x<0:
                background.x+=7
                if self.face=="right":
                    self.surf=pygame.transform.flip(self.surf, True, False)
                    self.face="left"
        elif key=="sd" or key=="ds":
            if background.y>-4000:
                background.y-=7
            if background.x>-4000:
                background.x-=7
                if self.face=="left":
                    self.surf=pygame.transform.flip(self.surf, True, False)
                    self.face="right"
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

    def is_input(self, key): #Zum Bestimmen ob gerade ein input durchgeführt wird
        return(key!='')

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

class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+"textures"+s+"Goblin"+s+"Goblin00.png")
        self.surf=pygame.transform.scale(self.surf, (75,75))
        self.face='left'
        self.leg=10
        self.health=5
        self.x=5
        self.y=5

    def print(self):
        screen.blit(self.surf, (self.x,self.y))

    def walk(self, key):
        if 520>self.x:
            self.x+=5
        if 420<self.x:
            self.x-=5
        if 535>self.y:
            self.y+=5
        if 435<self.y:
            self.y-=5
        if key=='a':
            self.x+=10
        if key=='d':
            self.x-=10
        if key=='w':
            self.y+=10
        if key=='wa' or key=='aw':
            self.y+=7
            self.x+=7
        if key=='wd' or key=='dw':
            self.y+=7
            self.x-=7
        if key=='s':
            self.y-=10
        if key=='sa' or key=='as':
            self.y-=7
            self.x+=7
        if key=='sd' or key=='ds':
            self.y-=7
            self.x-=7

    def walk_animation(self):
            if 515>self.x:
                self.face='right'
            elif 425<self.x:
                self.face='left'
            if self.leg>=30:
                self.leg=10
            if self.leg<20:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+"textures"+s+"Goblin"+s+"Goblin_"+self.face+"_1.png")
            else:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+"textures"+s+"Goblin"+s+"Goblin_"+self.face+"_2.png")
            self.surf=pygame.transform.scale(self.surf, (75,75))
            if 520<self.x or self.x<420 or 535<self.y or self.y<435:
                self.leg+=1

background=Background()
player=Player()

enemy1=Enemy1()

clock=pygame.time.Clock()

menu=False #Für das Menü
gameon=True #Für den Game-Loop
key='' #Für die Inputs

while gameon:
    
    background.print()
    player.print()
    if player.is_input(key):
        player.walk_animation() #Für die Geh-Animation
    player.walk(key) #Movement

    enemy1.print()
    enemy1.walk(key)
    enemy1.walk_animation()

    print(key_input(key, 'd'))

    if key=='':
        player.surf=pygame.image.load(os.path.dirname(__file__)+s+"textures"+s+"Characters"+s+"character1_0.png")
        player.surf=pygame.transform.scale(player.surf, (125,125))
        if player.face=="left":
            player.surf=pygame.transform.flip(player.surf, True, False)

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                menu=True

            if event.key == K_w:
                key+='w'
            if event.key == K_s:
                key+='s'
            if event.key == K_a:
                key+='a'
            if event.key == K_d:
                key+='d'

        if event.type == KEYUP:
            if event.key == K_w:
                key=key_input(key, 'w')
            if event.key == K_s:
                key=key_input(key, 's')
            if event.key == K_a:
                key=key_input(key, 'a')
            if event.key == K_d:
                key=key_input(key, 'd')

        elif event.type == QUIT:
            gameon=False

    clock.tick(30)
    pygame.display.flip()