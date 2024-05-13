import pygame as pg
import sys


class p:
    def __init__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
    def pr():
        print ("llllllllll")
class Floor(pg.sprite.Sprite):
    def __init__(self, floor_number):
        super().__init__()

        self.width = 10
        self.height = 4
        self.image = pg.Surface((800, 600))
        self.floor_number = floor_number
        # self.buildings = []
        # self.surface.fill((255, 255, 255))
        self.rect = self.image.get_rect()

    def convert_to_right_size(width, height, image_path):
        image = pg.image.load(image_path).convert_alpha()
        image = pg.transform.scale(image, (width, height))
        return image

