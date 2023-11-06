import pygame, os, time, random
pygame.init()
from pygame.locals import *
s='\\'

screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Matura-Projekt')

#Zum Entfernen von Buchstaben von "key"
def key_not_input(key, search):
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
    def __init__(self, character):
        self.character = character
        self.face='right'
        self.leg=10 #Für die Walking-Animation
        self.health=10
        self.arm=10
        self.is_attacking=False
        self.inventory=['1','1']
        self.surf = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Character'+str(self.character)+s+'character'+str(self.character)+'_'+self.inventory[0]+'_0.png')
        self.surf = pygame.transform.scale(self.surf, (125,125))
        self.x=438
        self.y=438
        self.font=pygame.font.Font('freesansbold.ttf', 32)
        self.stage = 1
        self.shield = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Items'+s+'Schild_'+self.inventory[1]+'.png')
        self.shield = pygame.transform.scale(self.shield, (100,100))
        self.block = False
        self.fireball = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Fähigkeiten'+s+'Fireball.png')
        self.heal = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Fähigkeiten'+s+'Heal.png')
        self.heal = pygame.transform.scale(self.heal, (125,125))
        self.ability_true = 0
        self.ability_x = 500
        self.ability_y = 500
        self.ability_direction = None
        self.ability_cooldown = 0
        self.coin = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Shop'+s+'Coins.png')
        self.coin_count = 0
        self.round_timer = 60

    def print(self):
        screen.blit(self.surf, (self.x,self.y))

        if self.block:
            if self.face=='right':
                screen.blit(self.shield, (446,455))
            else:
                screen.blit(self.shield, (453,455))
        else:
            if self.face=='right':
                screen.blit(self.shield, (430,455))
            else:
                screen.blit(self.shield, (468,455))
        screen.blit(self.font.render('HP: '+str(self.health), True, (255,255,255)), (5,5))
        screen.blit(self.coin, (925,25))
        if self.coin_count < 10:
            screen.blit(self.font.render(str(self.coin_count), True, (255,255,255)), (890,35))
        elif self.coin_count < 100:
            screen.blit(self.font.render(str(self.coin_count), True, (255,255,255)), (870,35))
        else:
            screen.blit(self.font.render(str(self.coin_count), True, (255,255,255)), (850,35))

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
        elif key=='a' or key=='aws' or key=='asw' or key=='was' or key=='wsa' or key=='saw' or key=='swa':
            if background.x<0:
                background.x+=10
                if self.face=='right':
                    self.surf=pygame.transform.flip(self.surf, True, False)
                    self.face='left'
        elif key=='d' or key=='dws' or key=='dsw' or key=='wds' or key=='wsd' or key=='sdw' or key=='swd':
            if background.x>-4000:
                background.x-=10
                if self.face=='left':
                    self.surf=pygame.transform.flip(self.surf, True, False)
                    self.face='right'

    def is_input(self, key): #Zum Bestimmen ob gerade ein input durchgeführt wird
        return(key!='')

    def attack(self, x, y, enemy_health, type):
        gegner_leben = enemy_health
        if type=='1':
            if self.arm>=30:
                self.arm=0
            if self.arm==0:
                if self.face=='right':
                    if 460<x<575 and 400<y<475:
                        gegner_leben-=int(self.inventory[0])
                if self.face=='left':
                    if 350<x<465 and 400<y<475:
                        gegner_leben-=int(self.inventory[0])
        if type=='2':
            if self.arm>=30:
                self.arm=0
            if self.arm==0:
                if self.face=='right':
                    if 400<x<550 and 330<y<450:
                        gegner_leben-=int(self.inventory[0])
                if self.face=='left':
                    if 250<x<400 and 330<y<450:
                        gegner_leben-=int(self.inventory[0])
        if type=='3':
            if self.arm>=30:
                self.arm=0
            if self.arm==0:
                if self.face=='right':
                    if 355<x<525 and 280<y<410:
                        gegner_leben-=int(self.inventory[0])
                if self.face=='left':
                    if 215<x<385 and 280<y<410:
                        gegner_leben-=int(self.inventory[0])
        if type=='4':
            if self.arm>=30:
                self.arm=0
            if self.arm==0:
                if self.face=='right':
                    if 300<x<500 and 200<y<450:
                        gegner_leben-=int(self.inventory[0])
                if self.face=='left':
                    if 200<x<400 and 200<y<450:
                        gegner_leben-=int(self.inventory[0])
        if type=='5':
            if self.arm>=30:
                self.arm=0
            if self.arm==0:
                if self.face=='right':
                    if 300<x<530 and 200<y<420:
                        gegner_leben-=int(self.inventory[0])
                if self.face=='left':
                    if 175<x<405 and 200<y<420:
                        gegner_leben-=int(self.inventory[0])
        return(gegner_leben)

    def animation(self, key):
        if self.is_attacking and key!='' and self.block != True:
            if self.leg>=30:
                self.leg=10
            if self.leg<20:
                if self.arm>=29 or self.arm<5:
                    self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Character'+str(self.character)+s+'character'+str(self.character)+'_'+self.inventory[0]+'_1_attack_1.png')
                    self.surf=pygame.transform.scale(self.surf, (229,125))
                    self.x=386
                else:
                    self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Character'+str(self.character)+s+'character'+str(self.character)+'_'+self.inventory[0]+'_1_attack_0.png')
                    self.surf=pygame.transform.scale(self.surf, (125,125))
                    self.x=438
            else:
                if self.arm==29 or self.arm<5:
                    self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Character'+str(self.character)+s+'character'+str(self.character)+'_'+self.inventory[0]+'_2_attack_1.png')
                    self.surf=pygame.transform.scale(self.surf, (229,125))
                    self.x=386
                else:
                    self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Character'+str(self.character)+s+'character'+str(self.character)+'_'+self.inventory[0]+'_2_attack_0.png')
                    self.surf=pygame.transform.scale(self.surf, (125,125))
                    self.x=438
        elif self.is_attacking == False and key!='':
            if self.leg>=30:
                self.leg=10
            if self.leg<20:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Character'+str(self.character)+s+'character'+str(self.character)+'_'+self.inventory[0]+'_1.png')
            else:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Character'+str(self.character)+s+'character'+str(self.character)+'_'+self.inventory[0]+'_2.png')
            self.surf=pygame.transform.scale(self.surf, (125,125))
            self.x=438
        elif self.is_attacking and key=='' and self.block != True:
            if self.leg>=30:
                self.leg=10
            if self.arm>=29 or self.arm<5:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Character'+str(self.character)+s+'character'+str(self.character)+'_'+self.inventory[0]+'_0_attack_1.png')
                self.surf=pygame.transform.scale(self.surf, (229,125))
                self.x=386
            else:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Character'+str(self.character)+s+'character'+str(self.character)+'_'+self.inventory[0]+'_0_attack_0.png')
                self.surf=pygame.transform.scale(self.surf, (125,125))
                self.x=438
        elif key=='':
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Character'+str(self.character)+s+'character'+str(self.character)+'_'+player.inventory[0]+'_0.png')
            self.surf=pygame.transform.scale(self.surf, (125,125))
            self.x=438
        else:
            if self.leg>=30:
                self.leg=10
            if self.leg<20:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Character'+str(self.character)+s+'character'+str(self.character)+'_'+self.inventory[0]+'_1.png')
            else:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Character'+str(self.character)+s+'character'+str(self.character)+'_'+self.inventory[0]+'_2.png')
            self.surf=pygame.transform.scale(self.surf, (125,125))
            self.x=438
        if self.face=='left':
            self.surf=pygame.transform.flip(self.surf, True, False)
        self.leg+=1

    def ability(self, x, y, enemy_health, enemy_type):
        if self.character == 1:
            if self.ability_true == 0:
                self.ability_direction = self.face
            if 0 < self.ability_true < 70:

                if self.ability_cooldown == 0:
                    if enemy_type == '1':
                        if abs(self.ability_x-x)<50 and abs(self.ability_y-y)<50:
                            enemy_health-=1
                            self.ability_cooldown += 1
                    elif enemy_type == '2':
                        if abs(self.ability_x-x)<50 and -50<(self.ability_y-y):
                            enemy_health-=1
                            self.ability_cooldown += 1
                    elif enemy_type == '3':
                        if 0 < (self.ability_x-x) < 150 and -100<(self.ability_y-y):
                            enemy_health-=1
                            self.ability_cooldown += 1

            if self.ability_true >= 70:
                self.ability_x = 500
                self.ability_y = 500
                self.ability_cooldown = 0
                self.ability_true = 0
        
        return(enemy_health)

    def ability_animation(self, key):
        if self.character == 1:
            if 0 < self.ability_true < 70:

                if key=='a' or key=='aws' or key=='asw' or key=='was' or key=='wsa' or key=='saw' or key=='swa':
                    self.ability_x+=10
                if key=='d' or key=='dws' or key=='dsw' or key=='wds' or key=='wsd' or key=='sdw' or key=='swd':
                    self.ability_x-=10
                if key=='w' or key=='wad' or key=='wda' or key=='awd' or key=='adw' or key=='daw' or key=='dwa':
                    self.ability_y+=10
                if key=='s' or key=='sad' or key=='sda' or key=='asd' or key=='ads' or key=='das' or key=='dsa':
                    self.ability_y-=10
                if key=='wa' or key=='aw':
                    self.ability_x+=50**0.5
                    self.ability_y+=50**0.5
                if key=='wd' or key=='dw':
                    self.ability_x-=50**0.5
                    self.ability_y+=50**0.5
                if key=='sa' or key=='as':
                    self.ability_x+=50**0.5
                    self.ability_y-=50**0.5
                if key=='sd' or key=='ds':
                    self.ability_x-=50**0.5
                    self.ability_y-=50**0.5

                if self.ability_cooldown == 0:
                    if self.ability_direction == 'right':
                        screen.blit(self.fireball, (self.ability_x,self.ability_y))
                        self.ability_x += 10
                    else:
                        screen.blit(pygame.transform.flip(self.fireball, True, False), (self.ability_x,self.ability_y))
                        self.ability_x -= 10
                elif self.ability_cooldown < 150:
                    self.ability_cooldown += 1
                else:
                    self.ability_cooldown = 0

                self.ability_true += 1

        if self.character == 2:
            if 0 < self.ability_true < 40:
                screen.blit(self.heal, (438,438))
                self.ability_true += 1
            if self.ability_true == 40:
                if self.health<10:
                    self.health += 1
                self.ability_true += 1
            if 40 < self.ability_true < 750:
                self.ability_true += 1
            if self.ability_true == 750:
                self.ability_true = 0

