# � 2023 Linkatel. All rights reserved

import pygame as pg
import pygame as pg1

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = "resources/sound/"
        self.shotgun = pg.mixer.Sound(self.path + "shotgun.wav")
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.npc_pain.set_volume(0.2)
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.npc_shot.set_volume(0.2)
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.player_pain.set_volume(0.1)
        self.theme = pg.mixer.music.load(self.path + 'DoomSide.wav')
        pg.mixer.music.set_volume(0.7)
        self.punchlines = "resources/sound/punchlines/"
        self.punchline1 = pg.mixer.Sound(self.punchlines + "You really wanna kill me.wav")
        self.player_pain.set_volume(100)
        self.punchline2 = pg.mixer.Sound(self.punchlines + "Asshole.wav")
        self.player_pain.set_volume(100)
        self.punchline3 = pg.mixer.Sound(self.punchlines + "shut_up.wav")
        self.player_pain.set_volume(100)