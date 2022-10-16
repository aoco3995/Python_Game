from turtle import screensize
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
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocity

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
<<<<<<< HEAD
        if self.rect.right >= self.screen_size[0] - 310:
            self.rect.right = self.screen_size[0] - 310
=======
        if self.rect.right >= self.screen_size[0] - 200:
            self.rect.right = self.screen_size[0] - 200
        if self.rect.y < (1/10)*self.screen_size[0]:
            self.rect.y = (9/10)*self.screen_size[0]
>>>>>>> e6f8290a8db731d2c5f9ef3f145e419ed33833ae
    
    def update(self):
        self.get_input()
        self.constraint()
        #self.recharge()
        #self.lasers.update()