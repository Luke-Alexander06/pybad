import pygame as pg
from random import randint
vec = pg.math.Vector2

karakter_img = pg.image.load("karakter4stå.png")
player_img = pg.transform.scale(karakter_img,(60,100)) # endre størelse på player image
enemy_img = pg.image.load("bos2.png")
enemy_img = pg.transform.scale(enemy_img,(300,300))

STANDING = pg.image.load('')
STANDING2 = pg.image.load('')
STANDING3 = pg.image.load('')
STANDING4 = pg.image.load('')


class player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect() # henter self.image sin størelse og
        self.pos = vec(100,100)
        self.rect.center = self.pos
        self.speed = 7
        self.liv = 5


    def update(self):
        self.rect.center = self.pos # flytter rect til player til ny posisjon
        
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= self.speed

        if keys[pg.K_s]:
            self.pos.y += self.speed

        if keys[pg.K_a]:
            self.pos.x -= self.speed

        if keys[pg.K_d]:
            self.pos.x += self.speed


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect() # henter self.image sin størelse og
        self.pos = vec(400,400)
        self.rect.center = self.pos
        self.speed = 10
        self.direction_x = -5
        self.direction_y = 1


    def update(self):
        self.rect.center = self.pos # flytter rect til player til ny posisjon

        self.pos.x += self.direction_x
        self.pos.y += self.direction_y


        if self.pos.x < -100: # til venstre for skjermen
           self.direction_x = randint(-1,10)
        