class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Goblin'+s+'Goblin_1.png')
        self.surf=pygame.transform.scale(self.surf, (75,75))
        self.face='left'
        self.leg=0 #Für die Walking-animation
        self.arm=20 #Für die Attacken
        self.attack_clock=0 #Für die Attack-animation
        self.health=5
        self.x=random.randint(-1500,1500)
        self.y=random.randint(-1500,1500)
        self.type='1'

    def print(self):
        screen.blit(self.surf, (self.x,self.y))

    def walk(self, key, x, y):
        if 530>self.x:
            self.x+=5
        if 405<self.x:
            self.x-=5
        if 545>self.y:
            self.y+=5
        if 375<self.y:
            self.y-=5
        if key=='a' or key=='aws' or key=='asw' or key=='was' or key=='wsa' or key=='saw' or key=='swa':
            if x<0:
                self.x+=10
        if key=='d' or key=='dws' or key=='dsw' or key=='wds' or key=='wsd' or key=='sdw' or key=='swd':
            if x>-4000:
                self.x-=10
        if key=='w' or key=='wad' or key=='wda' or key=='awd' or key=='adw' or key=='daw' or key=='dwa':
            if y<0:
                self.y+=10
        if key=='wa' or key=='aw':
            if x<0:
                self.x+=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='wd' or key=='dw':
            if x>-4000:
                self.x-=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='s' or key=='sad' or key=='sda' or key=='asd' or key=='ads' or key=='das' or key=='dsa':
            if y>-4000:
                self.y-=10
        if key=='sa' or key=='as':
            if x<0:
                self.x+=50**0.5
            if y>-4000:
                self.y-=50**0.5
        if key=='sd' or key=='ds':
            if x>-4000:
                self.x-=50**0.5
            if y>-4000:
                self.y-=50**0.5

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

    def attack(self, player_health, block, shield):
        if 530>self.x and self.x>400 and 545>self.y and self.y>370:
            if self.arm>=30:
                self.arm=0
                if block and (1-shield) >= 0:
                    player_health-=(1-shield)
                elif block != True:
                    player_health-=1
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

    def update(self, key, x, y):
        self.print()
        self.walk(key, x, y)
        self.walk_animation()
        self.attack_animation()

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Skelett'+s+'Skeleton_0.png')
        self.surf=pygame.transform.scale(self.surf, (75,75))
        self.face='left'
        self.leg=0 #Für die Walking-animation
        self.arm=20 #Für die Attacken
        self.attack_clock=0 #Für die Attack-animation
        self.health=5
        self.x=random.randint(-1500,1500)
        self.y=random.randint(-1500,1500)
        self.type='1'

    def print(self):
        screen.blit(self.surf, (self.x,self.y))

    def walk(self, key, x, y):
        if 530>self.x:
            self.x+=5
        if 405<self.x:
            self.x-=5
        if 545>self.y:
            self.y+=5
        if 375<self.y:
            self.y-=5
        if key=='a' or key=='aws' or key=='asw' or key=='was' or key=='wsa' or key=='saw' or key=='swa':
            if x<0:
                self.x+=10
        if key=='d' or key=='dws' or key=='dsw' or key=='wds' or key=='wsd' or key=='sdw' or key=='swd':
            if x>-4000:
                self.x-=10
        if key=='w' or key=='wad' or key=='wda' or key=='awd' or key=='adw' or key=='daw' or key=='dwa':
            if y<0:
                self.y+=10
        if key=='wa' or key=='aw':
            if x<0:
                self.x+=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='wd' or key=='dw':
            if x>-4000:
                self.x-=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='s' or key=='sad' or key=='sda' or key=='asd' or key=='ads' or key=='das' or key=='dsa':
            if y>-4000:
                self.y-=10
        if key=='sa' or key=='as':
            if x<0:
                self.x+=50**0.5
            if y>-4000:
                self.y-=50**0.5
        if key=='sd' or key=='ds':
            if x>-4000:
                self.x-=50**0.5
            if y>-4000:
                self.y-=50**0.5

    def walk_animation(self):
        if 460>self.x:
            self.face='right'
        else:
            self.face='left'
        if self.leg>=20:
            self.leg=0
        if self.leg<10:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Skelett'+s+'Skeleton_1.png')
        else:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Skelett'+s+'Skeleton_2.png')
        self.surf=pygame.transform.scale(self.surf, (75,75))
        self.leg+=1

    def attack(self, player_health, block, shield):
        if 530>self.x and self.x>400 and 545>self.y and self.y>370:
            if self.arm>=30:
                self.arm=0
                if block and (1-shield) >= 0:
                    player_health-=(1-shield)
                elif block != True:
                    player_health-=1
            self.arm+=1
        else:
            self.arm=20
        return(player_health)
        
    def attack_animation(self):
        if 530>self.x and self.x>400 and 545>self.y and self.y>370:
            if self.attack_clock >= 30:
                self.attack_clock = 0
            if self.attack_clock < 10:
                if self.face == 'left':
                    self.surf = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Skelett'+s+'Skeleton_attack1(2).png')
                else:
                    self.surf = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Skelett'+s+'Skeleton_attack1.png')
            elif self.attack_clock < 20:
                if self.face == 'left':
                    self.surf = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Skelett'+s+'Skeleton_attack2(2).png')
                else:
                    self.surf = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Skelett'+s+'Skeleton_attack2.png')
            elif self.attack_clock < 25:
                if self.face == 'left':
                    self.surf = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Skelett'+s+'Skeleton_attack3(2).png')
                else:
                    self.surf = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Skelett'+s+'Skeleton_attack3.png')
            else:
                if self.face == 'left':
                    self.surf = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Skelett'+s+'Skeleton_attack4(2).png')
                else:
                    self.surf = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Skelett'+s+'Skeleton_attack4.png')

            if self.attack_clock == 20:
                if self.face == 'left':
                    self.x -= 9
                else:
                    self.x += 9
            if self.attack_clock == 0:
                if self.face == 'left':
                    self.x += 9
                else:
                    self.x -= 9

            self.surf=pygame.transform.scale(self.surf, (75,75))
            self.attack_clock+=1

    def update(self, key, x, y):
        self.print()
        self.walk(key, x, y)
        self.walk_animation()
        self.attack_animation()

