import pygame
import os
from random import randint
pygame.init()
from pygame.locals import *
start_time = 0
def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)
    return(current_time)
def start_screen():
    #game title
    game_title_text_font = pygame.font.Font(os.path.dirname(__file__)+s+'Font/Pixeltype.ttf', 50)
    game_title_surf = game_title_text_font.render('Pixel Runner', False, (111,196,169))
    game_title_rect = game_title_surf.get_rect(center = (400, 50))
    screen.blit(game_title_surf, game_title_rect)
    #score
    score_message = game_title_text_font.render(f'Your score: {score}', False, (111,196,169))
    score_message_rect = score_message.get_rect(center = (150, 200))
    screen.blit(score_message, score_message_rect)
    #start button
    game_startbutton_text_font = pygame.font.Font(os.path.dirname(__file__)+s+'Font/Pixeltype.ttf', 35)
    game_startbutton_surf = game_startbutton_text_font.render('Press Space to start', False, (111,196,169))
    game_startbutton_rect = game_startbutton_surf.get_rect(center = (400, 350))
    screen.blit(game_startbutton_surf, game_startbutton_rect)
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return(obstacle_list)
    else:
        return []
def collisions (player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
s="\\"
test_font = pygame.font.Font(os.path.dirname(__file__)+s+'Font/Pixeltype.ttf', 50)
game_active = False
score = 0

sky_surface = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/sky.png').convert()
ground_surface = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/ground.png').convert()

#obstacle
snail_surface = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/snail/snail1.png'). convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))
obstacle_rect_list = []

fly_surf = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/fly/fly1.png'). convert_alpha()

player_surface = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/player/player_walk_1.png'). convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400,200))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos)and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)
        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900,1100), 300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100), 210)))

    
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0,300))
        score = display_score()
        
        #Snail
        #screen.blit(snail_surface, snail_rect)
        #snail_rect.right -= 4
        #if snail_rect.right <= 0:
        #    snail_rect.right = 800

        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        #Obstacle movement(
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collision
        game_active = collisions(player_rect,obstacle_rect_list)
    
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        start_screen()
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0


    pygame.display.flip()
    clock.tick(60)