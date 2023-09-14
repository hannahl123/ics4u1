import pygame

pygame.init()
screen = pygame.display.set_mode((1080, 620))

pygame.display.set_caption("Undead Uprising")
icon = pygame.image.load('test_char.png')
pygame.display.set_icon(icon)
# icon = pygame.image.load('')
# pygame.display.set_icon(icon)

# Background
bg = pygame.image.load('test_bg.png')

# Character
charImg = pygame.image.load('test_char.png')
charX = 200
charY = 100

running = True
while running:
    screen.fill((0, 0, 0))
    # Bg Image
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
