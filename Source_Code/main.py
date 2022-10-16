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

        #init state and score
        self.state = "main_menu"
        self.current_score = 0

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
            self.menu_font = pygame.font.Font(None, 50)

    def spawn_defender(self):
        self.last_defender_time = time.time()
        defend = defender("../Graphics/defender_1_small.png", (randint(1,self.screen.get_width()), 1), randint(1,3))
        self.defender_group.add(defend)

    def set_score(self, score):
        return

    def spawn_entity(self, entity):
        return

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
                    self.state = "gameover"

    def run(self):

        # clear screen
        self.screen.fill((30,30,30))

        # update state machine
        if self.state == "main_menu":
            # display main menu

            # play menu music
            if not self.music_playing:
                self.menu_music.play(loops=-1)
                self.music_playing = True

            # display game title
            text = self.menu_font.render("Run And Gun", True, (255,100,10))
            textpos = text.get_rect(centerx=self.screen.get_width() / 2, y=100)
            self.screen.blit(text,textpos)

            # set options
            menu_options = ["[p] Play Game", "[v] View High Scores", "[q] Quit"]
            
            # display options
            for i, option in enumerate(menu_options):
                text = self.menu_font.render(option, True, (255,100,10))
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

            print("main menu")


        elif self.state == "scores":
            # list of scores to display
            scores = ["High Scores"]
            scores = scores + (self.scoreDB.viewScores())

            # display each score on the screen
            for i, score in enumerate(scores):
                if i > 0:
                    score_str = f'{i}) {score}'
                    text = self.menu_font.render(score_str, True, (255,100,10))
                else:
                    text = self.menu_font.render(score, True, (255,100,10))
                textpos = text.get_rect(centerx=self.screen.get_width() / 2, y=self.screen.get_height()/4 + (self.menu_font.get_height()*2) * i)
                self.screen.blit(text,textpos)
                if i >= 5 :
                    break

            text = self.menu_font.render("[b] Back to Main Menu", True, (255,100,10))
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
                self.current_score += 7
                self.running_back_sprite.touchdown = False

            # display score
            text = self.menu_font.render(f'Score: {self.current_score}', True, (255,255,255))
            textpos = text.get_rect(x=0, y=0)
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

            self.screen.fill((30,30,30,100))

            # display score
            text = self.menu_font.render(f'Score: {self.current_score}', True, (255,255,255))
            textpos = text.get_rect(x=0, y=0)
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
            print("pause")
        elif self.state == "gameover":
            # play game over music
            #self.gameover_music.play(loops=1)
            #display game over menu
            print("gameover")
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


if __name__ == '__main__':
    game = Game((600,912))

    while True:
        game.run()
    