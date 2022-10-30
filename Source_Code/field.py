from turtle import screensize
import pygame
from entity import entity

class field(entity):
    def __init__(self,sprite_path,pos,velocity):
        super().__init__(sprite_path, pos, velocity)
        self.rect = self.image.get_rect(bottomleft = pos)

    def update(self):
        pass