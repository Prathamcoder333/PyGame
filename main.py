import pygame

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


def player(x, y):
    screen.blit(player_Img, (x, y))


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow key is pressed")
            if event.key == pygame.K_RIGHT:
                print("Right arrow key is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")


    # RGB
    screen.fill((0, 0, 0))
    player(playerX, playerY)
    pygame.display.update()
