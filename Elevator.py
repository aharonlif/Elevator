import pygame as pg

# Initialize Pygame
pg.init()

# Set up the display
width, height = 800, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Building Background")

# Define colors
BLACK = (0, 0, 0)

# Create a surface for the black background
background_surface = pg.Surface((width, height))
background_surface.fill(BLACK)

# Load building image
building_image = pg.image.load("building_image.png")  # Replace "building_image.png" with your actual image file

# Blit building image onto the background
building_rect = building_image.get_rect(center=(width // 2, height // 2))
background_surface.blit(building_image, building_rect)

# Main loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.blit(background_surface, (0, 0))  # Blit the background onto the screen

    pg.display.flip()

# Quit Pygame
pg.quit()
