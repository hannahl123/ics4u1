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

def player():
    screen.blit(charImg, (charX, charY))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    # Bg Image
    screen.blit(bg, (0, 0))
    player()
    pygame.display.update()
