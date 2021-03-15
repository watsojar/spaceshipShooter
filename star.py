import pygame
import random

WIDTH, HEIGHT = 500, 700


class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.width = random.randrange(1, 4)
        self.height = self.width
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.color = (255, 255, 255)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH)
        self.velx = 0
        self.vely = random.randrange(4, 25)

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely


