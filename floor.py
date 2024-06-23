import pygame as pg

from button import Button
from settings import Floor as f

class Floor(pg.sprite.Sprite):
    width, height = f.width, f.height
    def __init__(self, floor_number, bottomleft):
        super().__init__()
        self.image = pg.image.load("help_files/floor_image.png")
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(bottomleft=bottomleft)
        self.floor_number = floor_number
        self.button = Button(self.floor_number)
        self.button.rect.center = self.rect.center  # Add this line to set the button's position relative to the floor

        self.draw_button()
        self.font = pg.font.SysFont(None, 30)
        self.time_elevator = None      

    def update_time_elevator(self):
        self.time_elevator = 5
        text_surface = self.font.render(str(self.number), True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.size[0] // 2, self.size[1] // 2))

    def draw_button(self):
        button_size = self.button.size[0] # Height = width
        center_floor = self.width/2 - button_size/2, self.height/2 - button_size/2
        self.image.blit(self.button.image, center_floor)
