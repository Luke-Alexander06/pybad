import pygame as pg
from random import randint
vec = pg.math.Vector2

karakter_img = pg.image.load("karakter4stå.png")
player_img = pg.transform.scale(karakter_img,(40,65)) # endre størelse på player image
enemy_img = pg.image.load("bos2.png")
enemy_img = pg.transform.scale(enemy_img,(150,150))
STANDING = pg.image.load("karakter1stå.png")
STANDING = pg.transform.scale(STANDING,(40,65))
STANDING2 = pg.image.load("karakter2stå.png")
STANDING2 = pg.transform.scale(STANDING2,(40,65))
STANDING3 = pg.image.load("karakter3stå.png")
STANDING3 = pg.transform.scale(STANDING3,(40,65))
STANDING4 = pg.image.load("karakter4stå.png")
STANDING4 = pg.transform.scale(STANDING4,(40,65))

RUNNING = pg.image.load("karakter1løpe.png")
RUNNING = pg.transform.scale(RUNNING,(40,65))
RUNNING2 = pg.image.load("karakter2løpe.png")
RUNNING2 = pg.transform.scale(RUNNING2,(40,65))
RUNNING3 = pg.image.load("karakter3løpe.png")
RUNNING3 = pg.transform.scale(RUNNING3,(40,65))
RUNNING4 = pg.image.load("karakter4løpe.png")
RUNNING4 = pg.transform.scale(RUNNING4,(40,65))
RUNNING5 = pg.image.load("karakter5løpe.png")
RUNNING5 = pg.transform.scale(RUNNING5,(40,65))
RUNNING6 = pg.image.load("karakter6løpe.png")
RUNNING6 = pg.transform.scale(RUNNING6,(40,65))

class player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect() # henter self.image sin størelse og
        self.pos = vec(650,570)
        self.rect.center = self.pos
        self.speed = 4
        self.liv = 5
        self.current_frame = 10
        self.last_update = 10

        self.standing = True
        self.running = True

        self.standing_frames = [STANDING,STANDING2,STANDING3,STANDING4]
        self.running_frame = [RUNNING,RUNNING2,RUNNING3,RUNNING4,RUNNING5,RUNNING6]

    def update(self):
        self.rect.center = self.pos # flytter rect til player til ny posisjon
        self.animate()

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= self.speed 

        if keys[pg.K_s]:
            self.pos.y += self.speed

        if keys[pg.K_a]:
            self.pos.x -= self.speed
            self.image = pg.transform.flip(player_img, True, False)

        if keys[pg.K_d]:
            self.pos.x += self.speed
            self.image = pg.transform.flip(player_img, False, False)


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
      
    def animate(self):
        now = pg.time.get_ticks()

        if self.standing:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame +1)% len(self.standing_frames)
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()  

        if self.running:
            if now - self.last_update  > 350:
                self.last_update = now
                self.current_frame = (self.current_frame +1)% len(self.running_frames)
                self.image = self.running_frame[self.current_frame]
                self.rect = self.image.get_rect()

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
        self.direction_x = 0
        self.direction_y = 0


    def update(self):
        self.rect.center = self.pos # flytter rect til player til ny posisjon
        
        self.pos.x += self.direction_x
        self.pos.y += self.direction_y


        if self.pos.x < self.game.karakter.pos.x:
            self.direction_x = 1
            self.image = self.image_right
            
        elif self.pos.x > self.game.karakter.pos.x:
            self.direction_x = -1
            self.image = self.image_left


        if self.pos.y < self.game.karakter.pos.y:
            self.direction_y = 1

        elif self.pos.y > self.game.karakter.pos.y:
            self.direction_y = -1

 
        if self.pos.x < -100: # til venstre for skjermen
                self.direction_x = randint(-1,10)

