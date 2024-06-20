import pygame as pg

from floor import Floor as flr
from floor import Line as line
from elevator import Elevator as elv


class BlackRectangle(pg.sprite.Sprite):
    def __init__(self, start_pos, end_pos):
        super().__init__()
        x1, y1 = start_pos
        x2, y2 = end_pos
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        
        self.image = pg.Surface((width, height))
        self.image.fill((0, 0, 0))  # Fill the surface with black color
        self.rect = self.image.get_rect()

        self.rect.topleft = (min(x1, x2), min(y1, y2)) #top left or anysing instead

class Building(pg.sprite.Group):
    difference_building = flr.width*2 + elv.width

    def __init__(self, y_screen, floors: int, elevators: int, building_number=0):
        super().__init__()
        self.floors = [None] * floors
        self.elevators = [None] * elevators
        self.building_position_x = 0
        self.y_screen = y_screen
        self.building_number = building_number
        self.floors_factory()
        self.elevators_factory(elevators)

        
    def floors_factory(self):
        y_position = self.y_screen
        for i in range(len(self.floors)):
            self.floors[i] = flr(i, bottomleft=(0, y_position))
            self.add(self.floors[i])
            y_position -= flr.height + line.thickness

            # if i < len(self.floors):
            #     start_pos = self.floors[i].rect.midbottom
            #     end_pos = (self.floors[i].rect.midbottom[0], self.floors[i].rect.midbottom[1] + flr.height + line.width)
            #     print("st, end        =", start_pos, end_pos)
            #     new_line = line(start_pos, end_pos)
            #     self.add(new_line)
        # s = BlackRectangle(self.floors[0].rect, self.floors[-1].rect)

    def elevators_factory(self, elevators):
        for i in range(elevators):
            x_position = self.building_position_x + flr.width + (i* elv.width)
            y_position = self.y_screen
            elevator = elv(bottomleft=(x_position, y_position))
            self.add(elevator)
            self.elevators[i] = elevator

    def _find_nearest_elevator(self, floor):
        nearest_elevator = min((elevator for elevator in self.elevators if not (elevator.moving() and elevator.floor != floor)), key=lambda elevator: abs(elevator.floor - floor))
        return nearest_elevator if nearest_elevator.floor != floor else None
    
    def move_elevator(self, floor):
        # correct_floor = self.floors[floor]
        nearest_elevator = self._find_nearest_elevator(floor) #TODO: list of cold elevators if have not elv
        if nearest_elevator:
            nearest_elevator.move_to_floor(floor)



    def update_elevators_location(self):
        "run of all elevators and if floor != floor now - update."
        for elv in self.elevators:
            elv.update_location()        