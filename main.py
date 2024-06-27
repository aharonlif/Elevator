import pygame as pg

from manager import Manager
import settings


def main():
    """
    Main game loop. Handles events, updates the screen, and redraws all elements of manager class.
        """
    manager = Manager(settings.BUILDINGS)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False 
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                manager.check_floor_click(event.pos)

        manager.screen.fill((255, 255, 255)) 
        manager.update()
        manager.draw()
        pg.display.flip()
    pg.quit()

    

if __name__ == "__main__":
    """
    Entry point for the program. Calls the main function.
    """
    main()