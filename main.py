# � 2023 Linkatel. All rights reserved

import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *

import pygame as pg

def get_resolution():
    pg.init()
    fenetre = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 36)

    resolutions = {
        pg.K_1: (640, 480),
        pg.K_2: (800, 600),
        pg.K_3: (1024, 768),
        pg.K_4: (1280, 720),
        pg.K_5: (1920, 1080)
    }

    texts = [
        "Choose a resolution:",
        "1. 640x480",
        "2. 800x600",
        "3. 1024x768",
        "4. 1280x720",
        "5. 1920x1080",
        "Press a key (1-5) to select."
    ]

    rendered_texts = [font.render(text, True, (255, 255, 255)) for text in texts]

    running = True
    chosen_resolution = None

    while running:
        fenetre.fill((0, 0, 0))
        for i, text in enumerate(rendered_texts):
            fenetre.blit(text, (15, 30 * i))

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.KEYUP:
                if event.key in resolutions:
                    chosen_resolution = resolutions[event.key]
                    running = False

    pg.quit()
    return chosen_resolution



class Game:
    def __init__(self, resolution):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(resolution)
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        pg.display.set_icon(pg.image.load('./resources/ico/DoomSide-ico.ico'))
        self.new_game()
        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.sprite_object = SpriteObject(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)
    
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.sprite_object.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption('DoomSide')                 #afficher les fps sur la fenetre : f'{self.clock.get_fps():.1f}'
        
        
    def draw(self):
        self.object_renderer.draw()
        self.weapon.draw()
        
    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
                
            for npc in self.object_handler.npc_list:
                npc.handle_event(event)
            self.player.single_fire_event(event)
        
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            
if __name__ == '__main__':
    resolution = get_resolution()
    game = Game(resolution)
    game.run()