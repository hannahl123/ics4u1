# Imports of libraries used
import pygame
import sys
import time

# Setting Screen Size
screen = pygame.display.set_mode((1080, 620))  # resizable not added
screen_w, screen_h = pygame.display.get_surface().get_size()


# Classes for all 6 characters - includes basic stats
class John:
    char_img = pygame.image.load('images/john.png') # character image
    bg_img = pygame.image.load('images/backgrounds/bg_earth.png') # character background image
    charX, charY = screen_w / 2 - 45 / 2, 450 # position of character
    health = 100 # original health
    speed = 'normal' # speed of character movement
    penalty = 'normal' # movement penalty for character
    health_status = 100 # to be updated throughout the game

class Tony:
    char_img = pygame.image.load('images/char_blue.png')
    bg_img = pygame.image.load('images/backgrounds/bg_earth.png')
    health = 150
    speed = 'slow'
    penalty = 'extra'
    health_status = 150 # to be updated throughout the game

class Swift:
    char_img = pygame.image.load('images/swift.png')
    bg_img = pygame.image.load('images/backgrounds/bg_ice.png')
    health = 75
    speed = 'fast'
    penalty = 'none'
    health_status = 75 # to be updated throughout the game

class Quinn:
    char_img = pygame.image.load('images/char_green.png')
    bg_img = pygame.image.load('images/backgrounds/bg_magma.png')
    health = 100
    speed = 'normal'
    penalty = 'normal'
    health_status = 100 # to be updated throughout the game
    quality = 'explode' # special quality

class Theresa:
    char_img = pygame.image.load('images/char_yellow.png')
    bg_img = pygame.image.load('images/backgrounds/bg_ice.png')
    health = 100
    speed = 'normal'
    penalty = 'light'
    health_status = 100 # to be updated throughout the game
    quality = 'heal' # special quality

class Jekyll:
    char_img = pygame.image.load('images/jekyll.png')
    bg_img = pygame.image.load('images/backgrounds/bg_earth.png')
    health = 100
    speed = 'fast'
    penalty = 'light'
    health_status = 100 # to be updated throughout the game
    quality = 'poison_trail' # special quality

# Special qualities for characters
def explode():
    print()

def heal():
    print()

def poison_trail():
    print()
