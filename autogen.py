# Auto spawn enemies

import pygame 

pygame.init()
screen = pygame.display.set_mode((800, 600))
image = pygame.image.load('images/char_red.png')
while True:
    for event in pygame.event.get(): # detect when an event is happening in the game (e.g. mouse click, key pressed, etc.)
        # detects if the exit button is clicked or the [Q] key is clicked
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            # sets the variable to False, which breaks the while loop
            break
    screen.blit(image, (200, 200))
