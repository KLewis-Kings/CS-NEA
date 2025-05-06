import pygame
LEFTKEYS= [pygame.K_a, pygame.K_LEFT, pygame.K_j]
RIGHTKEYS = [pygame.K_d, pygame.K_RIGHT, pygame.K_l]
JUMPKEYS = [pygame.K_SPACE, pygame.K_w, pygame.K_UP, pygame.K_i, pygame.MOUSEBUTTONDOWN]

class keyboard():

    def __init__(self):
        self.jump = False
        self.left = False
        self.right = False
        self.playAgain = False

    def setJumpState(self, state):
        self.jump = state
    
    def setLeftState(self, state):
        self.left = state
    
    def setRightState(self, state):
        self.right = state

    def setKeys(self, keys):
        left = False
        right = False
        jump = False
        for keycode in LEFTKEYS:
            if keys[keycode]:
                left = True
        for keycode in RIGHTKEYS:
            if keys[keycode]:
                right = True
        for keycode in JUMPKEYS:
            if keys[keycode]:
                jump = True
        self.setJumpState(jump)
        self.setLeftState(left)
        self.setRightState(right)
        return