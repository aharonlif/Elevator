import pygame as pg

class Button(pg.sprite.Sprite):
    size = (50, 50)
    b_color = (255, 253, 208)  # Cream color
    text_color = (0, 0, 0)

    def __init__(self, number):
        super().__init__()
        self.number = number
        self.font = pg.font.SysFont(None, 30)
        self.image = self.create_button_image()
        self.rect = self.image.get_rect()
        self.clicked = False

    def create_button_image(self):
        button_surface = pg.Surface(self.size, pg.SRCALPHA)
        pg.draw.circle(button_surface, self.b_color, (self.size[0] // 2, self.size[1] // 2), self.size[0] // 2)        
        text_surface = self.font.render(str(self.number), True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
        button_surface.blit(text_surface, text_rect)
        
        return button_surface

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.clicked = True
            return True
        return False

class Line(pg.sprite.Sprite):
    def __init__(self, start_pos, end_pos, color=(0, 0, 0), width=3):
        super().__init__()
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = color
        self.width = width

        min_x = min(start_pos[0], end_pos[0])
        min_y = min(start_pos[1], end_pos[1])
        max_x = max(start_pos[0], end_pos[0])
        max_y = max(start_pos[1], end_pos[1])

        self.image = pg.Surface((max_x - min_x, max_y - min_y), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = (min_x, min_y)

        adjusted_start_pos = (start_pos[0] - min_x, start_pos[1] - min_y)
        adjusted_end_pos = (end_pos[0] - min_x, end_pos[1] - min_y)

        pg.draw.line(self.image, self.color, adjusted_start_pos, adjusted_end_pos, self.width)

class Floor(pg.sprite.Sprite):
    width, height = 150, 80
    def __init__(self, floor_number, bottomleft):
        super().__init__()

        self.image = pg.image.load("help_files/floor_image.png")
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(bottomleft=bottomleft)
        self.floor_number = floor_number
        self.draw_button()
      
    def draw_button(self):
        button = Button(self.floor_number)
        self.image.blit(button.image, button.rect.center)

