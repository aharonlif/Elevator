import pygame as pg


class Elevator(pg.sprite.Sprite):
    width, height = 80, 80
    def __init__(self, bottomleft):
        super().__init__()
        self.image = pg.image.load("help_files/elv.png")
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(bottomleft=bottomleft)

    def move(self, floor):
        pass
    


