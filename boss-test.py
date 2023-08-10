import pygame,os
pygame.init()
from pygame.locals import *
s='\\'

screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Boss-test')

class Background(pygame.sprite.Sprite):
    def __init__(self):
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Map'+s+'Map.png')
        self.x=-2000
        self.y=-2000

    def print(self):
        screen.blit(self.surf, (self.x,self.y))

class Boss1(pygame.sprite.Sprite):
    def __init__(self):
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'boss-test'+s+'test.png')
        self.x=500
        self.y=250
    
    def print(self):
        screen.blit(self.surf, (self.x,self.y))

background=Background()

boss1=Boss1()

clock=pygame.time.Clock()

gameon=True
while gameon:
    
    background.print()
    boss1.print()

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                gameon=False
        elif event.type == QUIT:
            gameon=False

    clock.tick(30)
    pygame.display.flip()