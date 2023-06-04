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
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Map'+s+'Map.png')
        self.x=-2000
        self.y=-2000

    def print(self):
        screen.blit(self.surf, (self.x,self.y))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Characters'+s+'character1_0.png')
        self.surf=pygame.transform.scale(self.surf, (125,125))
        self.face='right'
        self.leg=10 #Für die Walking-Animation
        self.health=10
        self.arm=0
        self.is_attacking=False
        self.inventory=['','']

    def print(self):
        screen.blit(self.surf, (438,438))

    def walk(self, key):
        if key=='w' or key=='wad' or key=='wda' or key=='awd' or key=='adw' or key=='daw' or key=='dwa':
            if background.y<0:
                background.y+=10
        elif key=='wa' or key=='aw':
            if background.y<0:
                background.y+=7
            if background.x<0:
                background.x+=7
                if self.face=='right':
                    self.surf=pygame.transform.flip(self.surf, True, False)
                    self.face='left'
        elif key=='wd' or key=='dw':
            if background.y<0:
                background.y+=7
            if background.x>-4000:
                background.x-=7
                if self.face=='left':
                    self.surf=pygame.transform.flip(self.surf, True, False)
                    self.face='right'
        elif key=='s' or key=='sad' or key=='sda' or key=='asd' or key=='ads' or key=='das' or key=='dsa':
            if background.y>-4000:
                background.y-=10
        elif key=='sa' or key=='as':
            if background.y>-4000:
                background.y-=7
            if background.x<0:
                background.x+=7
                if self.face=='right':
                    self.surf=pygame.transform.flip(self.surf, True, False)
                    self.face='left'
        elif key=='sd' or key=='ds':
            if background.y>-4000:
                background.y-=7
            if background.x>-4000:
                background.x-=7
                if self.face=='left':
                    self.surf=pygame.transform.flip(self.surf, True, False)
                    self.face='right'
        elif key=='a':
            if background.x<0:
                background.x+=10
                if self.face=='right':
                    self.surf=pygame.transform.flip(self.surf, True, False)
                    self.face='left'
        elif key=='d':
            if background.x>-4000:
                background.x-=10
                if self.face=='left':
                    self.surf=pygame.transform.flip(self.surf, True, False)
                    self.face='right'

    def is_input(self, key): #Zum Bestimmen ob gerade ein input durchgeführt wird
        return(key!='')

    def walk_animation(self):
        if self.leg>=30:
            self.leg=10
        if self.leg<20:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Characters'+s+'character1_1.png')
        else:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Characters'+s+'character1_2.png')
        self.surf=pygame.transform.scale(self.surf, (125,125))
        if self.face=='left':
            self.surf=pygame.transform.flip(self.surf, True, False)
        self.leg+=1

    def attack(self, x, y, enemy_health):
        if self.arm>=30:
            self.arm=0
        if self.arm==0:
            if self.face=='right':
                if x+37>=500:
                    if ((x-500)**2+(y-500)**2)**0.5<180:
                        enemy_health-=1
            if self.face=='left':
                if x+37<=500:
                    if ((x-500)**2+(y-500)**2)**0.5<180:
                        enemy_health-=1
        self.arm+=1
        return enemy_health
    
    def attack_animation(self):
        print()

class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Goblin'+s+'Goblin_1.png')
        self.surf=pygame.transform.scale(self.surf, (75,75))
        self.face='left'
        self.leg=0 #Für die Walking-animation
        self.arm=20 #Für die Attacken
        self.attack_clock=0 #Für die Attack-animation
        self.health=5
        self.x=750
        self.y=100

    def print(self):
        screen.blit(self.surf, (self.x,self.y))

    def walk(self, key):
        if 530>self.x:
            self.x+=5
        if 405<self.x:
            self.x-=5
        if 545>self.y:
            self.y+=5
        if 375<self.y:
            self.y-=5
        if key=='a':
            self.x+=10
        if key=='d':
            self.x-=10
        if key=='w' or key=='wad' or key=='wda' or key=='awd' or key=='adw' or key=='daw' or key=='dwa':
            self.y+=10
        if key=='wa' or key=='aw':
            self.y+=7
            self.x+=7
        if key=='wd' or key=='dw':
            self.y+=7
            self.x-=7
        if key=='s' or key=='sad' or key=='sda' or key=='asd' or key=='ads' or key=='das' or key=='dsa':
            self.y-=10
        if key=='sa' or key=='as':
            self.y-=7
            self.x+=7
        if key=='sd' or key=='ds':
            self.y-=7
            self.x-=7

    def walk_animation(self):
        if 460>self.x:
            self.face='right'
        else:
            self.face='left'
        if self.leg>=20:
            self.leg=0
        if self.leg<10:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Goblin'+s+'Goblin_1.png')
        else:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Goblin'+s+'Goblin_2.png')
        if self.face=='right':
            self.surf=pygame.transform.flip(self.surf, True, False)
        self.surf=pygame.transform.scale(self.surf, (75,75))
        self.leg+=1

    def attack(self, player_health):
        if 530>self.x and self.x>400 and 545>self.y and self.y>370:
            if self.arm>=30:
                self.arm=0
                player_health-=1
                print(player_health)
            self.arm+=1
        else:
            self.arm=20
        return(player_health)
        
    def attack_animation(self):
        if 530>self.x and self.x>400 and 545>self.y and self.y>370:
            if self.attack_clock>=60:
                self.attack_clock=0
            if self.attack_clock<30:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Goblin'+s+'Goblin_attack_1.png')
            else:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Goblin'+s+'Goblin_attack_2.png')
            if self.face=='right':
                self.surf=pygame.transform.flip(self.surf, True, False)
            self.surf=pygame.transform.scale(self.surf, (75,75))
            self.attack_clock+=1


background=Background()

player=Player()

enemy1=Enemy1()

clock=pygame.time.Clock()
gameon=True #Für den Game-Loop
key='' #Für die Inputs

while gameon:

    background.print()

    player.print()
    if player.is_input(key):
        player.walk_animation()
    player.walk(key)
    if player.is_attacking:
        enemy1.health=player.attack(enemy1.x, enemy1.y, enemy1.health)
    
    enemy1.print()
    enemy1.walk(key)
    enemy1.walk_animation()
    player.health=enemy1.attack(player.health)
    enemy1.attack_animation()
    if enemy1.health<=0:
        enemy1.x=300
        enemy1.y=-100
        enemy1.health=5

    if key=='':
        player.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Characters'+s+'character1_0.png')
        player.surf=pygame.transform.scale(player.surf, (125,125))
        if player.face=='left':
            player.surf=pygame.transform.flip(player.surf, True, False)

    for event in pygame.event.get():

        if event.type == KEYDOWN:

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

        if pygame.mouse.get_pressed()[0]:
            player.is_attacking=True
        else:
            player.is_attacking=False


    clock.tick(30)
    pygame.display.flip()