class Enemy3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'mittlerer Goblin'+s+'Goblin_0.png')
        self.face='right'
        self.leg=0 #Für die Walking-animation
        self.arm=20 #Für die Attacken
        self.attack_clock=0 #Für die Attack-animation
        self.health=8
        self.x=random.randint(-1500,1500)
        self.y=random.randint(-1500,1500)
        self.type='2'

    def print(self):
        screen.blit(self.surf, (self.x,self.y))

    def walk(self, key, x, y):
        if 490>self.x:
            self.x+=4
        if 350<self.x:
            self.x-=4
        if 440>self.y:
            self.y+=4
        if 510<self.y:
            self.y-=4
        if key=='a' or key=='aws' or key=='asw' or key=='was' or key=='wsa' or key=='saw' or key=='swa':
            if x<0:
                self.x+=10
        if key=='d' or key=='dws' or key=='dsw' or key=='wds' or key=='wsd' or key=='sdw' or key=='swd':
            if x>-4000:
                self.x-=10
        if key=='w' or key=='wad' or key=='wda' or key=='awd' or key=='adw' or key=='daw' or key=='dwa':
            if y<0:
                self.y+=10
        if key=='wa' or key=='aw':
            if x<0:
                self.x+=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='wd' or key=='dw':
            if x>-4000:
                self.x-=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='s' or key=='sad' or key=='sda' or key=='asd' or key=='ads' or key=='das' or key=='dsa':
            if y>-4000:
                self.y-=10
        if key=='sa' or key=='as':
            if x<0:
                self.x+=50**0.5
            if y>-4000:
                self.y-=50**0.5
        if key=='sd' or key=='ds':
            if x>-4000:
                self.x-=50**0.5
            if y>-4000:
                self.y-=50**0.5

    def walk_animation(self):
        if 450>self.x:
            self.face='right'
        else:
            self.face='left'
        if self.leg>=20:
            self.leg=0
        if self.leg<10:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'mittlerer Goblin'+s+'Goblin_1.png')
        else:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'mittlerer Goblin'+s+'Goblin_2.png')
        if self.face=='left':
            self.surf=pygame.transform.flip(self.surf, True, False)
        self.leg+=1

    def attack(self, player_health, block, shield):
        if 490>self.x and self.x>340 and 510>self.y and self.y>440:
            if self.arm>=60:
                self.arm=0
            if self.arm==50:
                if block and (2-shield) >= 0:
                    player_health-=(2-shield)
                elif block != True:
                    player_health-=2
            self.arm+=1
        else:
            self.arm=20
        return(player_health)
        
    def attack_animation(self):
        if 490>self.x and self.x>340 and 510>self.y and self.y>440:
            if self.attack_clock>=60:
                self.attack_clock=0
            if self.attack_clock < 10:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'mittlerer Goblin'+s+'Goblin_attack1.png')
            elif self.attack_clock < 20:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'mittlerer Goblin'+s+'Goblin_attack2.png')
            else:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'mittlerer Goblin'+s+'Goblin_attack3.png')
            if self.face=='left':
                self.surf=pygame.transform.flip(self.surf, True, False)
            self.attack_clock+=1

    def update(self, key, x, y):
        self.print()
        self.walk(key, x, y)
        self.walk_animation()
        self.attack_animation()

class Enemy4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'mittleres Skelett'+s+'Skeleton_0.png')
        self.face='right'
        self.leg=0 #Für die Walking-animation
        self.arm=20 #Für die Attacken
        self.attack_clock=0 #Für die Attack-animation
        self.health=8
        self.x=random.randint(-1500,1500)
        self.y=random.randint(-1500,1500)
        self.type='2'

    def print(self):
        screen.blit(self.surf, (self.x,self.y))

    def walk(self, key, x, y):
        if 490>self.x:
            self.x+=4
        if 350<self.x:
            self.x-=4
        if 440>self.y:
            self.y+=4
        if 510<self.y:
            self.y-=4
        if key=='a' or key=='aws' or key=='asw' or key=='was' or key=='wsa' or key=='saw' or key=='swa':
            if x<0:
                self.x+=10
        if key=='d' or key=='dws' or key=='dsw' or key=='wds' or key=='wsd' or key=='sdw' or key=='swd':
            if x>-4000:
                self.x-=10
        if key=='w' or key=='wad' or key=='wda' or key=='awd' or key=='adw' or key=='daw' or key=='dwa':
            if y<0:
                self.y+=10
        if key=='wa' or key=='aw':
            if x<0:
                self.x+=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='wd' or key=='dw':
            if x>-4000:
                self.x-=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='s' or key=='sad' or key=='sda' or key=='asd' or key=='ads' or key=='das' or key=='dsa':
            if y>-4000:
                self.y-=10
        if key=='sa' or key=='as':
            if x<0:
                self.x+=50**0.5
            if y>-4000:
                self.y-=50**0.5
        if key=='sd' or key=='ds':
            if x>-4000:
                self.x-=50**0.5
            if y>-4000:
                self.y-=50**0.5

    def walk_animation(self):
        if 450>self.x:
            self.face='right'
        else:
            self.face='left'
        if self.leg>=20:
            self.leg=0
        if self.leg<10:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'mittleres Skelett'+s+'Skeleton_1.png')
        else:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'mittleres Skelett'+s+'Skeleton_2.png')
        if self.face=='left':
            self.surf=pygame.transform.flip(self.surf, True, False)
        self.leg+=1

    def attack(self, player_health, block, shield):
        if 490>self.x and self.x>340 and 510>self.y and self.y>440:
            if self.arm>=60:
                self.arm=0
            if self.arm==50:
                if block and (2-shield) >= 0:
                    player_health-=(2-shield)
                elif block != True:
                    player_health-=2
            self.arm+=1
        else:
            self.arm=20
        return(player_health)
        
    def attack_animation(self):
        if 490>self.x and self.x>340 and 510>self.y and self.y>440:
            if self.attack_clock>=60:
                self.attack_clock=0
            if self.attack_clock < 10:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'mittleres Skelett'+s+'Skeleton_attack_1.png')
            elif self.attack_clock < 20:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'mittleres Skelett'+s+'Skeleton_attack_2.png')
            else:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'mittleres Skelett'+s+'Skeleton_attack_3.png')
            if self.face=='left':
                self.surf=pygame.transform.flip(self.surf, True, False)
            self.attack_clock+=1

    def update(self, key, x, y):
        self.print()
        self.walk(key, x, y)
        self.walk_animation()
        self.attack_animation()

class Enemy5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'grosser Goblin'+s+'Goblin_0.png')
        self.surf=pygame.transform.scale(self.surf, (267,267))
        self.face='right'
        self.leg=0 #Für die Walking-animation
        self.arm=20 #Für die Attacken
        self.attack_clock=0 #Für die Attack-animation
        self.health=10
        self.x=random.randint(-1500,1500)
        self.y=random.randint(-1500,1500)
        self.type='3'

    def print(self):
        screen.blit(self.surf, (self.x,self.y))

    def walk(self, key, x, y):
        if 505>self.x:
            self.x+=3
        if 290<self.x:
            self.x-=3
        if 455>self.y:
            self.y+=3
        if 500<self.y:
            self.y-=3
        if key=='a' or key=='aws' or key=='asw' or key=='was' or key=='wsa' or key=='saw' or key=='swa':
            if x<0:
                self.x+=10
        if key=='d' or key=='dws' or key=='dsw' or key=='wds' or key=='wsd' or key=='sdw' or key=='swd':
            if x>-4000:
                self.x-=10
        if key=='w' or key=='wad' or key=='wda' or key=='awd' or key=='adw' or key=='daw' or key=='dwa':
            if y<0:
                self.y+=10
        if key=='wa' or key=='aw':
            if x<0:
                self.x+=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='wd' or key=='dw':
            if x>-4000:
                self.x-=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='s' or key=='sad' or key=='sda' or key=='asd' or key=='ads' or key=='das' or key=='dsa':
            if y>-4000:
                self.y-=10
        if key=='sa' or key=='as':
            if x<0:
                self.x+=50**0.5
            if y>-4000:
                self.y-=50**0.5
        if key=='sd' or key=='ds':
            if x>-4000:
                self.x-=50**0.5
            if y>-4000:
                self.y-=50**0.5

    def walk_animation(self):
        if 450>self.x:
            self.face='right'
        else:
            self.face='left'
        if self.leg>=20:
            self.leg=0
        if self.leg<10:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'grosser Goblin'+s+'Goblin_1.png')
        else:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'grosser Goblin'+s+'Goblin_2.png')
        if self.face=='left':
            self.surf=pygame.transform.flip(self.surf, True, False)
        self.surf=pygame.transform.scale(self.surf, (267,267))
        self.leg+=1

    def attack(self, player_health, block, shield):
        if 505>self.x and self.x>280 and 500>self.y and self.y>455:
            if self.arm>=60:
                self.arm=0
                if block and (3-shield) >= 0:
                    player_health-=(3-shield)
                elif block != True:
                    player_health-=3
            self.arm+=1
        else:
            self.arm=20
        return(player_health)
        
    def attack_animation(self):
        if 505>self.x and self.x>280 and 500>self.y and self.y>455:
            if self.attack_clock>=60:
                self.attack_clock=0
            if self.attack_clock < 10:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'grosser Goblin'+s+'Goblin_attack1.png')
            elif self.attack_clock < 20:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'grosser Goblin'+s+'Goblin_attack2.png')
            elif self.attack_clock < 25:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'grosser Goblin'+s+'Goblin_attack3.png')
            else:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'grosser Goblin'+s+'Goblin_attack4.png')
            if self.face=='left':
                self.surf=pygame.transform.flip(self.surf, True, False)
            self.surf=pygame.transform.scale(self.surf, (267,267))
            self.attack_clock+=1

    def update(self, key, x, y):
        self.print()
        self.walk(key, x, y)
        self.walk_animation()
        self.attack_animation()

