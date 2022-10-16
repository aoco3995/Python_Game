import pygame
from entity import entity

class running_back(entity):
    def __init__(self, sprite_path, pos, velocity,screen_size):
        super().__init__(sprite_path, pos, velocity)
        self.screen_size = screen_size
    
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        elif keys[pygame.K_UP]:
            self.rect.y -= self.velocity
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.velocity

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.screen_size[0] - 200:
            self.rect.right = self.screen_size[0] - 200
    
    def update(self):
        self.get_input()
        self.constraint()
        #self.recharge()
        #self.lasers.update()