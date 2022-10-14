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

        #init game stuff
        self.state = "main_menu"
        self.current_score = 0
        self.defender_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.running_back = pygame.sprite.GroupSingle()
        self.scoreDB = ScoreDB()
        self.background_music_path = "../Audio/bgmusic.wav"

    def set_score(self, score):
        return

    def spawn_entity(self, entity):
        return

    def update_state(self):
        if self.state == "main_menu":
            #display main menu
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

    def run(self):
        self.update_state()
        self.screen.fill((30,30,30))
        pygame.display.flip()
        self.clock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    game = Game((600,800))

    while True:
        game.run()
    