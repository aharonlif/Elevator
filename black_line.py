import pygame as pg
import settings

class Line(pg.sprite.Sprite):
    """
    Represents a line (floor separator) in the building.

    Attributes:
        color (tuple): Color of the line.
        thickness (float): Thickness of the line.
        image (pg.Surface): Surface for the line sprite.
        rect (pg.Rect): Rectangle defining the dimensions and position of the line.
    """
    color = settings.LINE_COLOR
    thickness = settings.LINE_THICKNESS
    
    def __init__(self, bottomleft):
        """
        Initializes the Line object.

        Args:
            bottomleft (tuple): Bottom-left position of the line.
        """
        super().__init__()
        self.image = pg.Surface((settings.FLOOR_WIDTH, self.thickness))
        # self.image.fill(self.color)  # Ensure the line is filled with the specified color
        self.rect = self.image.get_rect(bottomleft=bottomleft)