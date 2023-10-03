import pygame
import sys

class John:
    char_img = pygame.image.load('images/john.png')
    health = 100
    speed = 'normal'
    penalty = 'normal'
    health_status = 100

class Tony:
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
    health = 100
    speed = 'normal'
    penalty = 'normal'
    health_status = 100
    quality = 'explode'

class Theresa:
    health = 100
    speed = 'normal'
    penalty = 'light'
    health_status = 100
    quality = 'heal'

class Jekyll:
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
