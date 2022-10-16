import pygame
from entity import entity
from running_back import running_back

class defender(entity):

    def update(self, running_back):

        self.rect.y += self.velocity
        self.rect.y += self.velocity
        if running_back.get_object_rect().x - self.rect.x > 2:
            self.rect.x += self.velocity
        elif running_back.get_object_rect().x - self.rect.x < -2:
            self.rect.x -= self.velocity
