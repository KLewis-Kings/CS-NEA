from os import walk
import pygame
WIDTH, HEIGHT = 1080, 720
BLOCKSIZE = 40
def importSprite(path):
    surfaceList = []
    for _, __, imgFile in walk(path):
        for image in imgFile:
            fullPath = f"{path}/{image}"
            imgSurface = pygame.image.load(fullPath).convert_alpha()
            surfaceList.append(imgSurface)
    return surfaceList