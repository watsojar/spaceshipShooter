import pygame
from bullet import Bullet

WIDTH, HEIGHT = 500, 700


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.image = pygame.image.load("Assets copy/spaceship_red.png").convert_alpha()
        self.image = pygame.transform.rotate(pygame.transform.scale(self.image, (55, 40)), 180)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT - self.rect.height - 10
        self.bullets = pygame.sprite.Group()
        self.velx = 0
        self.vely = 0
        self.speed = 5

    def update(self):
        self.bullets.update()
        for bullet in self.bullets:
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        self.rect.x += self.velx
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width
        self.rect.y += self.vely

    def shoot(self):
        newBullet = Bullet()
        newBullet.rect.x = self.rect.x + (self.rect.width // 2) - 1
        newBullet.rect.y = self.rect.y
        self.bullets.add(newBullet)
