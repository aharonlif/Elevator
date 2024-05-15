import pygame as pg


# class absimg(pg.sprite.Sprite):
#     def __init__(self, image_path):
#         super()
#         pg.image.load(image_path)# TODO: check if can to do abstract class with image load instead in floor and elevator classes
class BlackLine(pg.sprite.Sprite):
    BLACK = (0, 0, 0)

    def __init__(self, start, end, width=4):
        super().__init__()
        self.image = pg.Surface((abs(end[0] - start[0]), abs(end[1] - start[1])))
        self.image.fill(self.BLACK)
        self.rect = self.image.get_rect(bottomleft=start)
class Floor(pg.sprite.Sprite):
    width, height = 150, 80
    def __init__(self, floor_number, bottomleft):
        super().__init__()
        self.image = pg.image.load("help_files/floor_image.png")
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(bottomleft=bottomleft)
        self.floor_number = floor_number
        height_beginning_buildings = 50
        #The height of the floor is the height where the building starts, 
        #plus the number of floors times the height of each floor plus the height of the dividing line as the number of lines between the floors
        self.rect_y = height_beginning_buildings + self.floor_number*self.height 

class Elevator(pg.sprite.Sprite):
    width, height = 80, 80
    def __init__(self, bottomleft):
        super().__init__()
        self.image = pg.image.load("help_files/elv.png")
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(bottomleft=bottomleft)
