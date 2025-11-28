# � 2023 Linkatel. All rights reserved

from sprite_object import *
from random import randint, random
from sound import *
import random
import time
from main import NPC_PUNCHLINE_EVENT

class NPC(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/npc/soldier/0.png', pos=(10.5, 5.5),
                 scale=0.6, shift=3.1, animation_time=180):
        super().__init__(game, path, pos, scale, shift, animation_time)
        # Tous les dossiers d'animation
        self.attack_images = self.get_images(self.path + '/attack')
        self.death_images = self.get_images(self.path + '/death')
        self.idle_images = self.get_images(self.path + '/idle')
        self.pain_images = self.get_images(self.path + '/pain')
        self.walk_images = self.get_images(self.path + '/walk')

        self.attack_dist = randint(3, 6)
        self.speed = 1.8
        self.size = 20
        self.health = 100
        self.attack_damage = 10
        self.accuracy = 0.15
        self.alive = True
        self.pain = False
        self.ray_cast_value = False
        self.frame_counter = 0
        self.player_search_trigger = False

        # Attribut pour stocker le son de punchline sélectionné
        self.selected_punchline = None  # initialisé à None par défaut

                
    def update(self):
        self.check_animation_time()
        self.get_sprite()
        self.run_logic()
        #self.draw_ray_cast()
        
    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map
    
    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx * self.size), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * self.size)):
            self.y += dy
        
    def movement(self):
        next_pos = self.game.pathfinding.get_path(self.map_pos, self.game.player.map_pos)
        next_x, next_y = next_pos
        
        if next_pos not in self.game.object_handler.npc_positions:
            angle = math.atan2(next_y + 0.5 - self.y, next_x + 0.5 - self.x)
            step = self.speed * self.game.delta_time
            dx = math.cos(angle) * step
            dy = math.sin(angle) * step
            self.check_wall_collision(dx, dy)
        
    def attack(self):
        if ENABLE_DAMAGE == True:
            if self.animation_trigger:
                self.game.sound.npc_shot.play()
                if random() < self.accuracy:
                    self.game.player.get_damage(self.attack_damage)
        
    def animate_death(self):
        if not self.alive:
            if self.game.global_trigger and self.frame_counter < len(self.death_images) - 1:
                self.death_images.rotate(-1)
                self.image = self.death_images[0]
                self.frame_counter += 1
        
    def animate_pain(self):
        self.animate(self.pain_images)
        if self.animation_trigger:
            self.pain = False
        
    def check_hit_in_npc(self):
        if self.ray_cast_value and self.game.player.shot:
            if HALF_WIDTH - self.sprite_half_width < self.screen_x < HALF_WIDTH + self.sprite_half_width:
                self.game.sound.npc_pain.play()
                self.game.player.shot = False
                self.pain = True
                self.health -= self.game.weapon.damage
                self.check_health()
                
                
    def check_health(self):
        if self.health < 1:
            self.alive = False
            self.game.sound.npc_death.play()

            # Planifier le punchline après 1 seconde (1000 ms)
            pg.time.set_timer(NPC_PUNCHLINE_EVENT, 1000, loops=1)

   # def handle_event(self, event):
        #""" Gère les événements pour tous les NPC """
        #if event.type == NPC_PUNCHLINE_EVENT:
        #    punchline_sounds = [
        #        self.game.sound.punchline1,
        #        self.game.sound.punchline2,
        #        self.game.sound.punchline3,
        #        self.game.sound.punchline4,
        #        self.game.sound.punchline5,
        #        self.game.sound.punchline6,
        #        self.game.sound.punchline7,
        #    ]
        #    self.selected_punchline = random.choice(punchline_sounds)
        #    self.game.sound.punchline_channel.play(self.selected_punchline, loops=0) # 'Sound' object has no attribute 'punchline_channel'



        
    def run_logic(self):
        if self.alive:
            self.ray_cast_value = self.ray_cast_player_npc()
            self.check_hit_in_npc()
            if self.pain:
                self.animate_pain()

            elif self.ray_cast_value:
                self.player_search_trigger = True

                if self.dist < self.attack_dist:
                    self.animate(self.attack_images)
                    self.attack()
                else:
                    self.animate(self.walk_images)
                    self.movement()

            elif self.player_search_trigger:
                self.animate(self.walk_images)
                self.movement()

            else:
                self.animate(self.idle_images)
        else:
            self.animate_death()

        # Vérifie si un punchline a été joué, et si le canal est libre
        if self.selected_punchline and not self.game.sound.punchline_channel.get_busy():
            self.selected_punchline = None


        
                
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
    
    def ray_cast_player_npc(self):
        if self.game.player.map_pos == self.map_pos:
            return True

        wall_dist_v, wall_dist_h = 0, 0
        player_dist_v, player_dist_h = 0, 0

        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.theta

        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

        depth_hor = (y_hor - oy) / sin_a
        x_hor = ox + depth_hor * cos_a

        delta_depth = dy / sin_a
        dx = delta_depth * cos_a

        for i in range(MAX_DEPTH):
            tile_hor = int(x_hor), int(y_hor)
            if tile_hor == self.map_pos:
                player_dist_h = depth_hor
                break
            if tile_hor in self.game.map.world_map:
                wall_dist_h = depth_hor
                break
            x_hor += dx
            y_hor += dy
            depth_hor += delta_depth

        x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

        depth_vert = (x_vert - ox) / cos_a
        y_vert = oy + depth_vert * sin_a

        delta_depth = dx / cos_a
        dy = delta_depth * sin_a

        for i in range(MAX_DEPTH):
            tile_vert = int(x_vert), int(y_vert)
            if tile_vert == self.map_pos:
                player_dist_v = depth_vert
                break
            if tile_vert in self.game.map.world_map:
                wall_dist_v = depth_vert
                break
            x_vert += dx
            y_vert += dy
            depth_vert += delta_depth

        player_dist = max(player_dist_v, player_dist_h)
        wall_dist = max(wall_dist_v, wall_dist_h)

        if 0 < player_dist < wall_dist or not wall_dist:
            return True
        return False
    
    
            
class SoldierZombieNPC(NPC):
    def __init__(self, game, path='resources/sprites/npc/soldier/0.png', pos=(10.5, 5.5),
                 scale=0.6, shift=3.1, animation_time=180):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_dist = 2.5
        self.health = 200
        self.attack_damage = 25
        self.speed = 1.8
        self.accuracy = 0.35

class ZombieNPC(NPC):
    def __init__(self, game, path='resources/sprites/npc/caco_demon/0.png', pos=(10.5, 6.5),
                 scale=0.7, shift=3.1, animation_time=250):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_dist = 1.0
        self.health = 100
        self.attack_damage = 15
        self.speed = 3.0
        self.accuracy = 0.35

class CyberDemonNPC(NPC):
    def __init__(self, game, path='resources/sprites/npc/cyber_demon/0.png', pos=(11.5, 6.0),
                 scale=1.0, shift=3.4, animation_time=210):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_dist = 6
        self.health = 500
        self.attack_damage = 20
        self.speed = 4.8
        self.accuracy = 0.25
    
