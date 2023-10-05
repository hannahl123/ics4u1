import pygame
import sys
import time

class John:
    char_img = pygame.image.load('images/john.png')
    health = 100
    speed = 'normal'
    penalty = 'normal'
    health_status = 100

class Tony:
    char_img = pygame.image.load('images/char_blue.png')
    health = 150
    speed = 'slow'
    penalty = 'extra'
    health_status = 150

class Swift:
    char_img = pygame.image.load('images/swift.png')
    health = 75
    speed = 'fast'
    penalty = 'none'
    health_status = 75

class Quinn:
    char_img = pygame.image.load('images/char_green.png')
    health = 100
    speed = 'normal'
    penalty = 'normal'
    health_status = 100
    quality = 'explode'

class Theresa:
    char_img = pygame.image.load('images/char_yellow.png')
    health = 100
    speed = 'normal'
    penalty = 'light'
    health_status = 100
    quality = 'heal'

class Jekyll:
    char_img = pygame.image.load('images/jekyll.png')
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
