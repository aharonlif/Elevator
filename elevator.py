import pygame as pg
import time

import settings

class Elevator(pg.sprite.Sprite):
    """
    Represents an elevator in a building.

    Attributes:
        width (int): The width of the elevator.
        height (int): The height of the elevator.
        arrived_sound (pg.mixer.Sound): Sound to play when the elevator arrives.
        floor_travel_time (float): Time taken to travel one floor.
        floor (int): Target floor for the elevator.
        current_floor (int): Current floor of the elevator.
        movement_last_time (float): Time when the movement to the target floor started.
        arrival_time (int): Time until the elevator arrives at the target floor.
        y_position (float): Y position of the elevator.
    """
    width, height = settings.FLOOR_HIGHT, settings.FLOOR_HIGHT
    pg.mixer.init()
    arrived_sound = pg.mixer.Sound("help_files/ding.mp3")
    floor_travel_time = 0.5 

    def __init__(self, bottomleft):
        """
        Initializes the Elevator object.

        Args:
            bottomleft (tuple): Bottom-left position of the elevator.
        """
        super().__init__()
        self.image = pg.image.load("help_files/elv.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (self.width, self.height)).convert_alpha()
        self.rect = self.image.get_rect(bottomleft=bottomleft)
        self.made_a_sound = False
        self.floor = 0
        self.current_floor = 0
        self.movement_last_time = None
        self.last_drawn_time = 0
        self.arrival_time = 0
        self.free = True
        self.y_position = bottomleft[1]  # Y position at start
        self.move_to_floors = []

    def moving(self) -> bool:
        
        return self.floor != self.current_floor

    def move_to_floor(self, floor):
        """
        Sets the target floor for the elevator and starts the movement.

        Args:
            floor (int): Target floor.
        """
        if  not self.free:
            if not (self.move_to_floors):
                arrival_time = self.arrival_time + 2 + abs(self.floor - floor)/2 
            else:
                arrival_time = self.move_to_floors[-1]["arrival time"] + 2 + abs(self.move_to_floors[-1]["floor"] - floor)/2
            
            self.move_to_floors.append({"floor": floor, "arrival time": arrival_time})
            return
        if self.moving():
            raise (TypeError("Bug in the free argument"))
        self.free = False
        self.floor = floor
        self.movement_last_time = time.time()
        self.arrival_time = int(abs(self.floor - self.current_floor))/2

        
    def calculate_arrival_time(self):
        
        current_time = time.time()
        elapsed_time = current_time - self.movement_last_time
        self.arrival_time -= elapsed_time
        if self.arrival_time <= -2:
            self.free = True
        for floor in self.move_to_floors:
            floor["arrival time"] -= elapsed_time
        self.movement_last_time = current_time
        return elapsed_time

    def calculate_position_to_move(self):
        """
        Calculates the new position of the elevator based on the elapsed time.

        Returns:
            float: New Y position of the elevator.
        """
        elapsed_time = self.calculate_arrival_time()
        floors_to_move = elapsed_time / self.floor_travel_time
        y_move = floors_to_move * settings.FLOOR_HIGHT
        self.y_position += y_move if self.current_floor > self.floor else -y_move
        return self.y_position

    def free(self):
        return self.free

   
    def update(self):                    
        if self.free:
            self.movement_last_time = 0
            self.made_a_sound = False
            
            if self.move_to_floors:

                floor = self.move_to_floors[0]["floor"]
                self.arrival_time = self.move_to_floors[0]["arrival time"]
                self.move_to_floors.pop(0)
                self.move_to_floor(floor)
            else:
                return
        self.update_location()

    def update_location(self):
        """
        Updates the location of the elevator and handles arrival logic.

        Returns:
            bool: True if the elevator is moving, False otherwise.
        """
        if not self.moving():
            if self.free:
                return False
            self.calculate_arrival_time()
            return False

        if self.arrived():
            if not self.made_a_sound:
                self.arrived_sound.play()
                self.made_a_sound = True
                self.arrival_time = 0
                self.current_floor = self.floor
                return True

        y_position = self.calculate_position_to_move()
        self.rect.bottomleft = (self.rect.x, y_position)
        return True

    def arrived(self):
        """
        Checks if the elevator has arrived at the target floor.

        Returns:
            bool: True if the elevator has arrived, False otherwise.
        """
        floor = settings.FLOOR_HIGHT + settings.LINE_THICKNESS
        y_hight = settings.SCREEN_HIGHT - self.y_position
        return (floor * self.floor) <= y_hight if self.floor > self.current_floor else (floor * self.floor) >= y_hight