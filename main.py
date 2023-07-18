import pygame
import random

# Initialize PyGame
pygame.init()

# Creating a Display
screen = pygame.display.set_mode((800, 600))

# Caption
pygame.display.set_caption("Space Warriors")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
# Player
player_Img = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
Enemy_Img = pygame.image.load('enemy.png')
EnemyX = random.randint(0,800)
EnemyY = random.randint(50,150)
EnemyX_change = 0.3
EnemyY_change = 0


def player(x, y):
    screen.blit(player_Img, (x, y))


def Enemy(x, y):
    screen.blit(Enemy_Img, (x, y))


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # RGB
    screen.fill((0, 0, 0))
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    EnemyX += EnemyX_change
    if EnemyX <= 0:
        EnemyX_change = 0.3
    elif EnemyX >= 736:
        EnemyX_change = -0.3

    player(playerX, playerY)
    Enemy(EnemyX,EnemyY)
    pygame.display.update()
