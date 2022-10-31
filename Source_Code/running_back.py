from turtle import screensize
import pygame
from entity import entity

class running_back(entity):
    def __init__(self, sprite_path, pos, velocity,screen_size):
        super().__init__(sprite_path, pos, velocity)
        self.screen_size = screen_size
        self.touchdown = False
        self.move_x = 0
        self.move_y = 0
    
    def get_input(self,field):

        self.move_x =0
        self.move_y =0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.move_x = self.velocity
            if self.rect.x >= self.screen_size[0]:
                self.move_x = -self.velocity 

        if keys[pygame.K_a]:
            self.move_x = -self.velocity
            if self.rect.x <= 0:
                self.move_x = self.velocity
           
        if keys[pygame.K_w]:
            self.move_y = self.velocity
        if keys[pygame.K_s]:
            self.move_y = -self.velocity
        

        self.move_with_field(field,self.move_x,self.move_y)
  

    def constraint(self):
        pass
        # if self.rect.left <= 0:
        #     self.rect.left = 0
        # if self.rect.right >= self.screen_size[0] - 200:
        #     self.rect.right = self.screen_size[0] - 200
        # if self.rect.y < (1/10)*self.screen_size[0]:
        #     pass
        #     # self.rect.y = (9/10)*self.screen_size[0]
        #     # self.touchdown = True

    def update(self,field):
        self.get_input(field)
        self.constraint()
        #self.recharge()
        #self.lasers.update()
        #testing 