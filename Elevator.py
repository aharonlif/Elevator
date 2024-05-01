import help_file as hf
import pygame as pg
from IPython.display import display, Image

class Elevator(pg.sprite.Sprite):
        
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('elv.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def position_x(self):
        return self.rect.x
    def position_y(self):
        return self.rect.y
    def move(self, new_location):
        # TODO: need to check if the elevator moved or needs to refresh its.
        self.rect = new_location

class Floor:
    def __init__(self, file_name, size, location):
        self.file_name = file_name
        self.size = size
        self.location = location
    def left_location(self, location):
        return self.location[0]
    def right_location(self, location):
        return self.location[0] + self.size
    def up_location(self, location):
        return self.location[1]
    def down_location(self, location):
        return self.location[1] - self.size

class Line:
    def __init__(self):
        self.line_width = 5
        self.width_building = 3 # Define the width
    def draw(self, screen, location):
        x, y = location[0], location[1]
        pg.draw.line(screen, Black, [x, y], [x+self.width_building, y+self.width_building], self.line_width)
        pass
    """Have a built-in function
    def left_location(self, location):
        return self.location[0]
    def right_location(self, location):
        return self.location[0] + self.size
    def up_location(self, location):
        return self.location[1]
    def down_location(self, location):
        return self.location[1] - self.size"""

class Building:
    def __init__(self, floors, location):
        self.floors = floors
        """#delete...: size of building, and resize when added a new building
        # self.length = length
        # self.width = width"""
        self.location = location
        self.elevators = []
    def find_elevator(self, location):
        the_nearest_elevator = min(abs(i - location) for i in self.elevators)
        return the_nearest_elevator
    def move_elevator(self, floor):
        #TODO: this
        self.elevator_location = floor

class Management:
    def __init__(self, building):
        self.buildings = [building]
        self.event = None
    def find_elevator(self, building, floor):
        while not building.find_elevator(floor):
            self.checker_change_building(building)
        building.move_elevator(floor)
    def add_building(self, building):
        #TODO: add new building
        self.buildings.append(building)
    def change_building(self):
        #TODO this
        pass
    def checker_change_building(self):
        pass
        # if self.event == "Change Building":
        #     self.change_building()

def pg_run():
    WIDTH = 1700
    HEIGHT = 1300
    REFRESH_RATE = 60
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    #TODO  "Press floor" button, and drawing of an arrow button.
    pg.display.set_caption("buildings with a elevator")
    screen.fill((255, 255, 200))
    pg.display.flip()

    # for i in range(3):
    #     elv{f"i"} = Elevator(0,0)

    
    elv = Elevator(0,i*10)
    clock = pg.time.Clock()

    # all_sprites = pg.sprite.Group()
    # all_sprites.add(elv)
    # all_sprites.draw(screen)

    screen.blit(elv.image, (220,320))
    clock.tick(REFRESH_RATE)
    finish = False
    while not finish:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finish = True
    pg.quit()

pg_run()