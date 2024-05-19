import pygame as pg
import time
    
class Elevator(pg.sprite.Sprite):
    width, height = 80, 80
    def __init__(self, bottomleft):
        super().__init__()
        self.image = pg.image.load("help_files/elv.png")
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        # self.location = bottomleft
        self.rect = self.image.get_rect(bottomleft=bottomleft)
        self.floor = 0
        self.motion = False

    def move(self, rect, floor, end=False):
        self.motion = floor
        self.rect = rect
        if end:
            motion = False
        


# import time

# class Elevator(pg.sprite.Sprite):
#     def __init__(self, floors):
#         super().__init__()
#         self.current_floor = 0  # Assume elevator starts at floor 0
#         self.floors = floors

#     def move_to_floor(self, target_floor):
#         # Move the elevator to the target floor
#         if target_floor > self.current_floor:
#             direction = 1  # Move up
#         elif target_floor < self.current_floor:
#             direction = -1  # Move down
#         else:
#             return  # Already at the target floor

#         # Move the elevator to each floor sequentially with a delay
#         while self.current_floor != target_floor:
#             self.current_floor += direction
#             print(f"Moving elevator to floor {self.current_floor}")
#             time.sleep(0.5)  # Delay for half a second between each floor

#         print("Elevator reached destination floor.")

# # Usage example:
# elevator = Elevator(10)  # Assume 10 floors
# target_floor = 5  # Target floor to move the elevator to
# elevator.move_to_floor(target_floor)



