import pygame as pg

class Button(pg.sprite.Sprite):
    size = (50, 50)
    b_color = (255, 255, 255)
    text_color = (0, 0, 0)

    def __init__(self, number):
        super().__init__()
        self.number = number
        self.font = pg.font.SysFont(None, 30)
        self.image = self.create_button_image()
        self.rect = self.image.get_rect()

    def create_button_image(self):
        button_surface = pg.Surface(self.size)
        button_surface.fill(self.b_color)
        text_surface = self.font.render(str(self.number), True, self.text_color)
        text_rect = text_surface.get_rect(center=button_surface.get_rect().center)
        button_surface.blit(text_surface, text_rect)
        return button_surface

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

