import help_file as hf
import pygame as pg
from IPython.display import display, Image

class Elevator(pg.sprite.Sprite):
        
    def __init__(self, location):
        super().__init__()
        self.evl_img = pg.image.load('elv.png')
        #TODO  understand what this doing here
        self.size = 20
        # self.rect = self.image.get_rect()
#----------------------------------------------------------------
        self.location = location
        #TODO: a good scalar value
        self.scaled_image = (20, 20)
        self.resize()
        
    def resize(self, size=20):
        #TODO: Resize must to do that the size declared from a new variable Number of buildings
        new_location = (
                int(self.evl_img.get_width() * self.size),
                  int(self.evl_img.get_height() * self.size)
            )
        self.scaled_image = pg.transform.scale (
            self.evl_img, new_location)

    def location(self):
        return self.location
    def move(self, new_location):
        # TODO: need to move Evelator to the new location
        self.location = new_location

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
    def __init__(self, type, size, location):
        self.type = type # TODO: need to convert
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

class Building:
    def __init__(self, floors, location):
        self.floors = floors
        #TODO: size of building, and resize when added a new building
        # self.length = length
        # self.width = width
        self.location = location
        self.elevators = []
    def add_floor(self):
        #TODO: this
        pass
    def number_of_elevators(self):
        return len(self.elevators)
    def the_nearest_elevator(self, location):
        the_nearest_elevator = min(abs(i - location) for i in self.elevators)
        return the_nearest_elevator

    def move_elevator(self, floor):
        #TODO: this
        self.elevator_location = floor

class Management:
    def __init__(self, building):
        self.buildings = [building]
    def add_building(self, building):
        #TODO: add new building
        self.buildings.append(building)
    def move_elevator(self, building, floor):
        building.move_elevator(floor)

WIDTH = 720
HEIGHT = 721
  
def pg_run():
    print("Running")
    clock = pg.time.Clock()
    clock.tick(5)
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    screen.fill((255, 255, 200))
    #TODO  this in a caption and change it to "buildings with a elevator"
    pg.display.set_caption("Press in the specified floor to move the elevator")

    elv = Elevator((0,0))
    width, height = elv.get_size()
    scaled_image = pg.transform.scale(elv, (int(width * 20), int(height * 20)))
    # pygame.quit()


    # resize_image(input_image, output_image, 0.5)




    screen.blit(elv, (220,320))
    pg.display.flip()
    REFRESH_RATE = 60
    clock.tick(REFRESH_RATE)

    # clock = pg.time.Clock()
    finish = False
    while not finish:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finish = True

pg_run()