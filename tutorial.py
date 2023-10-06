import pygame
import sys

screen = pygame.display.set_mode((1080, 620))  # resizable not added
screen_w, screen_h = pygame.display.get_surface().get_size()
big_logo = pygame.image.load('images/UNDEAD UPRISING.png')

def intro():
    screen.blit(big_logo)
