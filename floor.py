import pygame as pg
from button import Button
from settings import Floor as f
import time

class Floor(pg.sprite.Sprite):
    """
    Represents a floor in a building with a button for elevator calls.
    """
    width, height = f.width, f.height

    def __init__(self, floor_number, bottomleft):
        """
        Initializes the Floor object.
        
        Args:
            floor_number (int): The number of the floor.
            bottomleft (tuple): The bottom-left position of the floor.
        """
        super().__init__()
        self.image = pg.image.load("help_files/floor_image.png")
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(bottomleft=bottomleft)
        self.floor_number = floor_number
        self.button = Button(self.floor_number)
        self.button.rect.center = self.rect.center  # Set the button's position relative to the floor
        self.draw_button()
        self.font = pg.font.SysFont(None, int(self.button.text_size / 2))
    
    def change_color(self, color, time_to_change):
        self.button.color =  color
        self.button.image = self.button.create_button_image()
        self.draw_button()
        self.time_chaneged_color = time_to_change

    def return_original_color(self):
        self.change_color(Button.color, None)

    def change_color_temporarily(self):
        self.change_color((0, 255, 0), time.time())

    def update(self, arrival_time):
        if self.time_chaneged_color:
            if time.time() - self.time_chaneged_color >= 0.08:
                self.return_original_color()
        self.update_time_elevator(arrival_time)


    def update_time_elevator(self, arrival_time):
        """
        Updates the display with the time until the elevator arrives.
        
        Args:
            arrival_time (int, optional): The time until the elevator arrives. Defaults to 99.
        """
        # arrival_time = int(abs(self.floor - self.current_floor))/2
        # self.arrival_time = arrival_time - (time.time() - self.movement_last_time)
        time_elevator = arrival_time
        text_surface = self.font.render(str(time_elevator), True, (20, 200, 200))
        text_rect = text_surface.get_rect(center=(self.width // 2 - self.button.size[0], self.height // 2))
        self.image.blit(text_surface, text_rect)

    def draw_button(self):
        """
        Draws the button on the floor.
        """
        button_size = self.button.size[0]  # Height equals width
        center_floor = self.width / 2 - button_size / 2, self.height / 2 - button_size / 2
        self.image.blit(self.button.image, center_floor)
