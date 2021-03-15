import pygame
from star import Star
import random

WIDTH, HEIGHT = 500, 700


class Bg(pygame.sprite.Sprite):
    def __init__(self):
        super(Bg, self).__init__()
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.color = (0, 0, 15)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.timer = random.randrange(1, 10)

    def update(self):
        self.stars.update()
        for star in self.stars:
            if star.rect.y >= HEIGHT:
                self.stars.remove(star)
        if self.timer == 0:
            newStar = Star()
            self.stars.add(newStar)
            self.timer = random.randrange(1, 10)
        self.image.fill(self.color)
        self.stars.draw(self.image)
        self.timer -= 1
