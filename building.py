import pygame as pg
from floor import Floor as flr
from black_line import Line
from elevator import Elevator as elv
import settings

class Building(pg.sprite.Group):
    """
    Represents a building containing multiple floors and elevators.
    Manages the elevators and their movements.
    """

    def __init__(self, build, x_position):
        """
        Initializes the Building object.
        
        Args:
            floors (int): The number of floors in the building.
            elevators (int): The number of elevators in the building.
            building_number (int, optional): The building number for positioning. Defaults to 0.
            x_position (int, optional): The x-coordinate for the building position. Defaults to 0.
        """
        super().__init__()
        self.floors = [None] * build["floors"]
        self.elevators = [None] * build["elevators"]
        self.x_position = x_position
        self.floors_factory()
        self.elevators_factory()


    def floors_factory(self):
        """
        Creates the floors for the building and adds them to the sprite group.
        Draws lines between the floors.
        """
        y_position = settings.SCREEN_HIGHT
        line_y_position = settings.SCREEN_HIGHT
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

    def elevators_factory(self):
        """
        Creates the elevators for the building and adds them to the sprite group.
        
        Args:
            elevators (int): The number of elevators to create.
        """
        for i in range(len(self.elevators)):
            x_position = self.x_position + flr.width + (i * elv.width)
            y_position = settings.SCREEN_HIGHT
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
       
        nearest_elevator = min(
            (elevator for elevator in self.elevators ), 
            key=lambda elevator: abs(elevator.floor - floor)/2 + elevator.moving()*2 + 0 if not elevator.move_to_floors else int(elevator.move_to_floors[-1]["arrival time"] + 2 ))
        
        # moving function is not correct
        return nearest_elevator

    def cold_to_elevator(self, floor):
        """
        Moves the nearest available elevator to the specified floor.
        
        Args:
            floor (int): The floor number to move the elevator to.
        
        Returns:
            bool: True if an elevator was moved, otherwise False.
        """
        nearest_elevator = self._find_nearest_elevator(floor)
        nearest_elevator.move_to_floor(floor)
        self.floors[floor].an_elevator_was_called(nearest_elevator.arrival_time)


    def update(self):
        """
        Updates the state of the building, moving elevators as needed.
        Processes any pending elevator calls.
        """
        for elv in self.elevators:
            elv.update()
            if not elv.moving() and self.floors[elv.floor].button.color == settings.BUTTON_COLOR_TEMPORARILY: # moving function is not correct
                self.floors[elv.floor].change_color(settings.BUTTON_COLOR)            

            if elv.update_location():
                floor = elv.floor
                self.floors[floor].update_time_elevator(elv.arrival_time)
            if elv.move_to_floors:
                for floor in elv.move_to_floors:
                    self.floors[floor["floor"]].update_time_elevator(floor["arrival time"])
