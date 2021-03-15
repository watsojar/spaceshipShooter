import pygame
import random
from enemy import Enemy

class EnemySpawner():
    def __init__(self):
        self.enemyGroup = pygame.sprite.Group()
        self.spawnTimer = random.randrange(30, 120)

    def update(self):
        self.enemyGroup.update()
        if self.spawnTimer == 0:
            self.spawnEnemy()
            self.spawnTimer = random.randrange(30, 120)
        else:
            self.spawnTimer -= 1

    def spawnEnemy(self):
        newEnemy = Enemy()
        self.enemyGroup.add(newEnemy)