import pygame
import os
pygame.init()
from pygame.locals import *
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
s="\\"
test_font = pygame.font.Font(os.path.dirname(__file__)+s+'Font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/sky.png').convert()
ground_surface = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/ground.png').convert()
text_surface = test_font.render('My Game', False, 'Green')

snail_surface = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/snail/snail1.png'). convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (325, 50))
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)
    snail_rect.right -= 4
    if snail_rect.right <= 0:
        snail_rect.right = 800
    
    if player_rect.colliderect(snail_rect):
        print('collision')
    pygame.display.flip()
    clock.tick(60)