class Enemy6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'grosses Skelett'+s+'Skeleton_0.png')
        self.surf=pygame.transform.scale(self.surf, (267,267))
        self.face='right'
        self.leg=0 #Für die Walking-animation
        self.arm=20 #Für die Attacken
        self.attack_clock=0 #Für die Attack-animation
        self.health=10
        self.x=random.randint(-1500,1500)
        self.y=random.randint(-1500,1500)
        self.type='3'

    def print(self):
        screen.blit(self.surf, (self.x,self.y))

    def walk(self, key, x, y):
        if 505>self.x:
            self.x+=3
        if 290<self.x:
            self.x-=3
        if 455>self.y:
            self.y+=3
        if 500<self.y:
            self.y-=3
        if key=='a' or key=='aws' or key=='asw' or key=='was' or key=='wsa' or key=='saw' or key=='swa':
            if x<0:
                self.x+=10
        if key=='d' or key=='dws' or key=='dsw' or key=='wds' or key=='wsd' or key=='sdw' or key=='swd':
            if x>-4000:
                self.x-=10
        if key=='w' or key=='wad' or key=='wda' or key=='awd' or key=='adw' or key=='daw' or key=='dwa':
            if y<0:
                self.y+=10
        if key=='wa' or key=='aw':
            if x<0:
                self.x+=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='wd' or key=='dw':
            if x>-4000:
                self.x-=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='s' or key=='sad' or key=='sda' or key=='asd' or key=='ads' or key=='das' or key=='dsa':
            if y>-4000:
                self.y-=10
        if key=='sa' or key=='as':
            if x<0:
                self.x+=50**0.5
            if y>-4000:
                self.y-=50**0.5
        if key=='sd' or key=='ds':
            if x>-4000:
                self.x-=50**0.5
            if y>-4000:
                self.y-=50**0.5

    def walk_animation(self):
        if 450>self.x:
            self.face='right'
        else:
            self.face='left'
        if self.leg>=20:
            self.leg=0
        if self.leg<10:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'grosses Skelett'+s+'Skeleton_1.png')
        else:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'grosses Skelett'+s+'Skeleton_2.png')
        if self.face=='left':
            self.surf=pygame.transform.flip(self.surf, True, False)
        self.surf=pygame.transform.scale(self.surf, (267,267))
        self.leg+=1

    def attack(self, player_health, block, shield):
        if 505>self.x and self.x>280 and 500>self.y and self.y>455:
            if self.arm>=60:
                self.arm=0
            if self.arm == 50:
                if block and (3-shield) >= 0:
                    player_health-=(3-shield)
                elif block != True:
                    player_health-=3
            self.arm+=1
        else:
            self.arm=20
        return(player_health)
        
    def attack_animation(self):
        if 505>self.x and self.x>280 and 500>self.y and self.y>455:
            if self.attack_clock>=60:
                self.attack_clock=0
            if self.attack_clock < 10:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'grosses Skelett'+s+'Skeleton_attack1.png')
            elif self.attack_clock < 20:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'grosses Skelett'+s+'Skeleton_attack2.png')
            else:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'grosses Skelett'+s+'Skeleton_attack3.png')
            if self.face=='left':
                self.surf=pygame.transform.flip(self.surf, True, False)
            self.surf=pygame.transform.scale(self.surf, (267,267))
            self.attack_clock+=1

    def update(self, key, x, y):
        self.print()
        self.walk(key, x, y)
        self.walk_animation()
        self.attack_animation()

class Boss1(pygame.sprite.Sprite):
    def __init__(self):
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Boss1'+s+'Bossgegner1.png')
        self.health=15
        self.face='right'
        self.leg=0
        self.arm=0
        self.attack_clock=0
        self.x=250
        self.y=700
        self.type = '4'
    
    def print(self):
        screen.blit(self.surf, (self.x,self.y))

    def walk(self, key, x, y):
        if 410<self.x:
            self.x-=6
        if self.x<410:
            self.x+=6
        if 400<self.y:
            self.y-=6
        if self.y<400:
            self.y+=6

        if key=='a' or key=='aws' or key=='asw' or key=='was' or key=='wsa' or key=='saw' or key=='swa':
            if x<0:
                self.x+=10
        if key=='d' or key=='dws' or key=='dsw' or key=='wds' or key=='wsd' or key=='sdw' or key=='swd':
            if x>-4000:
                self.x-=10
        if key=='w' or key=='wad' or key=='wda' or key=='awd' or key=='adw' or key=='daw' or key=='dwa':
            if y<0:
                self.y+=10
        if key=='wa' or key=='aw':
            if x<0:
                self.x+=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='wd' or key=='dw':
            if x>-4000:
                self.x-=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='s' or key=='sad' or key=='sda' or key=='asd' or key=='ads' or key=='das' or key=='dsa':
            if y>-4000:
                self.y-=10
        if key=='sa' or key=='as':
            if x<0:
                self.x+=50**0.5
            if y>-4000:
                self.y-=50**0.5
        if key=='sd' or key=='ds':
            if x>-4000:
                self.x-=50**0.5
            if y>-4000:
                self.y-=50**0.5

    def walk_animation(self):
        if 410>self.x:
            self.face='right'
        else:
            self.face='left'
        if 600>self.x>120 and 545>self.y>370:
            pass
        else:
            if self.leg>=40:
                self.leg=0
            if self.leg<20:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Boss1'+s+'Bossgegner1_Walk1.png')
            else:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Boss1'+s+'Bossgegner1_Walk2.png')
            if self.face=='left':
                self.surf=pygame.transform.flip(self.surf, True, False)
            self.leg+=1

    def attack(self, player_health, block, shield):
        if 600>self.x>120 and 545>self.y>370:
            if self.arm>=40:
                self.arm=0
                if block and (2-shield) >= 0:
                    player_health-=(2-shield)
                elif block != True:
                    player_health-=2
            self.arm+=1
        else:
            self.arm=20
        return(player_health)
        
    def attack_animation(self):
        if 600>self.x>120 and 545>self.y>370:
            if self.arm<30:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Boss1'+s+'Bossgegner1_attack1.png')
            else:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Boss1'+s+'Bossgegner1_attack2.png')
            if self.face=='left':
                self.surf=pygame.transform.flip(self.surf, True, False)
            self.attack_clock+=1

