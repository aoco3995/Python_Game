import pygame, sys
from bullet import bullet
#from bullet import bullet
from defender_1 import defender
from entity import entity
from running_back import running_back
#from laser import Laser
from ScoreDB import ScoreDB
import time
from random import *
from pistol_pete import pistol_pete

defender1_sprite = []
defender1 = []
class Game:


    def __init__(self,screensize):
        #init pygame and screen
        pygame.init()
        self.screen = pygame.display.set_mode(screensize)
        self.clock = pygame.time.Clock()

        #Background
        self.background_sprite = entity("..\\Graphics\\background_football_field.jpg",(self.screen.get_width()/2,self.screen.get_height()/2),0)
        self.background = pygame.sprite.GroupSingle(self.background_sprite)

        self.menu_bg_sprite = entity("..\\Graphics\\boone_pickens.png",(self.screen.get_width()/2, self.screen.get_height()/2),0)
        self.menu_bg = pygame.sprite.GroupSingle(self.menu_bg_sprite)

        self.gameover_bg_sprite = entity("..\\Graphics\\gameover.jpg",(self.screen.get_width()/2, self.screen.get_height()/2),0)
        self.gameover_bg = pygame.sprite.GroupSingle(self.gameover_bg_sprite)

        #init state and score
        self.state = "main_menu"
        self.current_score = 0
        self.current_down = 1

        #init player
        pistol_pete_sprite = pistol_pete("..\\Graphics\\pistol_pete.png",(self.screen.get_width()/2, self.screen.get_height()-20),5,(self.screen.get_height(),self.screen.get_width()), self.screen)
        self.player = pygame.sprite.GroupSingle(pistol_pete_sprite)

        #init bullets
        self.bullet_group = pygame.sprite.Group()

        #init running back
        self.running_back_sprite = running_back("..\\Graphics\\running_back.png", (screensize[0]*(5/10), screensize[1]*(9/10)),2, (self.screen.get_height(),self.screen.get_width()))
        self.running_back = pygame.sprite.GroupSingle(self.running_back_sprite)

        #init score database
        self.scoreDB = ScoreDB()
        self.initial = ['A','A','A']
        self.initial_index = 0
        self.score_saved = False
        self.blink = False
        self.blink_timer = 0

        #self.spawn_defender()
        self.defender_group = pygame.sprite.Group()
        self.last_defender_time = time.time()
        self.defender_spawn_rate = 5.0

        #init music
        self.game_music = pygame.mixer.Sound('../Audio/battleThemeA.wav')
        self.game_music.set_volume(0.05)

        self.menu_music = pygame.mixer.Sound('../Audio/the_field_of_dreams.wav')
        self.menu_music.set_volume(0.05)

        self.music_playing = False

        self.hit_sound = pygame.mixer.Sound('../Audio/hit.wav')
        self.hit_sound.set_volume(0.3)

        self.tackeled_sound = pygame.mixer.Sound('../Audio/dsplpain.wav')
        self.tackeled_sound.set_volume(0.3)

        #init font
        pygame.font.init()
        if pygame.font:
            self.menu_font = pygame.font.Font(None, 70)
            self.gameover_font = pygame.font.Font(None, 120)

    def spawn_defender(self):
        self.last_defender_time = time.time()
        defend = defender("../Graphics/defender_1_small.png", (randint(1,self.screen.get_width()), 1), randint(1,3))
        self.defender_group.add(defend)

    def collision_checks(self):
        # player lasers 
        if self.player.sprite.bullet:
            for bullet in self.player.sprite.bullet:
                defender_hit = pygame.sprite.spritecollide(bullet,self.defender_group,True)
                if defender_hit:
                    bullet.kill()
                    self.hit_sound.play()
                    self.current_score += 1

        # running back
        if self.defender_group:
            for defender in self.defender_group:
                if pygame.sprite.spritecollide(defender,self.running_back,False):
                    self.tackeled_sound.play()
                    self.current_down += 1
                    self.defender_group.remove(self.defender_group)

    def run(self):
        # clear screen
        self.screen.fill((30,30,30))

        # update state machine
        if self.state == "main_menu":
            # display main menu

            self.menu_bg.draw(self.screen)

            # blur background
            button_bg = pygame.Surface((600,800))
            button_bg.set_alpha(196)
            button_bg.fill((0,0,0))
            self.screen.blit(button_bg, (self.screen.get_width()/2 - button_bg.get_width()/2, self.screen.get_height()/2 - button_bg.get_height()/2 - 100))

            # play menu music
            if not self.music_playing:
                self.menu_music.play(loops=-1)
                self.music_playing = True

            # display game title
            text = self.menu_font.render("Run And Gun", True, (255,255,255))
            textpos = text.get_rect(centerx=self.screen.get_width() / 2, y=100)
            self.screen.blit(text,textpos)

            # set options
            menu_options = ["[p] Play Game", "[v] View High Scores", "[q] Quit"]
            
            # display options
            for i, option in enumerate(menu_options):
                text = self.menu_font.render(option, True, (255,255,255))
                textpos = text.get_rect(centerx=self.screen.get_width() / 2, y=self.screen.get_height()/2 + (self.menu_font.get_height()*2) * i)
                self.screen.blit(text,textpos)

            # get user input to change state
            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:
                self.music_playing = False
                self.menu_music.stop()
                self.state = "running"
            elif keys[pygame.K_v]:
                self.state = "scores"
            elif keys[pygame.K_q]:
                self.state = "quit"



        elif self.state == "scores":
            # list of scores to display
            scores = ["High Scores"]
            scores = scores + (self.scoreDB.viewScores())

            self.menu_bg.draw(self.screen)

            # blur background
            button_bg = pygame.Surface((600,1000))
            button_bg.set_alpha(196)
            button_bg.fill((0,0,0))
            self.screen.blit(button_bg, (self.screen.get_width()/2 - button_bg.get_width()/2, self.screen.get_height()/5))

            # display each score on the screen
            for i, score in enumerate(scores):
                if i > 0:
                    score_str = f'{i}) {score}'
                    text = self.menu_font.render(score_str, True, (255,255,255))
                else:
                    text = self.menu_font.render(score, True, (255,255,255))
                textpos = text.get_rect(centerx=self.screen.get_width() / 2, y=self.screen.get_height()/4 + (self.menu_font.get_height()*2) * i)
                self.screen.blit(text,textpos)
                if i >= 5 :
                    break

            text = self.menu_font.render("[b] Back to Main Menu", True, (255,255,255))
            textpos = text.get_rect(centerx=self.screen.get_width() / 2, y=self.screen.get_height() - self.menu_font.get_height())
            self.screen.blit(text,textpos)
        
            # get input to go back to menu
            keys = pygame.key.get_pressed()
            if keys[pygame.K_b]:
                self.state = "main_menu"
            print("scores")


        elif self.state == "running":
            #play the game

            if not self.music_playing:
                self.game_music.play(loops = -1)
                self.music_playing = True

            #print("running")

            self.background.draw(self.screen)

            self.running_back.update()
            self.running_back.draw(self.screen)

            self.player.update()
            self.player.draw(self.screen)

            #print(self.running_back_sprite.get_object_rect())

            if (time.time() - self.last_defender_time) > self.defender_spawn_rate:
                game.spawn_defender()
                self.defender_spawn_rate -=((self.defender_spawn_rate*self.defender_spawn_rate)/100)
            self.defender_group.update(self.running_back_sprite)
            self.defender_group.draw(self.screen)

            self.collision_checks()


            if self.running_back_sprite.touchdown:
                self.defender_group.remove(self.defender_group)
                self.current_score += 7
                self.running_back_sprite.touchdown = False
                self.current_down = 1

            # display score
            text = self.menu_font.render(f'Score: {self.current_score}', True, (255,255,255))
            textpos = text.get_rect(x=0, y=0)
            self.screen.blit(text,textpos)


            if self.current_down > 4:
                self.state = "gameover"


            # display downs (lives)
            text = self.menu_font.render(f'Down: {self.current_down}', True, (255,255,255))
            textpos = text.get_rect(right=self.screen.get_width(), y=0)
            self.screen.blit(text,textpos)


            # get user input to change state
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.music_playing = False
                self.game_music.stop()
                self.state = "pause"



        elif self.state == "pause":

            # play menu music
            if not self.music_playing:
                self.menu_music.play(loops=-1)
                self.music_playing = True

            # draw everything that was on the screen
            self.background.draw(self.screen)
            self.running_back.draw(self.screen)
            self.defender_group.draw(self.screen)

            # blur screen
            button_bg = pygame.Surface((self.screen.get_width(),self.screen.get_height()))
            button_bg.set_alpha(196)
            button_bg.fill((0,0,0))
            self.screen.blit(button_bg, (0,0))

            # display score
            text = self.menu_font.render(f'Score: {self.current_score}', True, (255,255,255))
            textpos = text.get_rect(x=0, y=0)
            self.screen.blit(text,textpos)

            # display downs (lives)
            text = self.menu_font.render(f'Down: {self.current_down}', True, (255,255,255))
            textpos = text.get_rect(right=self.screen.get_width(), y=0)
            self.screen.blit(text,textpos)

            # set options
            menu_options = ["Paused", "[r] Resume", "[q] Quit"]
            
            # display options
            for i, option in enumerate(menu_options):
                text = self.menu_font.render(option, True, (255,100,10))
                textpos = text.get_rect(centerx=self.screen.get_width() / 2, y=self.screen.get_height()/3 + (self.menu_font.get_height()*2) * i)
                self.screen.blit(text,textpos)

            # get user input to change state
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.music_playing = False
                self.menu_music.stop()
                self.state = "running"
            elif keys[pygame.K_q]:
                self.state = "quit"

            #display pause menu
        elif self.state == "gameover":
            # play game over music
            #self.gameover_music.play(loops=1)
            #display game over menu

            self.gameover_bg.draw(self.screen)

            # blur background
            blur_bg = pygame.Surface((1000,1000))
            blur_bg.set_alpha(196)
            blur_bg.fill((0,0,0))
            self.screen.blit(blur_bg, (self.screen.get_width()/2 - blur_bg.get_width()/2, self.screen.get_height()/2 - blur_bg.get_height()/2 + 100))

            # prompt for initials
            text = self.menu_font.render("Enter your initals to save your score using the arrow keys: ", True, (255,100,10))
            textpos = text.get_rect(centerx=self.screen.get_width() / 2, y=self.screen.get_height()/2 - (self.menu_font.get_height()*4))
            self.screen.blit(text,textpos)

            # increase blink
            if self.blink_timer % 6 == 0:
                self.blink = not self.blink
            self.blink_timer += 1

            # print current initials
            for i, letter in enumerate(self.initial):
                if self.blink and self.initial_index == i:
                    text = self.menu_font.render("_", True, (255,255,255))
                else:
                    text = self.menu_font.render(letter, True, (255,255,255))

                textpos = text.get_rect(x=self.screen.get_width() / 2 - self.menu_font.get_height() * (3-i), y=self.screen.get_height()/2 + (self.menu_font.get_height()))
                self.screen.blit(text,textpos)

            # print score
            text = self.menu_font.render(str(self.current_score), True, (255,255,255))
            textpos = text.get_rect(x=self.screen.get_width() / 2 + self.menu_font.get_height() * 3, y=self.screen.get_height()/2 + (self.menu_font.get_height()))
            self.screen.blit(text,textpos)

            # print gameover
            text = self.gameover_font.render("GAME OVER!", True, (255,100,10))
            textpos = text.get_rect(centerx=self.screen.get_width() / 2, y=self.screen.get_height()/2 - (self.menu_font.get_height()*6))
            self.screen.blit(text,textpos)

            # print menu option
            text = self.menu_font.render("Press [Esc] to go back to Main Menu", True, (255,100,10))
            textpos = text.get_rect(centerx=self.screen.get_width() / 2, y=self.screen.get_height()*(3/4) + (self.menu_font.get_height()*2))
            self.screen.blit(text,textpos)

            # get input to go back to menu
            # and handle inital inputs
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.game_music.stop()
                name = ""
                for letter in self.initial:
                    name += letter
                self.scoreDB.addScore((name, self.current_score))
                return True
            elif keys[pygame.K_UP]:
                if self.initial_index < 3 and ord(self.initial[self.initial_index]) > ord("A"):
                    self.initial[self.initial_index] = chr(ord(self.initial[self.initial_index])-1)
                time.sleep(0.1)
            elif keys[pygame.K_DOWN]:
                if self.initial_index < 3 and ord(self.initial[self.initial_index]) < ord("Z"):
                    self.initial[self.initial_index] = chr(ord(self.initial[self.initial_index])+1)
                time.sleep(0.1)
            elif keys[pygame.K_RIGHT]:
                self.initial_index += 1
                time.sleep(0.1)
            elif keys[pygame.K_LEFT]:
                if self.initial_index > 0:
                    self.initial_index -= 1
                time.sleep(0.1)

        elif self.state == "quit":
            #quit the game
            print("quit")
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        self.clock.tick(30)

        #handle exiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        return False


if __name__ == '__main__':
   
   while True:
        game = Game((1920,1000))
        new_game = False
        while new_game == False:
            new_game = game.run()
        