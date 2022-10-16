import pygame
from entity import entity

class bullet(entity):
	def __init__(self,sprite_path,pos,velocity,screen_size):
		super().__init__(sprite_path,pos,velocity)
		self.screen_size = screen_size

	def destroy(self):
		if self.rect.y <= -50 or self.rect.y >= self.screen_size[1] + 50: 
			self.kill()

	def update(self):
		self.rect.y += self.velocity
		self.destroy()		