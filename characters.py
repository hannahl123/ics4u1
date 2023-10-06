import pygame
import sys
import time

screen = pygame.display.set_mode((1080, 620))  # resizable not added
screen_w, screen_h = pygame.display.get_surface().get_size()

class John:
    char_img = pygame.image.load('images/john.png')
    bg_img = pygame.image.load('images/backgrounds/bg_earth.png')
    def start():
        screen.blit(John.bg_img, (0, 0))
        screen.blit(John.char_img, (screen_w / 2 - John.char_img.get_width() / 2, 450))
    health = 100
    speed = 'normal'
    penalty = 'normal'
    health_status = 100

class Tony:
    char_img = pygame.image.load('images/char_blue.png')
    bg_img = pygame.image.load('images/backgrounds/bg_earth.png')
    health = 150
    speed = 'slow'
    penalty = 'extra'
    health_status = 150

class Swift:
    char_img = pygame.image.load('images/swift.png')
    bg_img = pygame.image.load('images/backgrounds/bg_ice.png')
    health = 75
    speed = 'fast'
    penalty = 'none'
    health_status = 75

class Quinn:
    char_img = pygame.image.load('images/char_green.png')
    bg_img = pygame.image.load('images/backgrounds/bg_magma.png')
    health = 100
    speed = 'normal'
    penalty = 'normal'
    health_status = 100
    quality = 'explode'

class Theresa:
    char_img = pygame.image.load('images/char_yellow.png')
    bg_img = pygame.image.load('images/backgrounds/bg_ice.png')
    health = 100
    speed = 'normal'
    penalty = 'light'
    health_status = 100
    quality = 'heal'

class Jekyll:
    char_img = pygame.image.load('images/jekyll.png')
    bg_img = pygame.image.load('images/backgrounds/bg_earth.png')
    health = 100
    speed = 'fast'
    penalty = 'light'
    health_status = 100
    quality = 'poison_trail'

def explode():
    print()

def heal():
    print()

def poison_trail():
    print()
