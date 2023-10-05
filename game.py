import pygame
import sys

screen = pygame.display.set_mode((1080, 620))  # resizable not added
screen_w, screen_h = pygame.display.get_surface().get_size()

bg = pygame.image.load('images/bg_magma.png')

big_logo = pygame.image.load('images/UNDEAD UPRISING.png')

def play():
    screen.blit(bg, (0, 0))
    char_img = pygame.image.load('images/john.png')
    screen.blit(char_img, (screen_w / 2 - char_img.get_width() / 2, 450))

