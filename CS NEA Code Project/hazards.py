import pygame
from support import importSprite

class Hazards(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.fireImg = importSprite("assets/hazards/")
        self.frameIndex = 1
        self.animationDelay = 2
        self.image = self.fireImg[self.frameIndex]
        self.image = pygame.transform.scale(self.image, (size, size))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft = pos)

# Update object position due to world scroll
    def update(self, xShift):
        self.rect.x = self.rect.x + xShift