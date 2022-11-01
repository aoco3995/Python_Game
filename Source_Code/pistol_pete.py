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


        #power up vars
        self.power_up = False
        self.hits_till = 0
        self.power_up_time = 0
        self.power_up_time_start = 0
        self.power_up_rpm = 150
        self.bullet_speed = -20
        ####
        

        self.bullet = pygame.sprite.Group()

        self.bullet_sound = pygame.mixer.Sound('../Audio/pistol.wav')
        self.bullet_sound.set_volume(0.5)




    def get_input(self):
        keys = pygame.key.get_pressed()
        self.mouse_crt_x , self.mouse_crt_y = pygame.mouse.get_pos()
        self.rect.x = self.mouse_crt_x
        # if self.mouse_crt_x >= self.rect.x + 20:#keys[pygame.K_d]:
        #     self.rect.x += self.velocity
        # elif self.mouse_crt_x <= self.rect.x - 20:#keys[pygame.K_a]:
        #     self.rect.x -= self.velocity

        if pygame.mouse.get_pressed()[0] and self.ready:
            self.bullet_time = pygame.time.get_ticks()
            self.fire_bullet()
            self.ready = False
            self.bullet_sound.play()

        if pygame.mouse.get_pressed()[2]:
            if self.hits_till >= 3:
                self.power_up = True
                self.power_up_time = 3000
                self.power_up_time_start = pygame.time.get_ticks()

    def firerate(self):

        if not self.power_up:
            if not self.ready:
                current_time = pygame.time.get_ticks()
                if current_time - self.bullet_time >= self.bullet_rpm:
                    self.ready = True
                    
        else:
            
            current_time = pygame.time.get_ticks()
            print(current_time - self.power_up_time_start)
            if current_time - self.power_up_time_start <= self.power_up_time:
                if current_time - self.bullet_time >= self.power_up_rpm:
                    print(current_time - self.bullet_time)
                    self.ready = True
                    self.bullet_speed = -40

            else: 
                self.ready = False
                self.power_up = False
                self.hits_till = 0
                self.bullet_speed = -20


                

    def fire_bullet(self):
        self.bullet.add(bullet('..\\Graphics\\bullet.png',self.rect.center,self.bullet_speed,self.screen_size))

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.screen_size[0] - 310:
            self.rect.right = self.screen_size[0] - 310


    def update(self, hit):
        self.get_input()
        self.constraint()
        self.firerate()
        self.bullet.update()
        self.bullet.draw(self.screen)
        self.hits_till += hit