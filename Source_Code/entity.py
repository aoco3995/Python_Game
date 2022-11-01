import pygame

class entity(pygame.sprite.Sprite):
	def __init__(self,sprite_path,pos,velocity):
		super().__init__()
		self.image = pygame.image.load(sprite_path).convert_alpha()
		self.rect = self.image.get_rect(center = pos)
		self.pos = pos
		self.velocity = velocity
		self.x_on_field = 0
		self.y_on_field = 0

	def update(self,direction):
		self.rect.x += direction

	def get_object_rect(self):
		return self.rect

	def move_with_field(self, field,x,y):
		self.x_on_field += x
		self.y_on_field += y
		self.rect.x = field.get_object_rect().centerx + self.x_on_field
		self.rect.y = field.get_object_rect().bottom -self.y_on_field

	def get_velocity(self):
		return self.velocity

	def get_pos_on_field(self):
		return {"x": self.x_on_field, "y": self.y_on_field}

	def get_abs_pos(self, field):
		return((field.get_object_rect().centerx + self.x_on_field), (field.get_object_rect().bottom -self.y_on_field))