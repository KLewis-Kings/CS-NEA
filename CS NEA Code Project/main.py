import pygame
import sys
from map import *
from support import *
from levels import *
import keyboard
import random

pygame.init()
# Setting up the screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
# Constructor for the intial bootup
class Platformer:
    def __init__(self, SCREEN, WIDTH, HEIGHT):
        self.clock = pygame.time.Clock()
        self.screen =  SCREEN
        self.backgImg = pygame.image.load('./assets/terrain/background.jpg')
        self.backgImg = pygame.transform.scale(self.backgImg, (WIDTH, HEIGHT))
# Main loop to control flow of the game as well as registering key presses
    def main(self):
        levels = Levels()
        levels.initLevels()
        map = Map(levels.getLevel(0), self.screen)
        keys = keyboard.keyboard()
        while True:
            self.screen.blit(self.backgImg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    keys.setKeys(pygame.key.get_pressed())
                    if event.key == pygame.K_y or event.key == pygame.K_r:
                            play.main()
                elif event.type == pygame.KEYUP:
                    keys.setKeys(pygame.key.get_pressed())
            self.clock.tick(60)
            map.update(keys)
            pygame.display.update()

if __name__ == "__main__":
    play = Platformer(SCREEN, WIDTH, HEIGHT)
    play.main()