class Boss2(pygame.sprite.Sprite):
    def __init__(self):
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Boss2'+s+'Bossgegner2.png')
        self.health=15
        self.leg=0
        self.arm=0
        self.attack_clock=0
        self.x=750
        self.y=300
        self.type = '5'
    
    def print(self):
        screen.blit(self.surf, (self.x,self.y))

    def walk(self, key, x, y):
        if 410<self.x:
            self.x-=2
        if self.x<410:
            self.x+=2
        if 400<self.y:
            self.y-=2
        if self.y<400:
            self.y+=2

        if key=='a' or key=='aws' or key=='asw' or key=='was' or key=='wsa' or key=='saw' or key=='swa':
            if x<0:
                self.x+=10
        if key=='d' or key=='dws' or key=='dsw' or key=='wds' or key=='wsd' or key=='sdw' or key=='swd':
            if x>-4000:
                self.x-=10
        if key=='w' or key=='wad' or key=='wda' or key=='awd' or key=='adw' or key=='daw' or key=='dwa':
            if y<0:
                self.y+=10
        if key=='wa' or key=='aw':
            if x<0:
                self.x+=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='wd' or key=='dw':
            if x>-4000:
                self.x-=50**0.5
            if y<0:
                self.y+=50**0.5
        if key=='s' or key=='sad' or key=='sda' or key=='asd' or key=='ads' or key=='das' or key=='dsa':
            if y>-4000:
                self.y-=10
        if key=='sa' or key=='as':
            if x<0:
                self.x+=50**0.5
            if y>-4000:
                self.y-=50**0.5
        if key=='sd' or key=='ds':
            if x>-4000:
                self.x-=50**0.5
            if y>-4000:
                self.y-=50**0.5

    def walk_animation(self):
        if self.leg>=40:
            self.leg=0
        if self.leg<20:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Boss2'+s+'Bossgegner2_Walk1.png')
        else:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Boss2'+s+'Bossgegner2_Walk2.png')
        self.leg+=1

    def attack(self, player_health, block, shield):
        if 550>self.x>150 and 550>self.y>200:
            if self.arm == 55:
                if block and (2-shield) >= 0:
                    player_health-=(2-shield)
                elif block != True:
                    player_health-=2
            elif self.arm == 60:
                if block and (2-shield) >= 0:
                    player_health-=(2-shield)
                elif block != True:
                    player_health-=2
            elif self.arm >= 65:
                self.arm = 0
            self.arm+=1
        else:
            self.arm=20
        return(player_health)
        
    def attack_animation(self):
        if self.arm >= 20:
            if 550>self.x>150 and 550>self.y>200:
                if self.arm >= 55:
                    self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Boss2'+s+'Bossgegner2_Attack1.png')
                if self.arm >= 60:
                    self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Boss2'+s+'Bossgegner2_Attack2.png')

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        self.menu = True
        self.stage = 1
        self.click_possible = True

        self.start = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Start Button1.png')
        self.start_x = 300
        self.start_y = 450

        self.tutorial = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Tutorial Button1.png')
        self.tutorial_x = 300
        self.tutorial_y = 600

        self.neues_spiel = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Neues Spiel Button1.png')
        self.neues_spiel_x = 300
        self.neues_spiel_y = 300
        self.char1 = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Charakter1 Button1.png')
        self.char1_x = 30
        self.char1_y = 200

        self.char2 = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Charakter2 Button1.png')
        self.char2_x = 541
        self.char2_y = 200

        self.spiel_laden = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Spiel Laden Button1.png')
        self.spiel_laden_x = 300
        self.spiel_laden_y = 420
        self.stand1 = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Spielstand1 Button1.png')
        self.stand1_x = 30
        self.stand1_y = 25
        self.stand2 = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Spielstand2 Button1.png')
        self.stand2_x = 541
        self.stand2_y = 25

        self.zurück = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Zurück Button1.png')
        self.zurück_x = 300
        self.zurück_y = 740

        self.speichern = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Speichern Button1.png')
        self.speichern_x = 276
        self.speichern_y = 300

        self.speichern_verlassen = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Speichern und Verlassen Button1.png')
        self.speichern_verlassen_x = 276
        self.speichern_verlassen_y = 420

    def print(self):
        if self.stage == 1:
            screen.blit(self.start, (self.start_x, self.start_y))
            screen.blit(self.tutorial, (self.tutorial_x, self.tutorial_y))
        elif self.stage == 2:
            screen.blit(self.neues_spiel, (self.neues_spiel_x, self.neues_spiel_y))
            screen.blit(self.spiel_laden, (self.spiel_laden_x, self.spiel_laden_y))
            screen.blit(self.zurück, (self.zurück_x, self.zurück_y))
        elif self.stage == 3:
            screen.blit(self.char1, (self.char1_x, self.char1_y))
            screen.blit(self.char2, (self.char2_x, self.char2_y))
            screen.blit(self.zurück, (self.zurück_x, self.zurück_y))
        elif self.stage == 4:
            screen.blit(self.stand1, (self.stand1_x, self.stand1_y))
            screen.blit(self.stand2, (self.stand2_x, self.stand2_y))
            screen.blit(self.zurück, (self.zurück_x, self.zurück_y))
        elif self.stage == 5:
            screen.blit(self.speichern, (self.speichern_x, self.speichern_y))
            screen.blit(self.speichern_verlassen, (self.speichern_verlassen_x, self.speichern_verlassen_y))
            screen.blit(self.zurück, (self.zurück_x, self.zurück_y))

    def button(self, left, pos, player_info, enemies_info, background_info, boss1_info, boss2_info):
        if self.stage == 1:
            if 300<pos[0]<700 and 450<pos[1]<550:
                self.start = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Start Button2.png')
                self.start_x = 290
                if left:
                    self.stage = 2
            else:
                self.start = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Start Button1.png')
                self.start_x = 300

            if 300<pos[0]<700 and 600<pos[1]<700:
                self.tutorial = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Tutorial Button2.png')
                self.tutorial_x = 290
                if left:
                    self.stage = 6
            else:
                self.tutorial = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Tutorial Button1.png')
                self.tutorial_x = 300

        elif self.stage == 2:
            if 300<pos[0]<700 and 300<pos[1]<400:
                self.neues_spiel = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Neues Spiel Button2.png')
                self.neues_spiel_x = 291
                if left:
                    self.stage = 3
            else:
                self.neues_spiel = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Neues Spiel Button1.png')
                self.neues_spiel_x = 300

            if 300<pos[0]<700 and 420<pos[1]<520:
                self.spiel_laden = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Spiel Laden Button2.png')
                self.spiel_laden_x = 290
                if left:
                    self.stage = 4
            else:
                self.spiel_laden = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Spiel Laden Button1.png')
                self.spiel_laden_x = 300

            if 300<pos[0]<700 and 740<pos[1]<840:
                self.zurück = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Zurück Button2.png')
                self.zurück_x = 290
                if left:
                    self.stage = 1
            else:
                self.zurück = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Zurück Button1.png')
                self.zurück_x = 300

        elif self.stage == 3:
            if 25<pos[0]<459 and 200<pos[1]<634:
                self.char1 = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Charakter1 Button2.png')
                self.char1_x = 2
                if left:
                    return(1)
            else:
                self.char1 = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Charakter1 Button1.png')
                self.char1_x = 30

            if 541<pos[0]<975 and 200<pos[1]<634:
                self.char2 = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Charakter2 Button2.png')
                self.char2_x = 513
                if left:
                    return(2)
            else:
                self.char2 = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Charakter2 Button1.png')
                self.char2_x = 541

            if 300<pos[0]<700 and 740<pos[1]<840:
                self.zurück = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Zurück Button2.png')
                self.zurück_x = 290
                if left:
                    self.stage = 2
            else:
                self.zurück = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Zurück Button1.png')
                self.zurück_x = 300

        elif self.stage == 4:
            if 30<pos[0]<464 and 25<pos[1]<459:
                self.stand1 = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Spielstand1 Button2.png')
                self.stand1_x = 2
                if left:
                    save1 = open("Save1.txt","r")
                    if save1.read() != '':
                        save1.close()
                        save1 = open("Save1.txt","r")
                        player.character = str(save1.readlines()[0][0])
                        save1.close()
                        save1 = open("Save1.txt","r")
                        player.health = int(save1.readlines()[1][:-1])
                        save1.close()
                        save1 = open("Save1.txt","r")
                        player.inventory = [save1.readlines()[2][2]]
                        save1.close()
                        save1 = open("Save1.txt","r")
                        player.inventory.append(save1.readlines()[2][7])
                        save1.close()
                        save1 = open("Save1.txt","r")
                        player.coin_count = int(save1.readlines()[3][:-1])
                        save1.close()
                        save1 = open("Save1.txt","r")
                        player.stage = int(save1.readlines()[4][:-1])
                        save1.close()
                        save1 = open("Save1.txt","r")

                        background.x = float(save1.readlines()[5][:-1])
                        save1.close()
                        save1 = open("Save1.txt","r")
                        background.y = float(save1.readlines()[6][:-1])
                        save1.close()
                        save1 = open("Save1.txt","r")

                        boss1.health = int(save1.readlines()[7][:-1])
                        save1.close()
                        save1 = open("Save1.txt","r")
                        boss1.x = float(save1.readlines()[8][:-1])
                        save1.close()
                        save1 = open("Save1.txt","r")
                        boss1.y = float(save1.readlines()[9][:-1])
                        save1.close()
                        save1 = open("Save1.txt","r")

                        boss2.health = int(save1.readlines()[10][:-1])
                        save1.close()
                        save1 = open("Save1.txt","r")
                        boss2.x = float(save1.readlines()[11][:-1])
                        save1.close()
                        save1 = open("Save1.txt","r")
                        boss2.y = float(save1.readlines()[12][:-1])
                        save1.close()
                        save1 = open("Save1.txt","r")

                        for i in range(int(save1.readlines()[13][:-1])):
                            save1.close()
                            save1 = open("Save1.txt","r")
                            if int(save1.readlines()[14+4*i][:-1]) == 1:
                                enemy = Enemy1()
                            save1.close()
                            save1 = open("Save1.txt","r")
                            if int(save1.readlines()[14+4*i][:-1]) == 2:
                                enemy = Enemy2()
                            save1.close()
                            save1 = open("Save1.txt","r")
                            if int(save1.readlines()[14+4*i][:-1]) == 3:
                                enemy = Enemy3()
                            save1.close()
                            save1 = open("Save1.txt","r")
                            if int(save1.readlines()[14+4*i][:-1]) == 4:
                                enemy = Enemy4()
                            save1.close()
                            save1 = open("Save1.txt","r")
                            if int(save1.readlines()[14+4*i][:-1]) == 5:
                                enemy = Enemy5()
                            save1.close()
                            save1 = open("Save1.txt","r")
                            if int(save1.readlines()[14+4*i][:-1]) == 6:
                                enemy = Enemy6() 
                            save1.close()
                            save1 = open("Save1.txt","r")
                            enemy.health = int(save1.readlines()[15+4*i][:-1])
                            save1.close()
                            save1 = open("Save1.txt","r")
                            enemy.x = float(save1.readlines()[16+4*i][:-1])
                            save1.close()
                            save1 = open("Save1.txt","r")
                            enemy.y = float(save1.readlines()[17+4*i][:-1])
                            save1.close()
                            enemies.add(enemy)
                        
                        save1 = open("Save1.txt","r")
                        player.round_timer = int(save1.readlines()[-1])
                        save1.close()

                        save1 = open("Save1.txt","w")
                        save1.write("")
                        save1.close()
                        self.stage = 0
                        self.menu = False
                    else:
                        save1.close()
            else:
                self.stand1 = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Spielstand1 Button1.png')
                self.stand1_x = 30
            
            if 541<pos[0]<975 and 25<pos[1]<459:
                self.stand2 = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Spielstand2 Button2.png')
                self.stand2_x = 513
                if left:
                    save2 = open("Save2.txt","r")
                    if save2.read() != '':
                        save2.close()
                        save2 = open("Save2.txt","r")
                        player.character = str(save2.readlines()[0][0])
                        save2.close()
                        save2 = open("Save2.txt","r")
                        player.health = int(save2.readlines()[1][:-1])
                        save2.close()
                        save2 = open("Save2.txt","r")
                        player.inventory = [save2.readlines()[2][2]]
                        save2.close()
                        save2 = open("Save2.txt","r")
                        player.inventory.append(save2.readlines()[2][7])
                        save2.close()
                        save2 = open("Save2.txt","r")
                        player.coin_count = int(save2.readlines()[3][:-1])
                        save2.close()
                        save2 = open("Save2.txt","r")
                        player.stage = int(save2.readlines()[4][:-1])
                        save2.close()
                        save2 = open("Save2.txt","r")

                        background.x = float(save2.readlines()[5][:-1])
                        save2.close()
                        save2 = open("Save2.txt","r")
                        background.y = float(save2.readlines()[6][:-1])
                        save2.close()
                        save2 = open("Save2.txt","r")

                        boss1.health = int(save2.readlines()[7][:-1])
                        save2.close()
                        save2 = open("Save2.txt","r")
                        boss1.x = float(save2.readlines()[8][:-1])
                        save2.close()
                        save2 = open("Save2.txt","r")
                        boss1.y = float(save2.readlines()[9][:-1])
                        save2.close()
                        save2 = open("Save2.txt","r")

                        boss2.health = int(save2.readlines()[10][:-1])
                        save2.close()
                        save2 = open("Save2.txt","r")
                        boss2.x = float(save2.readlines()[11][:-1])
                        save2.close()
                        save2 = open("Save2.txt","r")
                        boss2.y = float(save2.readlines()[12][:-1])
                        save2.close()
                        save2 = open("Save2.txt","r")

                        for i in range(int(save2.readlines()[13][:-1])):
                            save2.close()
                            save2 = open("Save2.txt","r")
                            if int(save2.readlines()[14+4*i][:-1]) == 1:
                                enemy = Enemy1()
                            save2.close()
                            save2 = open("Save2.txt","r")
                            if int(save2.readlines()[14+4*i][:-1]) == 2:
                                enemy = Enemy2()
                            save2.close()
                            save2 = open("Save2.txt","r")
                            if int(save2.readlines()[14+4*i][:-1]) == 3:
                                enemy = Enemy3()
                            save2.close()
                            save2 = open("Save2.txt","r")
                            if int(save2.readlines()[14+4*i][:-1]) == 4:
                                enemy = Enemy4()
                            save2.close()
                            save2 = open("Save2.txt","r")
                            if int(save2.readlines()[14+4*i][:-1]) == 5:
                                enemy = Enemy5()
                            save2.close()
                            save2 = open("Save2.txt","r")
                            if int(save2.readlines()[14+4*i][:-1]) == 6:
                                enemy = Enemy6()
                            save2.close()
                            save2 = open("Save2.txt","r")
                            enemy.health = int(save2.readlines()[15+4*i][:-1])
                            save2.close()
                            save2 = open("Save2.txt","r")
                            enemy.x = float(save2.readlines()[16+4*i][:-1])
                            save2.close()
                            save2 = open("Save2.txt","r")
                            enemy.y = float(save2.readlines()[17+4*i][:-1])
                            save2.close()
                            enemies.add(enemy)
                        
                        save2 = open("Save2.txt","r")
                        player.round_timer = int(save2.readlines()[-1])
                        save2.close()

                        save2 = open("Save2.txt","w")
                        save2.write("")
                        save2.close()
                        self.stage = 0
                        self.menu = False
                    else:
                        save2.close()
            else:
                self.stand2 = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Spielstand2 Button1.png')
                self.stand2_x = 541
            
            if 300<pos[0]<700 and 740<pos[1]<840:
                self.zurück = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Zurück Button2.png')
                self.zurück_x = 290
                if left:
                    self.stage = 2
            else:
                self.zurück = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Zurück Button1.png')
                self.zurück_x = 300

        elif self.stage == 5:
            if 276<pos[0]<724 and 300<pos[1]<398:
                self.speichern = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Speichern Button2.png')
                self.speichern_x = 263
                if left:
                    save1 = open("Save1.txt","r")
                    save2 = open("Save2.txt","r")
                    if save1.read() == '':
                        save1.close()
                        save2.close()
                        save1 = open("Save1.txt","w")
                        save1.writelines([str(player_info.character)+"\n", str(player_info.health)+"\n", str(player_info.inventory)+"\n", str(player_info.coin_count)+"\n", str(player_info.stage)+"\n", str(background_info.x)+"\n", str(background_info.y)+"\n", str(boss1_info.health)+"\n", str(boss1_info.x)+"\n", str(boss1_info.y)+"\n", str(boss2_info.health)+"\n", str(boss2_info.x)+"\n", str(boss2_info.y)+"\n", str(len(enemies_info))+"\n"])
                        save1.close()
                        save1 = open("Save1.txt","a")
                        for enemy in enemies_info:
                            save1.writelines([str(enemy.__class__)[-3:-2]+"\n", str(enemy.health)+"\n", str(enemy.x)+"\n", str(enemy.y)+"\n"])
                        save1.close()
                        save1 = open("Save1.txt","a")
                        save1.write(str(player_info.round_timer))
                        save1.close()
                    elif save2.read() == '':
                        save1.close()
                        save2.close()
                        save2 = open("Save2.txt","w")
                        save2.writelines([str(player_info.character)+"\n", str(player_info.health)+"\n", str(player_info.inventory)+"\n", str(player_info.coin_count)+"\n", str(player_info.stage)+"\n", str(background_info.x)+"\n", str(background_info.y)+"\n", str(boss1_info.health)+"\n", str(boss1_info.x)+"\n", str(boss1_info.y)+"\n", str(boss2_info.health)+"\n", str(boss2_info.x)+"\n", str(boss2_info.y)+"\n", str(len(enemies_info))+"\n"])
                        save2.close()
                        save2 = open("Save2.txt","a")
                        for enemy in enemies_info:
                            save2.writelines([str(enemy.__class__)[-3:-2]+"\n", str(enemy.health)+"\n", str(enemy.x)+"\n", str(enemy.y)+"\n"])
                        save2.close()
                        save2 = open("Save2.txt","a")
                        save2.write(str(player_info.round_timer))
                        save2.close()
                    else:
                        save1.close()
                        save2.close()
            else:
                self.speichern = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Speichern Button1.png')
                self.speichern_x = 276

            if 276<pos[0]<724 and 420<pos[1]<518:
                self.speichern_verlassen = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Speichern und Verlassen Button2.png')
                self.speichern_verlassen_x = 263
                if left:
                    save1 = open("Save1.txt","r")
                    save2 = open("Save2.txt","r")
                    if save1.read() == '':
                        save1.close()
                        save2.close()
                        save1 = open("Save1.txt","w")
                        save1.writelines([str(player_info.character)+"\n", str(player_info.health)+"\n", str(player_info.inventory)+"\n", str(player_info.coin_count)+"\n", str(player_info.stage)+"\n", str(background_info.x)+"\n", str(background_info.y)+"\n", str(boss1_info.health)+"\n", str(boss1_info.x)+"\n", str(boss1_info.y)+"\n", str(boss2_info.health)+"\n", str(boss2_info.x)+"\n", str(boss2_info.y)+"\n", str(len(enemies_info))+"\n"])
                        save1.close()
                        save1 = open("Save1.txt","a")
                        for enemy in enemies_info:
                            save1.writelines([str(enemy.__class__)[-3:-2]+"\n", str(enemy.health)+"\n", str(enemy.x)+"\n", str(enemy.y)+"\n"])
                        save1.close()
                        save1 = open("Save1.txt","a")
                        save1.write(str(player_info.round_timer))
                        save1.close()
                    elif save2.read() == '':
                        save1.close()
                        save2.close()
                        save2 = open("Save2.txt","w")
                        save2.writelines([str(player_info.character)+"\n", str(player_info.health)+"\n", str(player_info.inventory)+"\n", str(player_info.coin_count)+"\n", str(player_info.stage)+"\n", str(background_info.x)+"\n", str(background_info.y)+"\n", str(boss1_info.health)+"\n", str(boss1_info.x)+"\n", str(boss1_info.y)+"\n", str(boss2_info.health)+"\n", str(boss2_info.x)+"\n", str(boss2_info.y)+"\n", str(len(enemies_info))+"\n"])
                        save2.close()
                        save2 = open("Save2.txt","a")
                        for enemy in enemies_info:
                            save2.writelines([str(enemy.__class__)[-3:-2]+"\n", str(enemy.health)+"\n", str(enemy.x)+"\n", str(enemy.y)+"\n"])
                        save2.close()
                        save2 = open("Save2.txt","a")
                        save2.write(str(player_info.round_timer))
                        save2.close()
                    else:
                        save1.close()
                        save2.close()
                    self.stage = 2
            else:
                self.speichern_verlassen = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Speichern und Verlassen Button1.png')
                self.speichern_verlassen_x = 276

            if 300<pos[0]<700 and 740<pos[1]<840:
                self.zurück = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Zurück Button2.png')
                self.zurück_x = 290
                if left:
                    self.stage = 0
            else:
                self.zurück = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Zurück Button1.png')
                self.zurück_x = 300

