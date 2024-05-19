import pygame as pg

import building
SCREEN_SIZE = 1200, 900

  

pg.init()

grp = building.Building(9, 1)


def main():

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
