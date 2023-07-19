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
# Background
background = pygame.image.load("background.png")
# Player
player_Img = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
Enemy_Img = pygame.image.load('enemy.png')
EnemyX = random.randint(0, 800)
EnemyY = random.randint(50, 150)
EnemyX_change = 2
EnemyY_change = 40

# Bullet
bullet_Img = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def player(x, y):
    screen.blit(player_Img, (x, y))


def Enemy(x, y):
    screen.blit(Enemy_Img, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_Img, (x + 16, y + 10))


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, EnemyY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # RGB
    screen.fill((0, 0, 0))
    # Inserting BG img
    screen.blit(background, (0, 0))
    playerX += playerX_change
    # Movement of Player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # Movement of Enemy
    EnemyX += EnemyX_change
    if EnemyX <= 0:
        EnemyX_change = 2
        EnemyY += EnemyY_change
    elif EnemyX >= 736:
        EnemyX_change = -2
        EnemyY += EnemyY_change

    # Movement of Bullet
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "fire"

    if bullet_state == "fire":
        fire_bullet(bulletX, EnemyY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    Enemy(EnemyX, EnemyY)
    pygame.display.update()
