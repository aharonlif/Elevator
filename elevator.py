import pygame as pg
import time
from floor import Floor
from black_line import Line
import settings


class Elevator(pg.sprite.Sprite):
    width, height = settings.Floor.height, settings.Floor.height
    def __init__(self, bottomleft):
        super().__init__()
        self.image = pg.image.load("help_files/elv.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (self.width, self.height)).convert_alpha()
        self.rect = self.image.get_rect(bottomleft=bottomleft)
        pg.mixer.init()
        self.arrived_sound = pg.mixer.Sound("help_files/ding.mp3")

        self.floor = 0
        self.current_floor = 0
        self.movement_last_time = None
        self.y_position = bottomleft[1]  # y position at start

    def moving(self) -> bool:
        return self.floor != self.current_floor

    def move_to_floor(self, floor):
        self.floor = floor
        self.movement_last_time = time.time()
        
    def calculate_position_to_move(self):
        # if self.movement_start_time is None:
        #     return self.y_position
        floor_travel_time = 0.5 
        current_time = time.time()
        elapsed_time = current_time - self.movement_last_time
        floors_to_move = elapsed_time / floor_travel_time
        y_move = floors_to_move * settings.Floor.height
        self.movement_last_time = current_time
        self.y_position += y_move if self.current_floor > self.floor else -y_move
        return self.y_position

    def passed_2_seconds(self):
        current_time = time.time()
        elapsed_time = current_time - self.movement_last_time
        return elapsed_time > 2

    def update_location(self):
        if not self.moving():
            return
        
        if self.arrived(): #todo: declare only ==, with change y position when it more from floor
            if self.passed_2_seconds():
                self.current_floor = self.floor
                self.arrival_sound()
            return
            
        y_position = self.calculate_position_to_move()
        self.rect.bottomleft = (self.rect.x, y_position)
        
    def arrival_sound(self):
        self.arrived_sound.play()

    def arrived(self):
        floor = Floor.height + Line.thickness
        y_hight = settings.Screen.hight - self.y_position

        return (floor * self.floor) < y_hight if self.floor > self.current_floor else (floor * self.floor) > y_hight


