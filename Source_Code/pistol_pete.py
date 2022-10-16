import pygame
from entity import entity
from bullet import bullet

class pistol_pete(entity):
    def __init__(self, sprite_path, pos, velocity, screen_size, screen):
        super().__init__(sprite_path, pos, velocity)
        self.bullet_time = 0
        self.bullet_rpm = 600
        self.screen_size = screen_size
        self.ready = True
        self.screen = screen
        

        self.bullet = pygame.sprite.Group()

        self.bullet_sound = pygame.mixer.Sound('../Audio/pistol.wav')
        self.bullet_sound.set_volume(0.5)


    def get_input(self):
        keys = pygame.key.get_pressed()
        self.mouse_crt_x , self.mouse_crt_y = pygame.mouse.get_pos()
        if self.mouse_crt_x >= self.rect.x + 50:#keys[pygame.K_d]:
            self.rect.x += self.velocity
        elif self.mouse_crt_x <= self.rect.x - 50:#keys[pygame.K_a]:
            self.rect.x -= self.velocity

        if keys[pygame.K_SPACE] and self.ready:
            self.fire_bullet()
            self.ready = False
            self.bullet_time = pygame.time.get_ticks()
            self.bullet_sound.play()

    def firerate(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.bullet_time >= self.bullet_rpm:
                self.ready = True

    def fire_bullet(self):
        self.bullet.add(bullet('..\\Graphics\\bullet.png',self.rect.center,-8,self.screen_size))

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.screen_size[0] - 310:
            self.rect.right = self.screen_size[0] - 310


    def update(self):
        self.get_input()
        self.constraint()
        self.firerate()
        self.bullet.update()
        self.bullet.draw(self.screen)
