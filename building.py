import pygame as pg

from floor import Floor as flr
from elevator import Elevator as elv
from parting_line import PartingLine as p_line

SCREEN_SIZE = 1200, 900 #TODO import or other solution here. the size of the screen is defined in main.py file

class Building(pg.sprite.Group):
    difference_building = flr.width*2 + elv.width
    def __init__(self, floors, elevators, building_number=0):
        super().__init__()
        self.building_location_x, self.building_location_y = SCREEN_SIZE  # TODO Define a correct location
        self.building_location_x = 0

        self.floors = [None] * floors
        self.elevators = [None] * elevators
        self.building_number = building_number
        self.rect_x = 40 + building_number * (flr.width + 40) # TODO add elevators Distance from the beginning of the screen + distance from the last building
        self._build_building_floors()
        self.create_elevators(elevators)

    def _parting_line(self):
        #TODO: a good background image to be parting line between the floor.
        image = p_line(len(self.floors))
        return image
        
    def _build_building_floors(self):
        background = self._parting_line()
        # Change it to draw the floors over the background
        _, position_y = SCREEN_SIZE
        for i in range(len(self.floors)):
            self.floors[i] = flr(i, bottomleft=(0, position_y))
            self.add(self.floors[i])
            position_y -= flr.height + p_line.width

    def create_elevators(self, elevators):
        for i in range(elevators):
            x_position = self.building_location_x + flr.width + (i* elv.width)
            y_position = self.building_location_y
            elevator = elv(bottomleft=(x_position, y_position))
            self.add(elevator)
            self.elevators[i] = elevator