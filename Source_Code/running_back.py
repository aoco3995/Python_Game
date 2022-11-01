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

        #animation vars
        self.animation_step = 0
        self.animation_action = 0 #temp
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 60
    
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
    
    def touchdown_check(self, field):
        if self.y_on_field > (field.get_object_rect().h*(9/10)):
            self.reset_field(field)
            self.y_on_field = 5
            self.touchdown = True


    def reset_field(self,field):
        field.rect.y = self.screen_size[1]-field.get_object_rect().h 

    def animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.image.blit(self.image, (50,50), ((112*self.animation_step),(0),(112+112*self.animation_step),(112)))
            self.image.fill(0,0,0)
            if self.animation_step < 7:
                self.animation_step += 1
            else:
                self.animation_step = 0
            self.last_update = pygame.time.get_ticks()

    def update(self,field):
        self.get_input(field)
        self.constraint()
        self.touchdown_check(field)
        self.animation()
        
