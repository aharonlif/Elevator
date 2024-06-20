import pygame as pg

from settings import Floor


class Button(pg.sprite.Sprite):
    s = Floor.width/4
    size = (s, s)
    color = (255, 253, 208) 
    text_color = (0, 0, 0)

    def __init__(self, number):

        super().__init__()
        self.color = (255, 253, 208)  # Cream color
        pg.font.init()
        self.number = number
        self.font = pg.font.SysFont(None, 30)
        self.image = self.create_button_image()
        self.rect = self.image.get_rect()
        self.clicked = False

    def create_button_image(self):
        button_surface = pg.Surface(self.size, pg.SRCALPHA)
        pg.draw.circle(button_surface, self.color, (self.size[0] // 2, self.size[1] // 2), self.size[0] // 2)        
        text_surface = self.font.render(str(self.number), True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
        button_surface.blit(text_surface, text_rect)
        return button_surface

    def check_click(self, pos):
        is_clicked = self.rect.collidepoint(pos)
        return is_clicked

    # def change_color_temporarily(self):
    #     # Warning: it dos that the buttons will not arrive in secound time!
    #     # button_surface = pg.Surface(self.size, pg.SRCALPHA)
    #     self.color = (0,233, 0)
    #     self.image = self.create_button_image()
    #     self.rect = self.image.get_rect(center=self.rect.center)
        # self.color = (0, 255, 0)
        # self.image = self.create_button_image()
        # self.rect = self.image.get_rect()
        # pg.draw.circle(button_surface, self.color, (self.size[0] // 2, self.size[1] // 2), self.size[0] // 2)
        # pg.draw(self)
        # self.image = self.create_button_image()
        # self.rect = self.image.get_rect(center=self.rect.center)
        # print("change_color_temporarily() function cold", self.color)
        # pg.time.delay(2350)
        # self.color = Button.color
        # self.image = self.create_button_image()
        # self.rect = self.image.get_rect(center=self.rect.center)
        
    def change_color_temporarily(self, new_color, duration):
        self.color = new_color
        self.image = self.create_button_image()
        pg.time.set_timer(pg.USEREVENT + 1, duration * 1000)

    # def reset_color(self):
    #     self.color = self.original_color
    #     self.image = self.create_button_image()

