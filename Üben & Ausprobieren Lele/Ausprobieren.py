import pygame
import os
from random import randint
pygame.init()
from pygame.locals import *
screen = pygame.display.set_mode((800, 400))
s="\\"
class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/player/player_walk_1.png'). convert_alpha()
        self.rect = self.image.get_rect(midbottom = (200,300))

class Sword(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = # hier noch Bilddatei vom Schwert einfügen
		self.rect = # hier noch rect machen
        def sword_input(self):
            keys = pygame.key.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and collisions(sword, 'enemy'): #hier für Gegner enemy als platzhalter verwendet
                damage = 3

class Shield(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = # hier noch Bilddatei vom Schild einfügen
        self.rect = # hier noch rect machen
        shield_points = 10
        def shield_input(self):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT and collision('enemy weapon', shield): # hier für Gegner Waffe auch Platzhalter verwendet
                shield_points -= damage #hier wieder variable für Schaden


            
#group for items        
items = pygame.sprite.Group()
Sword.add(items())
Shield.add(items())
#das hier muss in Game Loop sein, damit das Schwert und Schild auch auf dem Screen, muss noch Screenname hinzugefügt werden, erscheint
items.draw('screen')
#player = Player()
player = pygame.sprite.GroupSingle()
player.add(Player())

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
                screen.blit(snail_surf, obstacle_rect)
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
def player_animation():
    global player_surface, player_index

    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]

pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
s="\\"
test_font = pygame.font.Font(os.path.dirname(__file__)+s+'Font/Pixeltype.ttf', 50)
game_active = False
score = 0

sky_surface = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/sky.png').convert()
ground_surface = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/ground.png').convert()

#obstacle
snail_frame_1 = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/snail/snail1.png'). convert_alpha()
snail_frame_2 = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/snail/snail2.png'). convert_alpha()
snail_frames = [snail_frame_1,snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

#snail_rect = snail_.get_rect(bottomright = (600, 300))
obstacle_rect_list = []

fly_frame_1 = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/fly/fly1.png'). convert_alpha()
fly_frame_2 = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/fly/fly2.png'). convert_alpha()
fly_frames = [fly_frame_1,fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]
#player
player_walk_1 = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/player/jump.png').convert_alpha()

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load(os.path.dirname(__file__)+s+'Graphics/player/player_walk_1.png'). convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400,200))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)



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
        if game_active:
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100), 210)))
            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                    fly_surf = fly_frames[fly_frame_index]
                else:
                    fly_frame_index = 0
                    fly_surf = fly_frames[fly_frame_index]
            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                    snail_surf = snail_frames[snail_frame_index]
                else:
                    snail_frame_index = 0
                    snail_surf = snail_frames[snail_frame_index]
                print(snail_frame_index)
    
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0,300))
        score = display_score()
        
        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surface, player_rect)
        player.draw(screen)

        #Obstacle movement
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