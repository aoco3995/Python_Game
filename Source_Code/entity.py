import pygame

class entity(pygame.sprite.Sprite):
	def __init__(self,sprite_path,pos,velocity):
		super().__init__()
		self.image = pygame.image.load(sprite_path).convert_alpha()
		self.rect = self.image.get_rect(center = pos)
		self.pos = pos
		self.velocity = velocity

	def update(self,direction):
		self.rect.x += direction

	def get_object_rect(self):
		return self.rect