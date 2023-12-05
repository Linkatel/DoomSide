import pygame as pg

_ = False
mini_map = [
    #0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21       x ->
    [_, _, _, _, _, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, _],#0
    [_, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _],#1
    [_, _, _, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _],#2
    [_, _, _, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, 3, _, _, _, _],#3
    [_, _, _, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _],#4
    [_, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _],#5       ^
    [_, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _],#6       |
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, _, _, 1, 1, 1, 3, 3, 1, 1, 1],#7
    [1, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, 3],#8       y
    [1, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, 3],#9
    [1, _, _, _, _, _, _, 1, 1, _, _, 1, 1, 1, 1, _, _, 1, 1, 1, 1, 3],#10
    [1, _, _, 3, 3, _, _, 1, 1, _, _, _, _, _, 1, _, _, _, _, _, _, 3],#11
    [1, _, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],#12
    [1, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],#13
    [1, 1, _, _, 1, 3, 3, 3, 1, 1, 1, 1, 1, 3, 3, 3, 1, 1, 3, 3, 1, 1],#14
    [1, _, _, _, 1, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _],#15
    [1, _, _, _, _, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, _],#16
    [1, _, _, _, _, _, _, _, _, 1, 1, _, _, _, _, _, _, 1, _, _, _, _],#17
    [1, _, _, _, _, _, _, _, _, 1, 1, _, _, _, _, _, _, 1, _, _, _, _],#18
    [1, _, _, _, _, _, _, _, _, 1, 1, _, _, _, _, _, _, 1, _, _, _, _],#19
    [1, _, _, _, _, _, _, _, _, 1, 1, _, _, _, _, _, _, 1, _, _, _, _],#20
    [1, 1, 1, 1, _, _, 1, 1, 1, 1, 1, 1, 1, _, _, 1, 1, 1, 1, 1, _, _],#21
    [1, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4, _, _],#22
    [1, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, 1, _, _],#23
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3, _, _, 1, _, _],#24
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, 1, _, _],#25
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, 1, _, _],#26
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3, _, _, 1, _, _],#27
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _],#28
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _],#29
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _],#30
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _],#31
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _],#32
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _],#33
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _],#34
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _],#35
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],#36
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
                    
    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2) for pos in self.world_map]
