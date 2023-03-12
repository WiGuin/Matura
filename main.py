import pygame,os
pygame.init()
from pygame.locals import *
s='\\'

screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Matura-Projekt')

class Background(pygame.sprite.Sprite):
    def __init__(self):
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+"textures"+s+"Map"+s+"Map.png")
        self.x=-4500
        self.y=-4500

    def print(self):
        screen.blit(self.surf, (self.x,self.y))



background = Background()

menu = False
gameon = True

while gameon:
    
    background.print()

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                menu=True
        elif event.type == QUIT:
            gameon=False

    pygame.display.flip()