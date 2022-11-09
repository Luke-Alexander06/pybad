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
box_color = random 

all_sprites = pg.sprite.Group()

karakter = player()
all_sprites.add(karakter)

screen = pg.display.set_mode((1300,800))

fps_counter = 0

FPS = 120
clock = pg.time.Clock()
playing = True
while playing: # game loop
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    
    screen.fill(ORANGE) # tegner bakgrunn

    all_sprites.update() # kjør udsate funkjon til alle sprite i all_sprites

    # tegner alle sprites i gruppen all_sprites til screen
    all_sprites.draw(screen)

    pg.display.update()

    













