import pygame
from entity import entity

class running_back(entity):
    
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
    
    def update(self):
        self.get_input()
        #self.constraint()
        #self.recharge()
        #self.lasers.update()