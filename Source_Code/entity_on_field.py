import pygame
from entity import entity

class entity_on_field(entity):
    def __init__(self, sprite_path, pos, velocity):
        super().__init__(sprite_path, pos, velocity)
        self.pos_on_field = pos

    def move_x_on_field(self,x,field):
        self.pos_on_field[0] += x
        self.rect.x = field.get_object_rect().x + self.pos_on_field[0]


