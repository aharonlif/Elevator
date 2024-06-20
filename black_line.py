import pygame as pg

from settings import Line as l

class Line(pg.sprite.Sprite):
    color = l.color
    thickness = l.thickness
    def __init__(self, start_pos, end_pos):
        super().__init__()
        self.start_pos = start_pos[0]
        self.end_pos = end_pos[0]

        x1, y1 = start_pos
        x2, y2 = end_pos
        self.image = pg.Surface((abs(x2 - x1) + self.thickness, abs(y2 - y1) + self.thickness))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x1, y1)
