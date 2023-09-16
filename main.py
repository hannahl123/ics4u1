import pygame

pygame.init()
screen = pygame.display.set_mode((1080, 620))

pygame.display.set_caption("Undead Uprising")
icon = pygame.image.load('test_char.png')
pygame.display.set_icon(icon)

# Background
bg = pygame.image.load('bg.jpg')

# Character
charImg = pygame.image.load('char_blue.png')
charX = 500
charY = 300
charX_change = 0
charY_change = 0

def player(x, y):
    screen.blit(charImg, (x, y))


running = True
while running:
    screen.fill((69, 140, 41))
    # Bg Image
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("Left arrow is pressed")
                charX_change = -0.5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("Right arrow is pressed")
                charX_change = 0.5
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                print("Up arrow is pressed")
                charY_change = -0.5
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("Down arrow is pressed")
                charY_change = 0.5
            # Re-centres the character to the middle of the screen
            if event.key == pygame.K_c:
                print("Character is re-centred")
                charX = 500
                charY = 300
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("Keystroke has been released")
                charX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("Keystroke has been released")
                charY_change = 0
            if event.key == pygame.K_c:
                print("Keystroke has been released")
    charX += charX_change
    charY += charY_change
    player(charX, charY)
    pygame.display.update()
