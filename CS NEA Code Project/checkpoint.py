import pygame

class Checkpoint(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        imgPath = 'assets/checkpoint/checkpoint-removebg-preview.png'
        self.image = pygame.image.load(imgPath)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)

# Updating objects with side scroll
    def update(self, xShift):
        self.rect.x = self.rect.x + xShift