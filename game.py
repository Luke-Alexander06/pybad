import pygame as pg
from random import randint
from sprites import *

pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
ORANGE = (255, 118, 59)
random = (0,0,0)
GREY = (125,124,124)
box_color = random 

WIDTH = 2000
HEIGHT = 1200

all_sprites = pg.sprite.Group()
enemy_group = pg.sprite.Group()

karakter = player()
enemy = Enemy()


all_sprites.add(karakter, enemy)
enemy_group.add(enemy)

screen = pg.display.set_mode((WIDTH,HEIGHT))
bg = pg.image.load("kart.png").convert_alpha()
bg = pg.transform.scale(bg,(WIDTH,HEIGHT))

fps_counter = 0

FPS = 120
clock = pg.time.Clock()



playing = True
while playing: # game loop
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    
    screen.blit(bg,(0,0)) # tegner bakgrunn
    

    all_sprites.update() # kjør udsate funkjon til alle sprite i all_sprites
    
    hits = pg.sprite.spritecollide(karakter,enemy_group, True)
    if hits: 
        karakter.liv -= 1
        print("LIV ",karakter.liv)
        if karakter.liv <= 0:
            karakter.kill()
            karakter = player()
            all_sprites.add()
        

    # lag nye fiender 
    if len(enemy_group) < 1:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemy_group.add(enemy)

    # tegner alle sprites i gruppen all_sprites til screen
    all_sprites.draw(screen)









    pg.display.update()

    













