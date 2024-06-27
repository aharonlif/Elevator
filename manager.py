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

    def __init__(self, buildings) -> None:
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
        self.buildings = [None] * len(settings.BUILDINGS)
        self.group = pg.sprite.Group()
        self.factory_of_buildings()

    def factory_of_buildings(self):
        """
        Creates and initializes buildings with the given number of floors and elevators.
        
        Args:
            floors (int): Number of floors per building.
            elevators (int): Number of elevators per building.
        """
        for i, build in enumerate(settings.BUILDINGS):
            if i == 0:
                x_position = 0
            else:
                x_position = self.buildings[i-1].x_position + settings.FLOOR_WIDTH + settings.FLOOR_HIGHT * (settings.BUILDINGS[i-1]["elevators"])
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
                    if not any(floor.floor_number == elev.floor or any(floor.floor_number == d.get("floor") for d in elev.move_to_floors) for elev in build.elevators):
                        build.cold_to_elevator(floor.floor_number)
                    return

    def update(self):
        """
        Updates the state of all buildings.
        """
        for build in self.buildings:
            build.update()

    def draw(self):
        """
        Draws all sprites to the screen.
        
        Args:
            screen (pygame.Surface): The display surface.
        """
        self.group.draw(self.screen)