import pygame as pg

import building


WIDTH_SCREEN, HIGHT_SCREEN = 1200, 900
pg.init()

screen = pg.display.set_mode((WIDTH_SCREEN, HIGHT_SCREEN))
pg.display.set_caption("Building Floor")


class Manager:
        
    def __init__(self) -> None:
        self.buildings = []
        self.build = building.Building(9, 3, WIDTH_SCREEN)
        self.buildings.append(self.build)
        self.group = self.build
        # self.g = building.Building(3, 4, 1)
        # self.group.add(self.g)

    def move_elevator(the_building, floor):
        the_elevator_arrived = False
        while not the_elevator_arrived:
            the_elevator_arrived = the_building.move_elevator(floor)
            # self.handle_event() #TODO: this

    def handle_event(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False 
                    self.handle_event(event)
                if event.type == pg.MOUSEBUTTONDOWN:
                    for build in self.buildings:
                        for floor in build.floors:
                            if floor.button.check_click(event.pos):
                                self.build.move_elevator(floor.floor_number)
            screen.fill((255, 255, 255)) 
            self.draw(screen)


        pg.display.flip()

    pg.quit()



    def draw(self, screen):
        self.group.draw(screen)



def main():
    manager = Manager()
    manager.handle_event()
       

if __name__ == "__main__":
    main()
