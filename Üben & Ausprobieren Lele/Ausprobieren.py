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

score_surface = test_font.render('My Game', False, (64,64,64))
score_rect = score_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/snail/snail1.png'). convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
        
        #if event.type == pygame.MOUSEMOTION:
        #    if player_rect.collidepoint(event.pos):
        #        print('hit')
    

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0,300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect,)
    pygame.draw.rect(screen, '#c0e8ec', score_rect,10)
    screen.blit(score_surface, score_rect)
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)
    snail_rect.right -= 4
    if snail_rect.right <= 0:
        snail_rect.right = 800
    
    #if player_rect.colliderect(snail_rect):
     #   print('collision')

    pygame.display.flip()
    clock.tick(60)