import pygame as pg

import settings

class Line(pg.sprite.Sprite):
    color = settings.Line.color
    thickness = settings.Line.thickness
    def __init__(self, bottomleft):
        super().__init__()
        self.image = pg.Surface((settings.Floor.width, self.thickness))
        self.rect = self.image.get_rect(bottomleft=bottomleft)
