import pygame as pg

from button import Button


class Floor(pg.sprite.Sprite):
    width, height = 150, 80
    def __init__(self, floor_number, bottomleft):
        super().__init__()
        self.image = pg.image.load("help_files/floor_image.png")
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(bottomleft=bottomleft)
        self.floor_number = floor_number
        self.button = Button(self.floor_number)
        self.button.rect.center = self.rect.center  # Add this line to set the button's position relative to the floor

        self.draw_button()
      
    def draw_button(self):
        button_size = self.button.size[0] # Height = width
        center_floor = self.width/2 - button_size/2, self.height/2 - button_size/2
        self.image.blit(self.button.image, center_floor)
