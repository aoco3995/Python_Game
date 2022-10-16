import pygame
from entity import entity
from running_back import running_back

class defender(entity):

    def __init__(self,sprite_path,pos,velocity):
        super().__init__(sprite_path, pos, velocity)
        self.x_momentum = 0

    def update(self, running_back):

        self.rect.y += self.velocity
        self.rect.y += self.velocity

        #Running Back is to the Right
        if running_back.get_object_rect().x - self.rect.x > 2:
            if self.x_momentum < self.velocity:
                self.x_momentum += self.velocity/10

        #Running Back is to the Left
        elif running_back.get_object_rect().x - self.rect.x < -2:
            if (-1)*self.x_momentum < self.velocity:
                self.x_momentum -= self.velocity/10
    
        self.rect.x += self.x_momentum
