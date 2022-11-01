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
		self.animation_cooldown = 60

	def animation(self,field, screen, running_back):
		current_time = pygame.time.get_ticks()
		if current_time - self.last_update >= self.animation_cooldown:
			screen.blit(self.image, running_back.get_abs_pos(field), ((112.5*self.animation_step),(0),(112.5+112.5*self.animation_step),(112.5)))
			if self.animation_step < 7:
				self.animation_step += 1
			else:
				self.animation_step = 0
			self.last_update = pygame.time.get_ticks()

	def update(self, field, screen, running_back):
		self.animation(field, screen, running_back)