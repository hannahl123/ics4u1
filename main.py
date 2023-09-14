import pygame

pygame.init()
screen = pygame.display.set_mode((1080, 720))

pygame.display.set_caption("Undead Uprising")
icon = pygame.image.load('')
pygame.display.set_icon(icon)

# Character
charImg = pygame.image.load('')
charX = 0
charY = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.update()
