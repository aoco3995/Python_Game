from turtle import screensize
import pygame
from entity import entity

class field(entity):
    def __init__(self,sprite_path,pos,velocity):
        super().__init__(sprite_path, pos, velocity)
        self.rect = self.image.get_rect(bottomleft = pos)

    def update(self,running_back,screen_size):
        
        if running_back.get_object_rect().y < screen_size[0]/2:
            self.rect.y += running_back.get_velocity()
        elif running_back.get_object_rect().y > screen_size[0]*(6/10):
            if self.rect.y > screen_size[0] - self.rect.h:
                self.rect.y -= running_back.get_velocity()