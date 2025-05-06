import pygame
from main import SCREEN, WIDTH, HEIGHT
pygame.font.init()
from keyboard import *

class Game:
    def __init__(self, SCREEN):
        self.screen = SCREEN
        self.font = pygame.font.SysFont("impact", 70)
        self.messageColour = pygame.Color("darkorange")

    def showMana(self, character):
        imgPath = "assets/mana/mana.png"
        manaSize = 50
        manaImage = pygame.image.load(imgPath)
        manaImage = pygame.transform.scale(manaImage, (manaSize, manaSize))
        indent = -0.5 * manaSize
        for mana in range(character.mana):
            indent = indent + manaSize
            self.screen.blit(manaImage, (indent, 0.5 * manaSize))

    def gameStatus(self, character, checkpoint):
        if character.mana <= 0 or character.rect.y >= HEIGHT:
            self.gameLost(character)
        elif character.rect.colliderect(checkpoint.rect):
            self.gameWon(character)

    def gameWon(self, character):
        character.win = True
        character.gameOver = True
        message = self.font.render("You won, Press Y to play again.", True, self.messageColour)
        self.screen.blit(message, (WIDTH / 8, 70))
    
    def gameLost(self, character):
        character.lose = True
        character.gameOver = True
        message = self.font.render("You lost, Press Y to play again.", True, self.messageColour)
        self.screen.blit(message, (WIDTH / 8, 70))