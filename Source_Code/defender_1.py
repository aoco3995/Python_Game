import pygame
from entity import entity
from running_back import running_back
from random import *

class defender(entity):

    def __init__(self,sprite_path,pos,velocity,screen_size,field,running_back):
        super().__init__(sprite_path, pos, velocity)
        self.x_momentum = 0
        self.y_momentum = 0
        self.x_on_field = randint(-field.get_object_rect().w/2, field.get_object_rect().w/2)
        self.y_on_field = running_back.get_pos_on_field()["y"]+ screen_size[1]*(7/10)

    def update(self, running_back, field):

        #self.rect.y += self.velocity
        #self.rect.y += self.velocity

        #Running Back is above
        if running_back.get_pos_on_field()["y"] - self.y_on_field > 2:
            if self.y_momentum < self.velocity:
                self.y_momentum += 0.1
        #Running Back is below
        if running_back.get_pos_on_field()["y"] - self.y_on_field < -2:
            if (-1)*self.y_momentum < self.velocity:
                self.y_momentum -= 0.1
        #Running Back is to the Right
        if running_back.get_pos_on_field()["x"] - self.x_on_field > 2:
            if self.x_momentum < self.velocity:
                self.x_momentum += 0.1

        #Running Back is to the Left
        elif running_back.get_pos_on_field()["x"] - self.x_on_field < -2:
            if (-1)*self.x_momentum < self.velocity:
                self.x_momentum -= 0.1
    
        self.move_with_field(field,self.x_momentum,self.y_momentum * 1.5)
        # self.rect.x += self.x_momentum
        # self.rect.y += self.y_momentum * 1.5
