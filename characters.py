# Imports of libraries used
import pygame
import sys
import ctypes
import time

# Screen Settings - Setting size of screen and setting variables to access width and height of screen
true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
screen = pygame.display.set_mode(true_res, pygame.FULLSCREEN)
screen_w, screen_h = true_res[0], true_res[1]

# Classes for all 6 characters - includes basic stats
class John:
    char_img = pygame.image.load('images/john.png') # character image
    bg_img = pygame.image.load('images/backgrounds/bg_earth.png') # character background image
    bg_img = pygame.transform.scale(bg_img, (screen_w, screen_h))
    health = 100 # original health
    speed = 'normal' # speed of character movement
    penalty = 'normal' # movement penalty for character
    health_status = 100 # to be updated throughout the game


class Tony:
    char_img = pygame.image.load('images/tony.png')
    bg_img = pygame.image.load('images/backgrounds/bg_earth.png')
    bg_img = pygame.transform.scale(bg_img, (screen_w, screen_h))
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
    char_img = pygame.image.load('images/quinn.png')
    bg_img = pygame.image.load('images/backgrounds/bg_magma.png')
    health = 100
    speed = 'normal'
    penalty = 'normal'
    health_status = 100 # to be updated throughout the game
    quality = 'explode' # special quality

class Theresa:
    char_img = pygame.image.load('images/theresa.png')
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
