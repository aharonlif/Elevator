import pygame as pg

import floor as floor_file




class PartingLine:
    """
        This class creates a black background so that there will be black separation lines between the floors of the building.
        Streamlining the code in building one object instead of several lines of separation   
     """
    width = 7
    def __init__(self, floors, bildings=0): #TODO Delete building argument, define location in Building class instead. The class also needs to be fixed.
        height = floors * (floor_file.Floor.height + self.width) - self.width #TODO A correct width corresponds to the number of floors in the building
        length = floor_file.Floor.width 
        # image = pg.Surface((width, height))
        # image.fill((0,0,0))
        # self.rect = self.image.get_rect(width, height)




class BlackLine(pg.sprite.Sprite):
    """Delete this and create a black background    
    """
    BLACK = (0, 0, 0)

    def __init__(self, start, end, width=4):
        super().__init__()
        self.image = pg.Surface((abs(end[0] - start[0]), abs(end[1] - start[1])))
        self.image.fill(self.BLACK)
        self.rect = self.image.get_rect(bottomleft=start)
