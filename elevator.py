import pygame as pg
import time
from floor import Floor
from black_line import Line
from settings import Screen


class Elevator(pg.sprite.Sprite):
    width, height = 80, 80
    def __init__(self, bottomleft):
        super().__init__()
        self.image = pg.image.load("help_files/elv.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (self.width, self.height)).convert_alpha()
        self.rect = self.image.get_rect(bottomleft=bottomleft)
        self.floor = 0
        self.current_floor = 0
        self.movement_last_time = None
        self.y_position = bottomleft[1]  # y position in start

    def moving(self) -> bool:
        return self.floor != self.current_floor

    def move_to_floor(self, floor):
        self.floor = floor
        self.movement_last_time = time.time()
        
    def calculate_position_to_move(self):
        # if self.movement_start_time is None:
        #     return self.y_position
        
        current_time = time.time()
        elapsed_time = current_time - self.movement_last_time
        y_move = elapsed_time/5 #TODO this bettetr


        # # Clamp the position to the target position
        # if (direction == 1 and self.y_position >= target_y_position) or (direction == -1 and self.y_position <= target_y_position):
        #     self.y_position = target_y_position
        #     self.current_floor = self.floor.floor_number
        #     self.movement_start_time = None  # Stop the movement
        # else:
        #     # Update the movement start time for the next calculation
        #     self.movement_start_time = current_time - (elapsed_time % 0.5)
        towards = 1 if self.floor < self.current_floor else -1
        y_move *= towards
        self.y_position += y_move
        return self.y_position


    def update_location(self):
        if not self.moving():
            return
        
        if self.the_y_crossed_the_floor(): #TODO declare only ==, with change y position when it more from floor
                self.current_floor = self.floor
                self.elevator_arrival_sound()
                return
        y_position = self.calculate_position_to_move()
        self.rect.bottomleft = (self.rect.x, y_position)
        
    def elevator_arrival_sound(self):
        pg.mixer.init()
        self.arrival_sound = pg.mixer.Sound("help_files/ding.mp3")
        self.arrival_sound.play()

    def the_y_crossed_the_floor(self):
        floor = Floor.height + Line.thickness
        y_hight = Screen.hight - self.y_position

        return (floor * self.floor) < y_hight if self.floor > self.current_floor else (floor * self.floor) > y_hight


