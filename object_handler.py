# � 2023 Linkatel. All rights reserved

from sprite_object import *
from npc import *
import random
import math
import pygame as pg


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = "resources/sprites/npc/"
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

      # add_npc("Name"(game, pos=(x, y)))
        add_npc(SoldierZombieNPC(game, pos=(3, 12)))
        add_npc(SoldierZombieNPC(game, pos=(20, 9)))
        add_npc(SoldierZombieNPC(game, pos=(20, 13)))
        add_npc(SoldierZombieNPC(game, pos=(7, 17)))
        add_npc(SoldierZombieNPC(game, pos=(3, 20)))
        add_npc(ZombieNPC(game, pos=(14, 12)))
        add_npc(ZombieNPC(game, pos=(8, 19)))
        add_npc(ZombieNPC(game, pos=(10, 22)))
        add_npc(ZombieNPC(game, pos=(15, 22)))
        add_npc(ZombieNPC(game, pos=(10, 38)))
        add_npc(CyberDemonNPC(game, pos=(10, 33)))

    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(17000)
            self.game.new_game()
            
    def check_menu(self):
        pass

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()

        
    def add_npc(self, npc):
        self.npc_list.append(npc)


    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
        
    
