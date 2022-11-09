import pygame as pg
vec = pg.math.Vector2

karakter_img = pg.image.load("karakter.png")
player_img = pg.transform.scale(karakter_img,(110,165)) # endre størelse på player image


class player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect() # henter self.image sin størelse og
        self.pos = vec(100,100)
        self.rect.center = self.pos
        self.speed = 5


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

        

        





