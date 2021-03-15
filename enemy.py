import pygame
import random
WIDTH, HEIGHT = 500, 700

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("Assets copy/spaceship_yellow.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (55, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(10, WIDTH - self.rect.width - 10)
        self.rect.y = -self.rect.height
        self.velx = 0
        self.vely = random.randrange(3, 8)

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        