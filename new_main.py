import pygame as pg
from sprites import *

class game():
    def __init__(self):
        pg.init()

        self.HITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.BLUE = (0,0,255)
        self.GREEN = (0,255,0)       
        self.RED = (255,0,0)
        self.ORANGE = (255, 118, 59)
        random = (0,0,0)
        self.GREY = (125,124,124)
        self.box_color = random 
        
        self.tekst = pg.font.SysFont ("arial", 75)

        self.WIDTH = 2000
        self.HEIGHT = 1200


        self.FPS = 120
        self.clock = pg.time.Clock()
        
        self.new()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()

        self.karakter = player()     
        self.enemy = Enemy(self)

        self.all_sprites.add(self.karakter, self.enemy)
        self.enemy_group.add(self.enemy)

        self.screen = pg.display.set_mode((self.WIDTH,self.HEIGHT))
        self.bg = pg.image.load("kart.png").convert_alpha()
        self.bg = pg.transform.scale(self.bg,(self.WIDTH,self.HEIGHT)) 
        self.tekst_player_hp = self.tekst.render("HP: " + str(self.karakter.liv), False, (self.RED))


        self.run()    

    def run(self):
     
        playing = True
        while playing: # game loop
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing = False
            
            self.screen.blit(self.bg,(0,0)) # tegner bakgrunn
            

            self.all_sprites.update() # kjør udsate funkjon til alle sprite i all_sprites
            
            hits = pg.sprite.spritecollide(self.karakter,self.enemy_group, True)
            if hits: 
                self.karakter.liv -= 1
                print("LIV ",self.karakter.liv)
                if self.karakter.liv <= 0:
                    self.karakter.kill()
                    self.karakter = player()
                    self.all_sprites.add()
                self.tekst_player_hp = self.tekst.render("HP: " + str(self.karakter.liv), False, (self.RED))

            # lag nye fiender 
            if len(self.enemy_group) < 1:
                self.enemy = Enemy(self)
                self.all_sprites.add(self.enemy)
                self.enemy_group.add(self.enemy)

            # tegner alle sprites i gruppen all_sprites til screen
            

            
            self.screen.blit(self.tekst_player_hp, (10, 10))
            self.all_sprites.draw(self.screen)
            
            pg.display.update()


g = game() # starter game class