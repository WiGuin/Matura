import pygame
pygame.init()
from pygame.locals import *
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Graphics/sky.png')
ground_surface = pygame.image.load('Graphics/ground.png')
text_surface = test_font.render('My Game', False, 'Black')

snail_surface = pygame.image.load('Graphics/snail/snail1.png')
snail_x_pos = 600

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (325, 50))
    screen.blit(snail_surface, (snail_x_pos, 250))
    snail_x_pos = snail_x_pos - 4
    if snail_x_pos < -50:
        snail_x_pos = 800
    pygame.display.flip()
    clock.tick(60)