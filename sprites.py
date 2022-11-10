import pygame as pg
from random import randint
vec = pg.math.Vector2

karakter_img = pg.image.load("karakter2.png")
player_img = pg.transform.scale(karakter_img,(60,100)) # endre størelse på player image
enemy_img = pg.image.load("bos2.png")
enemy_img = pg.transform.scale(enemy_img,(300,300))


class player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect() # henter self.image sin størelse og
        self.pos = vec(100,100)
        self.rect.center = self.pos
        self.speed = 7


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
        self.pos = vec(randint(0,1400),randint(0,800))
        self.rect.center = self.pos
        self.speed = 10


    def update(self):
        self.rect.center = self.pos # flytter rect til player til ny posisjon

        self.pos.x -= self.speed

        if self.pos.x < -100: # til venstre for skjermen
            self.pos.x = 1500
            self.pos.y = randint(0,900)

        





