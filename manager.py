import pygame as pg

import building
import settings

class Manager:
    """
    Manages the game, including the screen setup, building initialization, 
    event handling, and game loop.

    Attributes:
        screen (pygame.Surface): The display surface.
        buildings (list): List of building instances.
        group (pygame.sprite.Group): Group of all sprites.
    """

    def __init__(self, buildings=1, floors=5, elevators=3) -> None:
        """
        Initializes the Manager with the given number of buildings, floors, and elevators.
        
        Args:
            buildings (int): Number of buildings.
            floors (int): Number of floors per building.
            elevators (int): Number of elevators per building.
        """
        pg.init()
        self.screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HIGHT), pg.SRCALPHA)
        pg.display.set_caption("Building Floor")
        self.buildings = [None] * len(buildings)
        self.group = pg.sprite.Group()
        self.factory_of_buildings(buildings)

    def factory_of_buildings(self, buildings):
        """
        Creates and initializes buildings with the given number of floors and elevators.
        
        Args:
            floors (int): Number of floors per building.
            elevators (int): Number of elevators per building.
        """
        for i, build in enumerate(buildings):
            if i == 0:
                x_position = 0
            else:
                x_position = self.buildings[i-1].x_position + settings.FLOOR_WIDTH + settings.FLOOR_HIGHT * (buildings[i-1]["elevators"])
            current_building = building.Building(build, x_position)
            self.buildings[i] = current_building
            self.group.add(current_building)

    def check_floor_click(self, mouse_pos):
        """
        Checks if a floor button is clicked and moves the elevator to the respective floor.
        
        Args:
            mouse_pos (tuple): The position of the mouse click.
        """
        for build in self.buildings:
            for floor in build.floors:
                if floor.button.check_click(mouse_pos):
                    # TODO
                    build.move_elevator(floor.floor_number)
                    return

    def update(self):
        """
        Updates the state of all buildings.
        """
        # TODO
        for build in self.buildings:
            build.update()

    def run(self):
        """
        Main game loop. Handles events, updates the screen, and redraws all elements.
        """
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False 
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        running = False
                    if event.key == pg.K_a:
                        print("   in manager: if evenet.key == pg.k_a:                self.buildings[0].floors[0].change_color_temporarily()")
                        self.buildings[0].floors[0].change_color_temporarily()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    self.check_floor_click(event.pos)
                # elif event.type == pg.USEREVENT + 1:
                #     button.reset_color()
            self.screen.fill((255, 255, 255)) 
            self.update()
            self.draw()
            pg.display.flip()
        pg.quit()

    def draw(self):
        """
        Draws all sprites to the screen.
        
        Args:
            screen (pygame.Surface): The display surface.
        """
        self.group.draw(self.screen)