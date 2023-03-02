import pygame
pygame.init()
from pygame.locals import *
screen = pygame.display.set_mode((800, 400))

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()

    pygame.display.flip()