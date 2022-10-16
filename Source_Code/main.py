import pygame, sys
#from bullet import bullet
#from defender_1 import defender1
#from entity import entity
#from running_back import running_back
#from laser import Laser
from ScoreDB import ScoreDB

class Game:

    def __init__(self,screensize):
        #init pygame and screen
        pygame.init()
        self.screen = pygame.display.set_mode(screensize)
        self.clock = pygame.time.Clock()

        #init state and score
        self.state = "main_menu"
        self.current_score = 0

        #init player
        #pistol_pete_sprite = Pistol_Pete((screensize[0]/2, screensize[1]))
        #self.player = pygame.sprite.GroupSingle(pistol_pete_sprite)

        #init bullets
        self.bullet_group = pygame.sprite.Group()

        #init defenders
        self.defender_group = pygame.sprite.Group()
        #self.init_defenders()

        #init running back
        #running_back_sprite = Running_Back((screensize[0]/2, screensize[1]/2))
        #self.running_back = pygame.sprite.GroupSingle(running_back_sprite)

        #init score database
        self.scoreDB = ScoreDB()

        #init background music
        music = pygame.mixer.Sound('../Audio/bg_music.wav')
        music.set_volume(0.05)
        music.play(loops = -1)

        #init font
        pygame.font.init()
        if pygame.font:
            self.menu_font = pygame.font.Font(None, 50)

    def set_score(self, score):
        return

    def spawn_entity(self, entity):
        return

    def run(self):
        # update state machine
        if self.state == "main_menu":
            #display main menu
            menu_options = ["[p] Play Game", "[v] View High Scores", "[q] Quit"]
            for i, option in enumerate(menu_options):
                text = self.menu_font.render(option, True, (255,100,10))
                textpos = text.get_rect(centerx=self.screen.get_width() / 2, y=self.screen.get_height()/3 + (self.menu_font.get_height()*2) * i)
                self.screen.blit(text,textpos)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:
                self.state = "running"
            elif keys[pygame.K_v]:
                self.state = "scores"
            elif keys[pygame.K_q]:
                self.state = "quit"
            print("main menu")
        elif self.state == "scores":
            #display top scores
            print("scores")
        elif self.state == "running":
            #play the game
            print("running")
        elif self.state == "pause":
            #display pause menu
            print("pause")
        elif self.state == "gameover":
            #display game over menu
            print("gameover")
        elif self.state == "quit":
            #quit the game
            print("quit")
            pygame.quit()
            sys.exit()

        #self.screen.fill((30,30,30))
        pygame.display.flip()
        self.clock.tick(60)

        #handle exiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    game = Game((600,800))

    while True:
        game.run()
    