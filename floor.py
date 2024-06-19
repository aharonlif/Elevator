import pygame as pg


class Line(pg.sprite.Sprite):
    color = (0, 0, 0)
    width = 7
    def __init__(self, start_pos, end_pos):
        super().__init__()
        self.start_pos = start_pos[0]
        self.end_pos = end_pos[0]

        min_x = start_pos[0]#, end_pos[0])
        min_y =start_pos[1]#, end_pos[1])
        max_x = end_pos[0]
        max_y =  end_pos[1]
        self.image = pg.Surface((max_x - min_x + self.width, max_y - min_y + self.width), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = (min_x, min_y)

        adjusted_start_pos = (start_pos[0] - min_x, start_pos[1] - min_y)
        adjusted_end_pos = (end_pos[0] - min_x, end_pos[1] - min_y)
        pg.draw.line(self.image, self.color, start_pos, end_pos, self.width)


class Floor(pg.sprite.Sprite):
    width, height = 150, 80
    def __init__(self, floor_number, bottomleft):
        super().__init__()
        self.image = pg.image.load("help_files/floor_image.png")
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(bottomleft=bottomleft)
        self.floor_number = floor_number
        self.button = Button(self.floor_number)
        self.button.rect.center = self.rect.center  # Add this line to set the button's position relative to the floor

        self.draw_button()
      
    def draw_button(self):
        button_size = self.button.size[0] # Height = width
        center_floor = self.width/2 - button_size/2, self.height/2 - button_size/2
        self.image.blit(self.button.image, center_floor)

class Button(pg.sprite.Sprite):
    s = Floor.width/4
    size = (s, s)
    b_color = (255, 253, 208)  # Cream color
    text_color = (0, 0, 0)

    def __init__(self, number):
        super().__init__()
        pg.font.init()
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
        is_clicked = self.rect.collidepoint(pos)
        return is_clicked
