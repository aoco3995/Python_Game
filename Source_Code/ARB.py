import pygame

class ARB(pygame.sprite.Sprite):
	def __init__(self):
		 #animation vars
		self.animation_step = 0
		self.animation_action = 0 #temp
		self.last_update = pygame.time.get_ticks()
		self.animation_cooldown = 60
	def animation(self):
		current_time = pygame.time.get_ticks()
		if current_time - self.last_update >= self.animation_cooldown:
			self.image.blit(self.image, (50,50), ((112.5*self.animation_step),(0),(112.5+112.5*self.animation_step),(112.5)))
			if self.animation_step < 7:
				self.animation_step += 1
			else:
				self.animation_step = 0
			self.last_update = pygame.time.get_ticks()