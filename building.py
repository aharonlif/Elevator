import pygame as pg

from floor import Floor as flr
from floor import Line as line
from elevator import Elevator as elv

SCREEN_SIZE = 1200, 900 

class Building(pg.sprite.Group):
    difference_building = flr.width*2 + elv.width

    def __init__(self, floors, elevators, y_location, building_number=0):
        super().__init__()
        self.floors = [None] * floors
        self.elevators = [None] * elevators
        self.building_location_x = 0
        self.building_location_y = y_location
        self.building_number = building_number
        self._build_building_floors()
        self.create_elevators(elevators)

        
    def _build_building_floors(self):
        _, position_y = SCREEN_SIZE
        for i in range(len(self.floors)):
            self.floors[i] = flr(i, bottomleft=(0, position_y))
            self.add(self.floors[i])

            if i < len(self.floors) - 1:

                start_pos = self.floors[i].rect.midbottom
                end_pos = (self.floors[i].rect.midbottom[0], self.floors[i].rect.midbottom[1] + flr.height + line.width)
                new_line = line(start_pos, end_pos)
                self.add(new_line)

            position_y -= flr.height + line.width

    def create_elevators(self, elevators):
        for i in range(elevators):
            x_position = self.building_location_x + flr.width + (i* elv.width)
            y_position = self.building_location_y
            elevator = elv(bottomleft=(x_position, y_position))
            self.add(elevator)
            self.elevators[i] = elevator

    def _find_nearest_elevator(self, floor):
        nearest_elevator = min((elevator for elevator in self.elevators if not elevator.motion), key=lambda elevator: abs(elevator.floor - floor))
        return nearest_elevator
    
    def move_elevator(self, floor):
        """Find the nearest elevator to the floor and send to the elevator to move.
        """

        nearest_elevator = self._find_nearest_elevator(floor)
        if not nearest_elevator:
            #TODO: cold to elevator when it doesn not exist
            pass 
        else:
            nearest_elevator.move(floor)


