from turtle import screensize
import pygame
from entity import entity

class field(entity):
    def __init__(self,sprite_path,pos,velocity):
        super().__init__(sprite_path, pos, velocity)
        self.rect = self.image.get_rect(bottomleft = pos)

    def update(self, running_back):

        self.rect.y += self.velocity
        self.rect.y += self.velocity

        if self.rect.y < running_back.get_object_rect().y:
            #Running Back is to the Right
            if running_back.get_object_rect().x - self.rect.x > 2:
                if self.x_momentum < self.velocity:
                    self.x_momentum += 0.1

            #Running Back is to the Left
            elif running_back.get_object_rect().x - self.rect.x < -2:
                if (-1)*self.x_momentum < self.velocity:
                    self.x_momentum -= 0.1
    
        self.rect.x += self.x_momentum