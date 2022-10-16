from turtle import screensize
import pygame
from entity import entity

class running_back(entity):
    def __init__(self, sprite_path, pos, velocity,screen_size):
        super().__init__(sprite_path, pos, velocity)
        self.screen_size = screen_size
        self.touchdown = False
    
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rect.x += self.velocity
        if keys[pygame.K_a]:
            self.rect.x -= self.velocity
        if keys[pygame.K_w]:
            self.rect.y -= self.velocity
        if keys[pygame.K_s]:
            self.rect.y += self.velocity

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.screen_size[0] - 200:
            self.rect.right = self.screen_size[0] - 200
        if self.rect.y < (1/10)*self.screen_size[0]:
            self.rect.y = (9/10)*self.screen_size[0]
            self.touchdown = True

    def update(self):
        self.get_input()
        self.constraint()
        #self.recharge()
        #self.lasers.update()