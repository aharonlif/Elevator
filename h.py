import pygame as pg

class Button(pg.sprite.Sprite):
    size = (50, 50)
    text_color = (0, 0, 0)

    def __init__(self, number, position, color=(255, 253, 208)):
        super().__init__()
        self.color = color
        self.original_color = color
        self.number = number
        self.font = pg.font.SysFont(None, 30)
        self.image = self.create_button_image()
        self.rect = self.image.get_rect(topleft=position)

    def create_button_image(self):
        button_surface = pg.Surface(self.size, pg.SRCALPHA)
        pg.draw.circle(button_surface, self.color, (self.size[0] // 2, self.size[1] // 2), self.size[0] // 2)
        text_surface = self.font.render(str(self.number), True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
        button_surface.blit(text_surface, text_rect)
        return button_surface

    def check_click(self, pos):
        return self.rect.collidepoint(pos)

    def change_color_temporarily(self, new_color, duration=1):
        self.color = new_color
        self.image = self.create_button_image()
        pg.time.set_timer(pg.USEREVENT + self.number, int(duration * 1000))

    def reset_color(self):
        self.color = self.original_color
        self.image = self.create_button_image()

# Initialize Pygame and create the screen
pg.init()
screen = pg.display.set_mode((600, 400))

# Create four buttons and a sprite group
buttons = [
    Button(1, (50, 50)),
    Button(2, (150, 50)),
    Button(3, (250, 50)),
    Button(4, (350, 50))
]
all_sprites = pg.sprite.Group(buttons)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.check_click(event.pos):
                    button.change_color_temporarily((0, 255, 0), 1)  # Change to green for 1 second
        elif event.type >= pg.USEREVENT and event.type < pg.USEREVENT + len(buttons):
            button_index = event.type - pg.USEREVENT
            buttons[button_index].reset_color()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pg.display.flip()

pg.quit()
