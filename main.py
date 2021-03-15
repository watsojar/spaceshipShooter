import pygame
from ship import Ship
from background import Bg
from enemy_spawner import EnemySpawner

# display setup
WIDTH, HEIGHT = 500, 700
display = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()
black = (0, 0, 0)

# object set up
bg = Bg()
bgGroup = pygame.sprite.Group()
bgGroup.add(bg)
player = Ship()
spriteGroup = pygame.sprite.Group()
spriteGroup.add(player)
enemySpawner = EnemySpawner()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.velx = -player.speed
            elif event.key == pygame.K_d:
                player.velx = player.speed
            if event.key == pygame.K_SPACE:
                player.shoot()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.velx = 0
            elif event.key == pygame.K_d:
                player.velx = 0

    # update objects
    spriteGroup.update()
    bgGroup.update()
    enemySpawner.update()

    # render objects onto screen
    display.fill(black)
    bgGroup.draw(display)
    spriteGroup.draw(display)
    player.bullets.draw(display)
    enemySpawner.enemyGroup.draw(display)


    pygame.display.update()
