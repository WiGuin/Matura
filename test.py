import pygame,os
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
    def __init__(self):
        self.face='right'
        self.leg=10 #Für die Walking-Animation
        self.health=10
        self.arm=5
        self.is_attacking=False
        self.inventory=['1','']
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Character1'+s+'character1_'+self.inventory[0]+'_0.png')
        self.surf=pygame.transform.scale(self.surf, (125,125))
        self.x=438
        self.y=438
        self.font=pygame.font.Font('freesansbold.ttf', 32)

    def print(self):
        screen.blit(self.surf, (self.x,self.y))
        screen.blit(self.font.render('HP: '+str(self.health), True, (255,255,255)), (5,5))

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
        if type=='1':
            if self.arm>=30:
                self.arm=0
            if self.arm==0:
                if self.face=='right':
                    if 463<x<608 and 360<y<500:
                        enemy_health-=1
                if self.face=='left':
                    if 392<x<510 and 360<y<500:
                        enemy_health-=1
        if type=='10':
            if self.arm>=30:
                self.arm=0
            if self.arm==0:
                if self.face=='right':
                    if 350<x<595 and 170<y<500:
                        enemy_health-=1
                if self.face=='left':
                    if 225<x<470 and 170<y<500:
                        enemy_health-=1
        if type=='20':
            if self.arm>=30:
                self.arm=0
            if self.arm==0:
                if self.face=='right':
                    if 260<x<620 and 165<y<500:
                        enemy_health-=1
                if self.face=='left':
                    if 150<x<520 and 165<y<500:
                        enemy_health-=1
        return enemy_health

    def animation(self, key):
        if self.is_attacking and key!='':
            if self.leg>=30:
                self.leg=10
            if self.leg<20:
                if self.arm>=29 or self.arm<5:
                    self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Characters'+s+'character1_'+self.inventory[0]+'_1_attack_1.png')
                    self.surf=pygame.transform.scale(self.surf, (229,125))
                    self.x=386
                else:
                    self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Characters'+s+'character1_'+self.inventory[0]+'_1_attack_0.png')
                    self.surf=pygame.transform.scale(self.surf, (125,125))
                    self.x=438
            else:
                if self.arm==29 or self.arm<5:
                    self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Characters'+s+'character1_'+self.inventory[0]+'_2_attack_1.png')
                    self.surf=pygame.transform.scale(self.surf, (229,125))
                    self.x=386
                else:
                    self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Characters'+s+'character1_'+self.inventory[0]+'_2_attack_0.png')
                    self.surf=pygame.transform.scale(self.surf, (125,125))
                    self.x=438
        elif key!='':
            if self.leg>=30:
                self.leg=10
            if self.leg<20:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Characters'+s+'character1_'+self.inventory[0]+'_1.png')
            else:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Characters'+s+'character1_'+self.inventory[0]+'_2.png')
            self.surf=pygame.transform.scale(self.surf, (125,125))
            self.x=438
        elif self.is_attacking:
            if self.arm>=29 or self.arm<5:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Characters'+s+'character1_'+self.inventory[0]+'_0_attack_1.png')
                self.surf=pygame.transform.scale(self.surf, (229,125))
                self.x=386
            else:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Characters'+s+'character1_'+self.inventory[0]+'_0_attack_0.png')
                self.surf=pygame.transform.scale(self.surf, (125,125))
                self.x=438
        elif key=='' and self.is_attacking==False:
            self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Characters'+s+'character1_'+player.inventory[0]+'_0.png')
            self.surf=pygame.transform.scale(self.surf, (125,125))
            self.x=438
        if self.face=='left':
            self.surf=pygame.transform.flip(self.surf, True, False)
        self.leg+=1

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

    def attack(self, player_health):
        if 530>self.x and self.x>400 and 545>self.y and self.y>370:
            if self.arm>=30:
                self.arm=0
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

class Boss1(pygame.sprite.Sprite):
    def __init__(self):
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Gegner'+s+'Bossgegner1.png')
        self.health=15
        self.face='right'
        self.leg=0
        self.arm=0
        self.attack_clock=0
        self.x=410
        self.y=300
    
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
        if 690>self.x>310 and 545>self.y>370:
            pass
        else:
            if self.leg>=40:
                self.leg=0
            if self.leg<20:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Gegner'+s+'Bossgegner1_Walk1.png')
            else:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Gegner'+s+'Bossgegner1_Walk2.png')
            if self.face=='left':
                self.surf=pygame.transform.flip(self.surf, True, False)
            self.leg+=1

    def attack(self, player_health):
        if 690>self.x>310 and 545>self.y>370:
            if self.arm>=40:
                self.arm=0
                player_health-=2
            self.arm+=1
        else:
            self.arm=20
        return(player_health)
        
    def attack_animation(self):
        if 690>self.x>310 and 545>self.y>370:
            if self.arm<30:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Gegner'+s+'Bossgegner1_attack_1.png')
            else:
                self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Goblin'+s+'Bossgegner1_attack_2.png')
            if self.face=='right':
                self.surf=pygame.transform.flip(self.surf, True, False)
            self.attack_clock+=1

class Boss2(pygame.sprite.Sprite):
    def __init__(self):
        self.surf=pygame.image.load(os.path.dirname(__file__)+s+'textures'+s+'Gegner'+s+'Bossgegner2.png')
        self.health=15
        self.face='center'
        self.leg=0
        self.arm=0
        self.attack_clock=0
        self.x=365
        self.y=290
    
    def print(self):
        screen.blit(self.surf, (self.x,self.y))

    def walk(self, key, x, y):
        if 10<self.x<365 or 720<self.x:
            self.x-=2
        if 365<self.x<990 or self.x<0:
            self.x+=2
        if 10<self.y<290:
            self.y-=2
        if 290<self.y<710:
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


background=Background()

player=Player()

enemy1=Enemy1()

boss1=Boss1()
boss2=Boss2()

clock=pygame.time.Clock()
key='' #Für die Inputs

while player.health>0:

    background.print()

    player.print()
    player.walk(key)
    player.animation(key)
    if player.is_attacking:
        player.arm+=1
        boss1.health=player.attack(boss1.x, boss1.y, boss1.health, '10')
        boss1.health=player.attack(boss2.x, boss2.y, boss2.health, '20')
        enemy1.health=player.attack(enemy1.x, enemy1.y, enemy1.health, '1')
    else:
        player.arm=5

    enemy1.print()
    enemy1.walk(key, background.x, background.y)
    enemy1.walk_animation()
    player.health=enemy1.attack(player.health)
    enemy1.attack_animation()
    if enemy1.health<=0:
        enemy1.x=300
        enemy1.y=-100
        enemy1.health=5

    if boss1.health>0:
        boss1.print()
        boss1.walk(key, background.x, background.y)
        boss1.walk_animation()

    if boss2.health>0:
        boss2.print()
        boss2.walk(key, background.x, background.y)

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
                key=key_not_input(key, 'w')
            if event.key == K_s:
                key=key_not_input(key, 's')
            if event.key == K_a:
                key=key_not_input(key, 'a')
            if event.key == K_d:
                key=key_not_input(key, 'd')

        if event.type == QUIT:
            player.health=0

        if pygame.mouse.get_pressed()[0]:
            player.is_attacking=True
        else:
            player.is_attacking=False


    clock.tick(30)
    pygame.display.flip()