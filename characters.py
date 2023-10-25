# Imports of libraries used
import pygame
import sys
import ctypes
import time

# Screen Settings - Setting size of screen and setting variables to access width and height of screen
true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
screen = pygame.display.set_mode(true_res, pygame.FULLSCREEN)
screen_w, screen_h = true_res[0], true_res[1]

class Character():
    def __init__(self):
        self.name = ""
        self.clicked = False


# Classes for all 6 characters - includes basic stats
class John:
    char_img = pygame.image.load('images/john.png') # character image
    clicked = True
    clicked_img = pygame.image.load('images/h_john.png')
    def show():
        if John.clicked:
            screen.blit(John.clicked_img, (screen_w * 2 / 7, screen_h / 2 + 20))
        else:
            screen.blit(John.char_img, (screen_w * 2 / 7, screen_h / 2 + 20))
    bg_img = pygame.image.load('images/backgrounds/bg_earth.png') # character background image
    bg_img = pygame.transform.scale(bg_img, (screen_w, screen_h))
    health = 100 # original health
    speed = 'normal' # speed of character movement
    penalty = 'normal' # movement penalty for character
    health_status = 100 # to be updated throughout the game


class Tony:
    char_img = pygame.image.load('images/tony.png')
    clicked = False
    clicked_img = pygame.image.load('images/h_tony.png')
    def show():
        if Tony.clicked:
            screen.blit(Tony.clicked_img, (screen_w * 2.5 / 7, screen_h / 2 + 20))
        else:
            screen.blit(Tony.char_img, (screen_w * 2.5 / 7, screen_h / 2 + 20))
    bg_img = pygame.image.load('images/backgrounds/bg_earth.png')
    bg_img = pygame.transform.scale(bg_img, (screen_w, screen_h))
    health = 150
    speed = 'slow'
    penalty = 'extra'
    health_status = 150 # to be updated throughout the game

class Swift:
    char_img = pygame.image.load('images/swift.png')
    clicked = False
    clicked_img = pygame.image.load('images/h_swift.png')
    def show():
        if Swift.clicked:
            screen.blit(Swift.clicked_img, (screen_w * 3 / 7, screen_h / 2 + 20))
        else:
            screen.blit(Swift.char_img, (screen_w * 3 / 7, screen_h / 2 + 20))
    bg_img = pygame.image.load('images/backgrounds/bg_ice.png')
    bg_img = pygame.transform.scale(bg_img, (screen_w, screen_h))
    health = 75
    speed = 'fast'
    penalty = 'none'
    health_status = 75 # to be updated throughout the game

class Quinn:
    char_img = pygame.image.load('images/quinn.png')
    clicked = False
    clicked_img = pygame.image.load('images/h_quinn.png')
    def show():
        if Quinn.clicked:
            screen.blit(Quinn.clicked_img, (screen_w * 3.5 / 7, screen_h / 2 + 20))
        else:
            screen.blit(Quinn.char_img, (screen_w * 3.5 / 7, screen_h / 2 + 20))
    bg_img = pygame.image.load('images/backgrounds/bg_magma.png')
    bg_img = pygame.transform.scale(bg_img, (screen_w, screen_h))
    health = 100
    speed = 'normal'
    penalty = 'normal'
    health_status = 100 # to be updated throughout the game
    quality = 'explode' # special quality

class Theresa:
    char_img = pygame.image.load('images/theresa.png')
    bg_img = pygame.image.load('images/backgrounds/bg_ice.png')
    clicked = False
    clicked_img = pygame.image.load('images/h_theresa.png')
    def show():
        if Theresa.clicked:
            screen.blit(Theresa.clicked_img, (screen_w * 4 / 7 + 10, screen_h / 2 + 20))
        else:
            screen.blit(Theresa.char_img, (screen_w * 4 / 7 + 10, screen_h / 2 + 20))
    bg_img = pygame.image.load('images/backgrounds/bg_magma.png')
    bg_img = pygame.transform.scale(bg_img, (screen_w, screen_h))
    health = 100
    speed = 'normal'
    penalty = 'light'
    health_status = 100 # to be updated throughout the game
    quality = 'heal' # special quality

class Jekyll:
    char_img = pygame.image.load('images/jekyll.png')
    bg_img = pygame.image.load('images/backgrounds/bg_earth.png')
    clicked = False
    clicked_img = pygame.image.load('images/h_jekyll.png')
    def show():
        if Jekyll.clicked:
            screen.blit(Jekyll.clicked_img, (screen_w * 4.5 / 7 + 20, screen_h / 2 + 20))
        else:
            screen.blit(Jekyll.char_img, (screen_w * 4.5 / 7 + 20, screen_h / 2 + 20))
    bg_img = pygame.image.load('images/backgrounds/bg_magma.png')
    bg_img = pygame.transform.scale(bg_img, (screen_w, screen_h))
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
