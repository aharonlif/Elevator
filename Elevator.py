import pygame as pg
import sys

import floor

#f = floor.p
def p():
    print(9)
#print(f.pr())

# class ColorDraw:
#     black = (0, 0, 0)
#     red = (0, 0, 0)
#     white = (255, 255, 255)
class Building(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, floors):
        super().__init__()
        self.image = pg.Surface((width, height))
        # self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.walls = []
        self.floors = floors
        # Add black walls to the building
        for floor in self.floors:
            #new_floor = floor.Floor(floor)
            #pg.draw.new_floor(self.image, (0, 0, 0), (x, y), (x, y), 2)
            pass
        self._add_walls()


    def _add_walls(self):
        top = self.rect
        line_width = 4
        #pg.draw.line(self.image, (0, 0, 0), top, line_width)
class BuildingFloor:
    def __init__(self, width, height, color, building_line):
        self.width = width
        self.height = height
        self.color = color
        self.buildings = []
        self.building_line = building_line

    def add_building(self, building):
        self.buildings.append(building)

    def draw(self, surface):
        pg.draw.rect(surface, self.color, (0, surface.get_height() - self.height, self.width, self.height))
        # for building in self.buildings:
        #     building.draw(surface)


def main():
    p()
    pg.init()

    # Set up the display
    width, height = 800, 600
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Single Building Floor")

    # Define the building line
    building_line = [(100, 300), (300, 400), (600, 200)]

    # Create a building floor object
    building_floor = BuildingFloor(width, 500, (100, 100, 100), building_line)

    # Generate buildings based on the building line
    for i in range(len(building_line) - 1):
        x1, y1 = building_line[i]
        x2, y2 = building_line[i + 1]
        building_width = x2 - x1
        building_height = y1
        building = Building(x1, 0, building_width, building_height, (200, 200, 200))
        building_floor.add_building(building)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Fill the screen with white color

        # Draw the building floor
        building_floor.draw(screen)

        pg.display.flip()

    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
