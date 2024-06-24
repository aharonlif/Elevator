import pygame as pg
from floor import Floor as flr
from black_line import Line
from elevator import Elevator as elv
from settings import Screen

class Building(pg.sprite.Group):
    """
    Represents a building containing multiple floors and elevators.
    Manages the elevators and their movements.
    """
    difference_building = flr.width * 2 + elv.width

    def __init__(self, floors: int, elevators: int, building_number=0, x_position=0):
        """
        Initializes the Building object.
        
        Args:
            floors (int): The number of floors in the building.
            elevators (int): The number of elevators in the building.
            building_number (int, optional): The building number for positioning. Defaults to 0.
            x_position (int, optional): The x-coordinate for the building position. Defaults to 0.
        """
        super().__init__()
        self.floors = [None] * floors
        self.elevators = [None] * elevators
        self.x_position = x_position
        self.number = building_number
        self.calculate_x_position()
        self.floors_factory()
        self.elevators_factory(elevators)
        self.calls_to_the_elevator = []

    def calculate_x_position(self):
        """
        Calculates the x position of the building based on its number and the number of elevators.
        """
        if self.number and not self.x_position:
            plase_elvs = len(self.elevators) * elv.width + flr.width
            self.x_position = (plase_elvs) * self.number

    def floors_factory(self):
        """
        Creates the floors for the building and adds them to the sprite group.
        Draws lines between the floors.
        """
        y_position = Screen.height
        line_y_position = Screen.height
        for i in range(len(self.floors)):
            self.floors[i] = flr(i, bottomleft=(self.x_position, y_position))
            self.add(self.floors[i])
            y_position -= flr.height + Line.thickness

            if i == 1:  # If i == 0 don't need to draw black line, only between floors.
                line_y_position -= flr.height
                self.add(Line(bottomleft=(self.x_position, line_y_position)))
                continue

            if i:
                line_y_position -= flr.height + Line.thickness
                self.add(Line(bottomleft=(self.x_position, line_y_position)))

    def elevators_factory(self, elevators):
        """
        Creates the elevators for the building and adds them to the sprite group.
        
        Args:
            elevators (int): The number of elevators to create.
        """
        for i in range(elevators):
            x_position = self.x_position + flr.width + (i * elv.width)
            y_position = Screen.height
            elevator = elv(bottomleft=(x_position, y_position))
            self.add(elevator)
            self.elevators[i] = elevator

    def _find_nearest_elevator(self, floor):
        """
        Finds the nearest available elevator to the given floor.
        
        Args:
            floor (int): The floor number to find the nearest elevator to.
        
        Returns:
            Elevator: The nearest available elevator.
        """
        try:
            nearest_elevator = min(
                (elevator for elevator in self.elevators if not (elevator.moving() and elevator.floor != floor)), 
                key=lambda elevator: abs(elevator.floor - floor)
            )
        except Exception:
            if floor not in self.calls_to_the_elevator:
                self.calls_to_the_elevator.append(floor)
            return
        return nearest_elevator

    def move_elevator(self, floor):
        """
        Moves the nearest available elevator to the specified floor.
        
        Args:
            floor (int): The floor number to move the elevator to.
        
        Returns:
            bool: True if an elevator was moved, otherwise False.
        """
        nearest_elevator = self._find_nearest_elevator(floor)
        if nearest_elevator:
            nearest_elevator.move_to_floor(floor)
            self.floors[floor].an_elevator_that_arrives = nearest_elevator
            return True

    def change_button_color(self, floor=0):
        """
        Changes the color of the button on the specified floor temporarily.
        
        Args:
            floor (int, optional): The floor number of the button to change color. Defaults to 0.
        """
        self.floors[floor].change_color_temporarily()

    def update(self):
        """
        Updates the state of the building, moving elevators as needed.
        Processes any pending elevator calls.
        """
        if self.calls_to_the_elevator:
            if self.move_elevator(self.calls_to_the_elevator[0]):
                self.calls_to_the_elevator.pop(0)
        for elv in self.elevators:
            if elv.update_location():
                floor = elv.floor
                self.floors[floor].update_time_elevator(elv.arrival_time)