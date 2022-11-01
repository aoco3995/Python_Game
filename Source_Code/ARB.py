import pygame

from entity import entity
from running_back import running_back

class ARB(entity):
	def __init__(self, sprite_path, pos, velocity,screen_size):
		super().__init__(sprite_path, pos, velocity)

		self.screen_size = screen_size
		 #animation vars

		self.animation_step = 0
		self.animation_action = 0 #temp
		self.last_update = pygame.time.get_ticks()
		self.animation_cooldown = 40
		


	def get_input(self):
		self.keys = pygame.key.get_pressed()
		if self.keys[pygame.K_a]:
			self.animation_action = 0
		if self.keys[pygame.K_s]:
			self.animation_action = 6
		if self.keys[pygame.K_d]:
			self.animation_action = 4
		if self.keys[pygame.K_w]:
			self.animation_action = 2
		if self.keys[pygame.K_w] and self.keys[pygame.K_a]:
			self.animation_action = 1
		if self.keys[pygame.K_w] and self.keys[pygame.K_d]:
			self.animation_action = 3
		if self.keys[pygame.K_s] and self.keys[pygame.K_a]:
			self.animation_action = 7
		if self.keys[pygame.K_s] and self.keys[pygame.K_d]:
			self.animation_action = 5

	def animation(self,field, screen, running_back):
		current_time = pygame.time.get_ticks()
		screen.blit(self.image, running_back.get_abs_pos(field), ((112.5*self.animation_step),(112.5*self.animation_action),(112.5),(112.5)))
		if current_time - self.last_update >= self.animation_cooldown:
			
			if self.animation_step < 7:
				self.animation_step += 1
			else:
				self.animation_step = 0
			self.last_update = pygame.time.get_ticks()

	def update(self, field, screen, running_back):
		self.get_input()
		self.animation(field, screen, running_back)