class Shop(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Shop'+s+'Shop_0_0.png')
        self.coin = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Shop'+s+'Coins.png')
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        self.font2 = pygame.font.Font('freesansbold.ttf', 25)
        self.coin2 = pygame.transform.scale(self.coin, (28,22))
        self.choice_cooldown = False
        self.shop = False
        self.bought = False
        self.item_0_x = 480
        self.item_0_y = 360
        self.item_1_x = 400
        self.item_1_y = 360
        self.price_x = 560
        self.price_y = 550
        self.price_coins_x = 595
        self.price_coins_y = 550
        self.coins = 0
    
    def print(self, player_coins):
        screen.blit(self.surf, (200,200))

        self.coins = player_coins

        if self.coins < 10:
            screen.blit(self.font.render(str(self.coins), True, (255,255,255)), (655,230))
        elif self.coins < 100:
            screen.blit(self.font.render(str(self.coins), True, (255,255,255)), (620,230))
        else:
            screen.blit(self.font.render(str(self.coins), True, (255,255,255)), (595,230))

        if self.bought != True:
            if self.type == 0:
                screen.blit(self.item, (self.item_0_x, self.item_0_y))
            else:
                screen.blit(self.item, (self.item_1_x, self.item_1_y))
            screen.blit(self.coin2, (self.price_coins_x, self.price_coins_y))
            screen.blit(self.font2.render('20', True, (255,255,255)), (self.price_x, self.price_y))
    
    def button(self, left, pos):
        if 388 < pos[0] < 611 and 681 < pos[1] < 749:
            self.surf = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Shop'+s+'Shop_0_1.png')
            if left:
                self.bought = False
                self.choice_cooldown = False
                self.shop = False

        elif 365 < pos[0] < 635 and 333 < pos[1] < 588:
            self.surf = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Shop'+s+'Shop_1_0.png')
            self.item_0_x = 470
            self.item_0_y = 370
            self.item_1_x = 390
            self.item_1_y = 370
            self.price_x = 550
            self.price_y = 560
            self.price_coins_x = 585
            self.price_coins_y = 560
            if left and self.bought == False and self.coins >= 20:
                self.bought = True
                return(True)
        
        else:
            self.surf = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Shop'+s+'Shop_0_0.png')
            self.item_0_x = 480
            self.item_0_y = 360
            self.item_1_x = 400
            self.item_1_y = 360
            self.price_x = 560
            self.price_y = 550
            self.price_coins_x = 595
            self.price_coins_y = 550
    
    def choice(self, inventory):
        if self.choice_cooldown == False:
            self.type = random.randint(0, 1)
            if inventory[0] == 5:
                self.type = 1
            elif inventory[1] == 5:
                self.type = 0
            if self.type == 0:
                self.item = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Items'+s+'Schwert '+str(int(inventory[self.type])+1)+'.png')
                self.item = pygame.transform.scale(self.item, (43,200))
                self.item_number = str(int(inventory[self.type])+1)
            else:
                self.item = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Items'+s+'Schild_'+str(int(inventory[self.type])+1)+'.png')
                self.item = pygame.transform.scale(self.item, (200,200))
                self.item_number = str(int(inventory[self.type])+1)
            self.choice_cooldown = True

class Tutorial(pygame.sprite.Sprite):
    def __init__(self):
        self.tutorial = False
        self.stage = 1
        self.text = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Tutorial Text'+str(self.stage)+'.png')
        self.show = True
        self.timer = 0
        self.timer_start = False

    def print(self):
        screen.blit(self.text, (200, 100))

    def change_text(self):
        if self.stage < 11:
            self.text = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Menütexturen'+s+'Tutorial Text'+str(self.stage)+'.png')
    
    def timer_tick(self):
        if self.timer_start:
            self.timer += 1


SPAWN_ENEMY_1 = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_ENEMY_1, 5000)

