import pygame
from entity import entity
from running_back import running_back

class defender(entity):

    def update(self, running_back):

        self.rect.y += self.velocity
        if running_back.get_object_rect().x > self.rect.x:
            self.rect.x += self.velocity
        else:
            self.rect.x -= self.velocity