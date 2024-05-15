import pygame as pg

import floor as floor_file
# import Elevator

SCREEN_SIZE = 1200, 900

class Building(pg.sprite.Group):
    difference_building = floor_file.Floor.width*2 + floor_file.Elevator.width
    
    def __init__(self, floors, building_number=0):
        super().__init__()
        self.floors = floors
        self.building_number = building_number
        self.rect_x = 40 + building_number * (floor_file.Floor.width + 40) # Distance from the beginning of the screen + distance from the last building
        self._build_building_floors(floors=floors)
    

    def _build_building_floors(self, floors):
        for i in range(floors):
            _, position_y = SCREEN_SIZE
            position_y -= 50 # difference from the floor
            position_y -= i * (floor_file.Floor.height + 4)#line width. need to add hight above building.
            new_floor = f"floor_{i}"
            locals()[new_floor] = floor_file.Floor(i, bottomleft=(200, position_y))
            self.add(locals()[new_floor])

    def boundary_line(self, start, end, y_position):
        d = floor_file.Elevator()



    # def _draw_walls(self):
    #     top = self.rect
    #     line_width = 4
    #     #pg.draw.line(self.image, (0, 0, 0), top, line_width)


grp = Building(9)


def main():
    pg.init()

    width, height = SCREEN_SIZE
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Single Building Floor")

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((255, 255, 255)) 
        grp.draw(screen)


        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()
