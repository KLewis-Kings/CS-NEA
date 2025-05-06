import pygame
from blocks import Blocks
from hazards import Hazards
from checkpoint import Checkpoint
from character import Character
from game import Game
from support import BLOCKSIZE, WIDTH
from keyboard import *
# Constructor for map data
class Map:
    def __init__(self, mapData, SCREEN):
        self.gravity = 3
        self.mapData = mapData
        self.setupMap(mapData)
        self.screen = SCREEN
        self.mapShift = 0
        self.game = Game(self.screen)

    def setupMap(self, layout):
        self.blocks = pygame.sprite.Group()
        self.hazards = pygame.sprite.Group()
        self.checkpoint = pygame.sprite.GroupSingle()
        self.character = pygame.sprite.GroupSingle()
# Goes through each row checking each cell and denoting it to it's designated group
        for rowIndex, row in enumerate(layout):
            for colIndex, cell in enumerate(row):
                x, y = (colIndex*BLOCKSIZE), (rowIndex*BLOCKSIZE)
                if cell == "X":
                    block = Blocks((x,y), BLOCKSIZE)
                    self.blocks.add(block)
                elif cell == "P":
                    characterSprite = Character((x, y-4))
                    self.character.add(characterSprite)
                elif cell == "H":
                    block = Hazards((x+(BLOCKSIZE//2), y+(BLOCKSIZE//2)), BLOCKSIZE/5)
                    self.hazards.add(block)
                elif cell == "C":
                    checkpointSprite = Checkpoint((x,y), BLOCKSIZE)
                    self.checkpoint.add(checkpointSprite)

    def Overlap(self, At, Ab, Bt, Bb):
        if (At <= Bt) and (Ab >= Bt):
            return True
        if (At <= Bt) and (Ab >= Bb):
            return True
        if (At >= Bt) and (At <= Bb):
            return True
        if (At >= Bt) and (Ab <= Bb):
            return True
        return False
    
# Ensuring character will collide with blocks
    def collisions(self):
        character = self.character.sprite
        character.onLeft = False
        character.onRight = False
        character.onTop = False
        character.onBottom = False
        for sprite in self.blocks.sprites():
            if sprite.rect.colliderect(character.rect):
                #check for top/bottom
                if self.Overlap(character.rect.left, character.rect.right, sprite.rect.left, sprite.rect.right):
                    if character.yacc <= 0:
                        character.onTop = True                      
                    elif character.yacc > 0:
                        character.onBotton = True
                if self.Overlap(character.rect.top, character.rect.bottom, sprite.rect.top, sprite.rect.bottom):
                    if character.status == "walkingleft" or character.status == "jumpingleft":
                        character.onRight = True    
                    elif character.status == "walkingright" or character.status == "jumpingright":
                        character.onLeft = True
                #now nudge the character to the appropriate boundaries
                while sprite.rect.colliderect(character.rect):
                    if character.onTop:
                        character.nudgexy(0,-1)
                    elif character.onBottom:
                        character.nudgexy(0,1)
                    if character.onLeft:
                        character.nudgexy(-1,0)
                    elif character.onRight:
                        character.nudgexy(1,0)
                #place just inside by 1 pixel
                if character.onTop:
                    character.nudgexy(0,1)
                elif character.onBottom:
                    character.nudgexy(0,-1)
                if character.onLeft:
                    character.nudgexy(1,0)
                elif character.onRight:
                    character.nudgexy(-1,0)

        return
    def hazardCollisions(self):
        character = self.character.sprite
        for sprite in self.hazards.sprites():
            if sprite.rect.colliderect(character.rect):
# Prevents character getting stuck when colliding
                if character.xvel > 0 or character.yvel > 0:
                    character.rect.x = character.rect.x - BLOCKSIZE
                if character.xvel < 0 or character.xvel < 0:
                    character.rect.x = character.rect.x + BLOCKSIZE
# Deducts a mana point when hit
                character.mana = character.mana - 1

# Side scroller lets the map move behind the character
    def scrollX(self):
        character = self.character.sprite
# When the character reaches a certain point of the map, the world will scroll and halt its' movement allowing it to move freely
        if character.rect.centerx < (WIDTH // 2) and (character.xvel < 0):
            self.mapShift = 50
            character.rect.x += (self.mapShift * 0.67)
        elif character.rect.centerx > WIDTH - (WIDTH // 7) and (character.xvel > 0):
            self.mapShift = -50
            character.rect.x += (self.mapShift * 0.67)
        else:
            self.mapShift = 0

    def update(self, keys):
# Updating map
        self.collisions()
        self.hazardCollisions()
        self.character.update(keys)
        self.game.showMana(self.character.sprite)
        self.character.draw(self.screen)
        self.game.gameStatus(self.character.sprite, self.checkpoint.sprite)
# Updating blocks
        self.blocks.update(self.mapShift)
        self.blocks.draw(self.screen)
# Updating hazards
        self.hazards.update(self.mapShift)
        self.hazards.draw(self.screen)
# Updating checkpoints
        self.checkpoint.update(self.mapShift)
        self.checkpoint.draw(self.screen)
        self.scrollX()