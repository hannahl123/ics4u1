import pygame

pygame.init()
screen = pygame.display.set_mode((1080, 620), pygame.RESIZABLE)

# Game Title and Icon
pygame.display.set_caption("Undead Uprising")
icon = pygame.image.load('test_char.png')
pygame.display.set_icon(icon)

# Background
bg = pygame.image.load('bg.jpg')

# Character
charImg = pygame.image.load('char_blue.png')
charX = 510
charY = 280
charX_change = 0
charY_change = 0

def player(x, y):
    screen.blit(charImg, (x, y))


running = True
while running:
    screen.fill((69, 140, 41))
    w, h = pygame.display.get_surface().get_size()
    # Bg Image
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
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
                charX = w/2 - 30
                charY = h/2 - 30
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
