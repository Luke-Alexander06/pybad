import pygame as pg
from random import randint
vec = pg.math.Vector2

karakter_img = pg.image.load("karakter4stå.png")
player_img = pg.transform.scale(karakter_img,(40,65)) # endre størelse på player image
player_img_left = pg.transform.flip(player_img, True, False)
enemy_img = pg.image.load("boss1.png")
enemy_img = pg.transform.scale(enemy_img,(150,150))

STANDING = pg.image.load("karakter1stå.png")
STANDING = pg.transform.scale(STANDING,(34,56))
STANDING2 = pg.image.load("karakter2stå.png")
STANDING2 = pg.transform.scale(STANDING2,(34,56))
STANDING3 = pg.image.load("karakter3stå.png")
STANDING3 = pg.transform.scale(STANDING3,(34,56))
STANDING4 = pg.image.load("karakter4stå.png")
STANDING4 = pg.transform.scale(STANDING4,(34,56))

RUNNING = pg.image.load("karakter1løpe.png")
RUNNING = pg.transform.scale(RUNNING,(40,54))
RUNNING2 = pg.image.load("karakter2løpe.png")
RUNNING2 = pg.transform.scale(RUNNING2,(40,54))
RUNNING3 = pg.image.load("karakter3løpe.png")
RUNNING3 = pg.transform.scale(RUNNING3,(40,54))
RUNNING4 = pg.image.load("karakter4løpe.png")
RUNNING4 = pg.transform.scale(RUNNING4,(40,54))
RUNNING5 = pg.image.load("karakter5løpe.png")
RUNNING5 = pg.transform.scale(RUNNING5,(40,54))
RUNNING6 = pg.image.load("karakter6løpe.png")
RUNNING6 = pg.transform.scale(RUNNING6,(40,54))

RUNNINGBOSS = pg.image.load("boss1.png")
RUNNINGBOSS = pg.transform.scale(RUNNINGBOSS,(150,150))
RUNNINGBOSS2 = pg.image.load("boss2.png")
RUNNINGBOSS2 = pg.transform.scale(RUNNINGBOSS2,(150,150))
RUNNINGBOSS3 = pg.image.load("boss3.png")
RUNNINGBOSS3 = pg.transform.scale(RUNNINGBOSS3,(150,150))
RUNNINGBOSS4 = pg.image.load("boss4.png")
RUNNINGBOSS4 = pg.transform.scale(RUNNINGBOSS4,(150,150))

class player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect() 
        self.pos = vec(650,570)
        self.rect.center = self.pos
        self.speed = 4
        self.liv = 5
        self.current_frame = 10
        self.last_update = 10
        self.standing = True
        self.running = False
        self.left = True
        self.right = True 

        self.standing_frames = [STANDING,STANDING2,STANDING3,STANDING4]
        self.running_frames = [RUNNING,RUNNING2,RUNNING3,RUNNING4,RUNNING5,RUNNING6]
        

    def update(self):
        self.rect.center = self.pos # flytter rect til player til ny posisjon
        

        self.running = False
        self.standing = True
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= self.speed
            self.running = True
            self.standing = False
            
        
        if keys[pg.K_s]:
            self.pos.y += self.speed
            self.running = True
            self.standing = False
            
       
        if keys[pg.K_a]:
            self.pos.x -= self.speed          
            self.running = True
            self.standing = False
            self.left = True
            self.right = False

        if keys[pg.K_d]:
            self.pos.x += self.speed        
            self.running = True
            self.standing = False
            self.right = True
            self.left = False

        if keys[pg.K_LSHIFT]:
            self.speed = 7
        else:
            self.speed = 4


        if self.pos.y < 270:
            self.pos.y = 270

        if self.pos.y > 870:
            self.pos.y = 870

        if self.pos.x < 500:
            self.pos.x = 500

        if self.pos.x > 1450:
            self.pos.x = 1450
      
        self.animate()
    def animate(self):
        now = pg.time.get_ticks()

        if self.running:
            if now - self.last_update  > 100:
                self.last_update = now
                self.current_frame = (self.current_frame +1)% len(self.running_frames)
                self.image = self.running_frames[self.current_frame]
                self.rect = self.image.get_rect()
                print("running animation")

                # hvis moving left, flip
                if self.left:
                    self.image = pg.transform.flip(self.image, True, False)
                   
        elif self.standing:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame +1)% len(self.standing_frames)
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()  
                print("standing animation")

                if self.left:
                    self.image = pg.transform.flip(self.image, True, False)

        self.rect.center = self.pos

class Enemy(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = enemy_img
        self.image_left = self.image
        self.image_right = self.image = pg.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect() # henter self.image sin størelse og
        self.pos = vec(1300,550)
        self.rect.center = self.pos
        self.speed = 1
        self.direction_x = 1
        self.direction_y = 1
        self.current_frame = 10
        self.last_update = 10
        self.left = True
        self.right = True 

        self.bossrunning_frames = [RUNNINGBOSS,RUNNINGBOSS2,RUNNINGBOSS3,RUNNINGBOSS4]

    def update(self):
        self.rect.center = self.pos # flytter rect til player til ny posisjon
        
        self.pos.x += self.direction_x
        self.pos.y += self.direction_y


        if self.pos.x < self.game.karakter.pos.x:
            self.direction_x = 1
            
            
        elif self.pos.x > self.game.karakter.pos.x:
            self.direction_x = -1
           

        if self.pos.y < self.game.karakter.pos.y:
            self.direction_y = 1

        elif self.pos.y > self.game.karakter.pos.y:
            self.direction_y = -1
 
        if self.pos.x < -100: # til venstre for skjermen
            self.direction_x = randint(-1,10)


        now = pg.time.get_ticks()

        if now - self.last_update  > 100:
            self.last_update = now
            self.current_frame = (self.current_frame +1)% len(self.bossrunning_frames)
            self.image = self.bossrunning_frames[self.current_frame]
            self.rect = self.image.get_rect()
            print("bossrunning animation")

            if self.left:
                self.image = pg.transform.flip(self.image, True, False)