SPAWN_ENEMY_2 = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_ENEMY_2, 5000)

SPAWN_ENEMY_3 = pygame.USEREVENT + 3
pygame.time.set_timer(SPAWN_ENEMY_3, 15000)

SPAWN_ENEMY_4 = pygame.USEREVENT + 4
pygame.time.set_timer(SPAWN_ENEMY_4, 15000)

SPAWN_ENEMY_5 = pygame.USEREVENT + 5
pygame.time.set_timer(SPAWN_ENEMY_5, 30000)

SPAWN_ENEMY_6 = pygame.USEREVENT + 6
pygame.time.set_timer(SPAWN_ENEMY_6, 30000)

ROUND_TIMER_TICK = pygame.USEREVENT + 7
pygame.time.set_timer(ROUND_TIMER_TICK, 1000)

enemies = pygame.sprite.Group()

player = Player(1)

background=Background()

enemy1=Enemy1()
enemies.add(enemy1)

boss1=Boss1()
boss2=Boss2()

menu = Menu()
shop = Shop()

clock = pygame.time.Clock()
key='' #Für die Inputs
game = True
font = pygame.font.Font('freesansbold.ttf', 80)
font2 = pygame.font.Font('freesansbold.ttf', 30)
tutorial = Tutorial()

while game:

    if menu.menu:
        key=''
        background.print()
        menu.print()

        if menu.stage == 0:
            menu.menu = False

        if menu.stage == 6:
            tutorial.tutorial = True
            menu.menu = False

        for event in pygame.event.get():

            if pygame.mouse.get_pressed()[0] == False:
                menu.click_possible = True

            if menu.click_possible:
                if menu.button(pygame.mouse.get_pressed()[0], pygame.mouse.get_pos(), player, enemies, background, boss1, boss2) != None:
                    round_timer = 60
                    background.x=-2000
                    background.y=-2000
                    player = Player(menu.button(pygame.mouse.get_pressed()[0], pygame.mouse.get_pos(), player, enemies, background, boss1, boss2))
                    menu.stage = 0

            if pygame.mouse.get_pressed()[0]:
                menu.click_possible = False

            if event.type == QUIT:
                game = False

    else:
        background.print()

        if tutorial.tutorial:

            player.print()
            player.walk(key)
            player.animation(key)
            if player.is_attacking:
                player.arm+=1
            else:
                player.arm=25

            if tutorial.stage == 4:
                player.health = enemy1.attack(player.health, player.block, int(player.inventory[1]))
                if player.is_attacking and player.block != True:
                    enemy1.health = player.attack(enemy1.x, enemy1.y, enemy1.health, enemy1.type)

                if enemy1.health <= 0:
                    player.coin_count = 21
                    enemy1.kill()
                    tutorial.stage += 1
                    tutorial.change_text()
                    tutorial.timer_start = True
                else:
                    enemy1.update(key, background.x, background.y)
                
                if player.health <= 0:
                    player.health = 10
                    enemy1 = Enemy1()

            elif tutorial.stage == 6:
                tutorial.timer_start = True
                shop.shop = True
                shop.type = 0
                shop.item = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Items'+s+'Schwert '+str(int(player.inventory[shop.type])+1)+'.png')
                shop.item = pygame.transform.scale(shop.item, (43,200))
                shop.item_number = str(int(player.inventory[shop.type])+1)
                shop.print(player.coin_count)

            elif tutorial.stage == 7:
                shop.print(player.coin_count)

            elif tutorial.stage == 8:
                shop.print(player.coin_count)
                if shop.shop == False:
                    tutorial.stage += 1
                    tutorial.change_text()

            elif tutorial.stage == 9:
                boss2.print()
                boss2.walk(key, background.x, background.y)
                boss2.walk_animation()
                player.health = boss2.attack(player.health, player.block, int(player.inventory[1]))
                boss2.attack_animation()
                player.attack(boss2.x, boss2.y, boss2.health, boss2.type)
                if player.health <= 0:
                    tutorial.stage += 1
                    tutorial.change_text()
            
            elif tutorial.stage == 10:
                boss2.print()
                tutorial.timer_start = True
            
            elif tutorial.stage == 11:
                tutorial.tutorial = False
                menu.stage = 1
                menu.menu = True

            if tutorial.show:
                tutorial.print()
            tutorial.timer_tick()


            if tutorial.timer >= 250:
                tutorial.timer_start = False
                tutorial.timer = 0
                tutorial.stage += 1
                tutorial.change_text()
                tutorial.show =  True


            for event in pygame.event.get():

                if event.type == KEYDOWN:

                    if tutorial.stage == 1:
                        tutorial.stage += 1
                        tutorial.change_text()

                    elif tutorial.stage == 2 or tutorial.stage == 4 or tutorial.stage == 9:

                        if event.key == K_w:
                            key+='w'
                        if event.key == K_s:
                            key+='s'
                        if event.key == K_a:
                            key+='a'
                        if event.key == K_d:
                            key+='d'
                        if event.key == K_q:
                            player.ability_true += 1

                    elif tutorial.stage == 3:
                        tutorial.show =  False
                        tutorial.timer_start = True

                    if tutorial.stage == 2:
                        tutorial.timer_start = True

                if tutorial.stage == 3 or tutorial.stage == 4 or tutorial.stage == 9:
                    if pygame.mouse.get_pressed()[0]:
                        player.is_attacking=True
                    else:
                        player.is_attacking=False
                                
                    if pygame.mouse.get_pressed()[2]:
                        player.block = True
                    else:
                        player.block = False
                else:
                    player.is_attacking=False
                    player.block = False

                if tutorial.stage == 7 or tutorial.stage == 8:
                    if shop.button(pygame.mouse.get_pressed()[0], pygame.mouse.get_pos()) != None:
                        player.inventory[shop.type] = shop.item_number
                        player.coin_count -= 20

                        player.surf = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Character'+str(player.character)+s+'character'+str(player.character)+'_'+player.inventory[0]+'_0.png')
                        player.surf = pygame.transform.scale(player.surf, (125,125))
                        player.shield = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Items'+s+'Schild_'+player.inventory[1]+'.png')
                        player.shield = pygame.transform.scale(player.shield, (100,100))

                        tutorial.stage += 1
                        tutorial.change_text()

                if event.type == KEYUP:
                    if event.key == K_w:
                        key=key_not_input(key, 'w')
                    if event.key == K_s:
                        key=key_not_input(key, 's')
                    if event.key == K_a:
                        key=key_not_input(key, 'a')
                    if event.key == K_d:
                        key=key_not_input(key, 'd')


                if event.type == QUIT:
                    game = False
        
        else:
            if shop.shop:
                key=''
                player.health = 10
                shop.choice(player.inventory)
                shop.print(player.coin_count)

                for event in pygame.event.get():

                    if shop.button(pygame.mouse.get_pressed()[0], pygame.mouse.get_pos()) != None:
                        player.inventory[shop.type] = shop.item_number
                        player.coin_count -= 20

                        player.surf = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Character'+str(player.character)+s+'character'+str(player.character)+'_'+player.inventory[0]+'_0.png')
                        player.surf = pygame.transform.scale(player.surf, (125,125))
                        player.shield = pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Items'+s+'Schild_'+player.inventory[1]+'.png')
                        player.shield = pygame.transform.scale(player.shield, (100,100))

                    if event.type == QUIT:
                        game = False
            
            else:
                enemies.update(key, background.x, background.y)

                for single_enemy in enemies:

                    player.health = single_enemy.attack(player.health, player.block, int(player.inventory[1]))
                    if player.is_attacking and player.block != True:
                        single_enemy.health = player.attack(single_enemy.x, single_enemy.y, single_enemy.health, single_enemy.type)
                    single_enemy.health = player.ability(single_enemy.x , single_enemy.y , single_enemy.health, single_enemy.type)

                    if single_enemy.health <= 0:
                        player.coin_count += int(single_enemy.type)
                        single_enemy.kill()
                
                if len(enemies) == 0:
                    player.ability(0,0,0,'0')

                if player.stage == 6:
                    if boss1.health>0:
                        boss1.print()
                        boss1.walk(key, background.x, background.y)
                        boss1.walk_animation()
                        player.health = boss1.attack(player.health, player.block, int(player.inventory[1]))
                        boss1.attack_animation()
                        if player.is_attacking:
                            boss1.health = player.attack(boss1.x, boss1.y, boss1.health, boss1.type)
                    else:
                        time.sleep(1)
                        player.coin_count += 15
                        player.stage += 1
                        shop.shop = True

                elif player.stage == 11:
                    if boss2.health>0:
                        boss2.print()
                        boss2.walk(key, background.x, background.y)
                        boss2.walk_animation()
                        player.health = boss2.attack(player.health, player.block, int(player.inventory[1]))
                        boss2.attack_animation()
                        if player.is_attacking:
                            boss2.health = player.attack(boss2.x, boss2.y, boss2.health, boss2.type)
                    else:
                        time.sleep(1)
                        menu.stage = 1
                        menu.menu = True

                else:
                    if player.round_timer > 0:
                        screen.blit(font.render(str(player.round_timer), True, (255,255,255)), (460,5))

                    if player.round_timer == 0:
                        for enemy in enemies:
                            enemy.kill()
                        player.round_timer = 60
                        player.stage += 1
                        shop.shop = True

                player.print()
                player.walk(key)
                player.animation(key)
                player.ability_animation(key)
                if player.is_attacking:
                    player.arm+=1
                else:
                    player.arm=25
                
                screen.blit(font2.render('Stage: '+str(player.stage), True, (255,255,255)), (460,950))

                for event in pygame.event.get():

                    if event.type == KEYDOWN:

                        if event.key == K_ESCAPE:
                            menu.stage = 5
                            menu.menu = True

                        if event.key == K_w:
                            key+='w'
                        if event.key == K_s:
                            key+='s'
                        if event.key == K_a:
                            key+='a'
                        if event.key == K_d:
                            key+='d'
                        if event.key == K_q:
                            player.ability_true += 1

                    if event.type == KEYUP:
                        if event.key == K_w:
                            key=key_not_input(key, 'w')
                        if event.key == K_s:
                            key=key_not_input(key, 's')
                        if event.key == K_a:
                            key=key_not_input(key, 'a')
                        if event.key == K_d:
                            key=key_not_input(key, 'd')

                    if event.type == SPAWN_ENEMY_1:
                        if player.stage != 6 and player.stage != 11:
                            enemy1 = Enemy1()
                            enemies.add(enemy1)

                    if event.type == SPAWN_ENEMY_2:
                        if player.stage != 6 and player.stage != 11:
                            enemy2 = Enemy2()
                            enemies.add(enemy2)

                    if event.type == SPAWN_ENEMY_3:
                        if player.stage != 6 and player.stage != 11:
                            enemy3 = Enemy3()
                            enemies.add(enemy3)

                    if event.type == SPAWN_ENEMY_4:
                        if player.stage != 6 and player.stage != 11:
                            enemy4 = Enemy4()
                            enemies.add(enemy4)

                    if event.type == SPAWN_ENEMY_5:
                        if player.stage != 6 and player.stage != 11:
                            enemy5 = Enemy5()
                            enemies.add(enemy5)

                    if event.type == SPAWN_ENEMY_6:
                        if player.stage != 6 and player.stage != 11:
                            enemy6 = Enemy6()
                            enemies.add(enemy6)

                    if event.type == ROUND_TIMER_TICK:
                        player.round_timer -= 1

                    if event.type == QUIT:
                        game = False

                    if pygame.mouse.get_pressed()[0]:
                        player.is_attacking=True
                    else:
                        player.is_attacking=False
                    
                    if pygame.mouse.get_pressed()[2]:
                        player.block = True
                    else:
                        player.block = False

                if player.health <= 0:
                    for enemy in enemies:
                        enemy.kill()
                    player.health = 10
                    menu.stage = 2
                    menu.menu = True

    clock.tick(30)
    pygame.display.flip()

pygame.quit()