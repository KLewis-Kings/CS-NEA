import pygame
from support import importSprite
from keyboard import *

GRAVITY = 0.2
JUMPACC = 2
TERMINALVEL = -7.5

class Character(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.importCharacterAssets()
        self.frameIndex = 1
        self.animationSpeed = 0.3
        self.image = self.animations["still"][self.frameIndex]
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)
#        self.direction = pygame.math.Vector2(0, 0)
        self.status = "still"
        self.mana = 3
        self.win = False
        self.gameOver = False
        self.onRight = False
        self.onLeft = False
        self.onTop = False
        self.onBottom = False
        self.xvel = 0
        self.xacc = 0
        self.yvel = 0
        self.yacc = 0
        self.maxXvel = 5
        self.minXvel = -5
        self.playAgain = False

    def importCharacterAssets(self):
        characterPath = "assets/character/"
        self.animations = {"dead": [], "space": [], "still": [], "walk": []}
        for animation in self.animations.keys():
            fullPath = characterPath + animation
            self.animations[animation] = importSprite(fullPath)

    def characterAction(self, keys):
        if not self.gameOver or not self.win:
            if self.status == "still" or self.status == None:
                if keys.left:
                    self.status = "walkingleft"
                    self.xacc = -2.5
                elif keys.right:
                    self.status = "walkingright"
                    self.xacc = 2.5
                elif keys.jump:
                    self.status = "jumpingstill"
                    self.yacc = JUMPACC
            elif self.status == "walkingleft":
                if keys.jump:
                    self.status = "jumpingleft"
                    self.yacc = JUMPACC
                elif not keys.left:
                    self.status = "still"
            elif self.status == "walkingright":
                if keys.jump:
                    self.status = "jumpingright"
                    self.yacc = JUMPACC
                elif not keys.right:
                    self.status = "still"
                elif not self.onTop:
                    self.status = "jumpingright"
                    self.yacc = GRAVITY
            elif self.status == "jumpingstill":
                if self.onTop:
                    self.status = "still"
                    self.yacc = 0
                
            elif self.status == "jumpingleft":
                if self.onTop:
                    self.status = "walkingleft"
                    self.yacc = 0
            elif self.status == "jumpingright":
                if self.onTop:
                    self.status = "walkingright"
                    self.yacc = 0
            else:
                self.status = "still"
                self.xacc = 0
                self.yacc = 0

        #adjust vel and acc based on NEW state
        if self.status == "still":
            self.xacc = 0
            self.xvel = 0
        print(self.status)

    def updateVel(self):
        if self.onTop and self.yvel<0:
            self.yvel=0
            self.yacc=0
        elif not self.onTop:
            self.yacc -= GRAVITY        

        if self.status == "walkingright" and not self.onLeft:
            self.xvel += self.xacc
        elif self.status == "walkingleft" and not self.onRight:
            self.xvel += self.xacc
        elif self.status == "jumpingstill":
            self.yvel += self.yacc
        elif self.status == "jumpingleft" :
            self.yvel += self.yacc
        elif self.status == "jumpingright" :
            self.yvel += self.yacc
        else:
            self.yacc = 0
        if self.xvel > self.maxXvel:
            self.xvel = self.maxXvel
        if self.xvel < self.minXvel:
            self.xvel = self.minXvel
        if self.yvel <= TERMINALVEL:
            self.yvel = TERMINALVEL

    def characterMovement(self):
        self.rect.x += self.xvel
        
        self.rect.y -= self.yvel
    
    def nudgexy(self,nx,ny):
        self.rect.x+=nx
        self.rect.y+=ny
        return

    def update(self, keys):
        self.characterAction(keys)
        self.updateVel()
        self.characterMovement()
        if self.gameOver and self.win:
            self.xacc = 0
            self.xvel = 0