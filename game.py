import pygame
import sys
import characters

screen = pygame.display.set_mode((1080, 620))  # resizable not added
screen_w, screen_h = pygame.display.get_surface().get_size()

big_logo = pygame.image.load('images/UNDEAD UPRISING.png')


def play(char):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            running = False
    if char == 'John':
        characters.John.start()
    elif char == 'Tony':
        screen.blit(characters.Tony.bg_img, (0, 0))
        screen.blit(characters.Tony.char_img, (screen_w / 2 - characters.Tony.char_img.get_width() / 2, 450))
    health_bar()
    pygame.display.update()


def health_bar():
    pygame.draw.rect(screen, (41, 237, 255), [20, 20, 200, 30])
