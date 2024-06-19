import pygame as pg

import building


WIDTH_SCREEN, HIGHT_SCREEN = 1200, 600 #Screen size need to be in setting file

class Manager:
    
    def __init__(self, buildings=1, floors=5, elv=3) -> None:
        pg.init()
        self.screen = pg.display.set_mode((WIDTH_SCREEN, HIGHT_SCREEN), pg.SRCALPHA)

        pg.display.set_caption("Building Floor")

        self.buildings = []
        self.group = self.factory_of_buildings(buildings, floors, elv)
        # self.g = building.Building(3, 4, 1)
        # self.group.add(self.g)

    def factory_of_buildings(self, buildings, floors, elv):
        #TODO: for i in buildings.
        build = building.Building(HIGHT_SCREEN, floors, elv, WIDTH_SCREEN)
        self.buildings.append(build)
        return build #TODO: return all buildings

    def check_floor_click(self, mouse_pos):
        for build in self.buildings:
            for floor in build.floors:
                if floor.button.check_click(mouse_pos):
                    build.move_elevator(floor.floor_number)


    def run(self):

        
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False 
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        running = False
                        # self.handle_event(event)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.check_floor_click(event.pos) #TODO: need to declare befor asciment
                self.screen.fill((255, 255, 255)) 
            self.draw(self.screen)


            pg.display.flip()

    pg.quit()



    def draw(self, screen):
        self.group.draw(screen)
