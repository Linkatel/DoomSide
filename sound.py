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
        pg.mixer.music.set_volume(0.1)
        # Dialogue section
        self.Dialogue = "resources/sound/Dialogue/"
        self.Dialogue1 = pg.mixer.Sound(self.Dialogue + "Dialogue1.flac")
        pg.mixer.music.set_volume(15.0)
        self.Dialogue1.play()
        # Punchlines section
        self.punchlines = "resources/sound/punchlines/"
        self.punchline1 = pg.mixer.Sound(self.punchlines + "Im_gonna_make_you_eat_your_guts2.flac")
        pg.mixer.music.set_volume(1.0)
        self.punchline2 = pg.mixer.Sound(self.punchlines + "What_up_you_little_shit.flac")
        pg.mixer.music.set_volume(1.0)
        self.punchline3 = pg.mixer.Sound(self.punchlines + "Shh_shut_up.flac")
        pg.mixer.music.set_volume(1.0)
        self.punchline4 = pg.mixer.Sound(self.punchlines + "Hellooooo_its_me.flac")
        pg.mixer.music.set_volume(1.0)
        self.punchline5 = pg.mixer.Sound(self.punchlines + "Hey_Im_there.flac")
        pg.mixer.music.set_volume(1.0)
        self.punchline6 = pg.mixer.Sound(self.punchlines + "I_knew_a_one-eyed_man_who_aimed_better.flac")
        pg.mixer.music.set_volume(1.0)
        self.punchline7 = pg.mixer.Sound(self.punchlines + "Im_gonna_make_you_eat_your_guts2.flac")
        pg.mixer.music.set_volume(1.0)
        self.punchline8 = pg.mixer.Sound(self.punchlines + "Im_kick_your_ass_in_style.flac")
        pg.mixer.music.set_volume(1.0)