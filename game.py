import pygame as pg
from random import randint

pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
ORANGE = (255, 118, 59)
random = (0,0,0)
box_color = random 

screen = pg.display.set_mode((1300,800))
karakter_img = pg.image.load("karakter.png")
player_img = pg.transform.scale(karakter_img,(110,165)) # endre størelse på player image

fps_counter = 0

x = 50
y = 50

speed = 5

direction_x = 1
direction_y = 1

FPS = 120
clock = pg.time.Clock()
playing = True
while playing: # game loop
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    
    screen.fill(ORANGE) # tegner bakgrunn
    # move box
    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        y -= speed
    if keys[pg.K_s]:
        y += speed
    if keys[pg.K_a]:
        x -= speed
    if keys[pg.K_d]:
        x += speed




    # sjekk hvis utfor skjerm
    if x > 700:
        x = 700
    if x < 0:
        x = 0
    if y > 500:
        y = 500
    if y < 0:
        y = 0
        
    screen.blit(player_img, (x,y))
    pg.display.update()

    













