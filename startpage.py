import pygame
import sys

screen = pygame.display.set_mode((1080, 620))  # resizable not added
screen_w, screen_h = pygame.display.get_surface().get_size()
big_logo = pygame.image.load('images/UNDEAD UPRISING.png')


def display_start_menu():
    font = pygame.font.SysFont('consolas', 25)
    screen.blit(big_logo, ((screen_w - 800) / 2, screen_h - 550))
    instructions = font.render('Pick your character', True, (255, 255, 255))
    screen.blit(instructions,
                (screen_w / 2 - instructions.get_width() / 2, screen_h / 2 - instructions.get_height() / 2 - 100))
    # mouse = pygame.mouse.get_pos()
    border()
    show_all_char()
    start_button()
    pygame.display.update()


def start_button():
    start_text = pygame.image.load('images/START.png')
    font = pygame.font.SysFont('Retro', 25, bold=True)
    pygame.draw.rect(screen, (255, 0, 255), [screen_w / 2 - 150 / 2 - 5, 515 - 5, 160, 50])
    # pygame.draw.rect(screen, (0, 255, 255), [screen_w / 2 - 150 / 2, 515, 150, 40])
    # start_text = font.render('START', True, (0, 0, 0))
    # screen.blit(start_text, (screen_w / 2 - 150 / 2 + start_text.get_width() / 2, 515 + start_text.get_height() / 2, 150, 40))
    screen.blit(start_text, (screen_w / 2 - 100 / 2, screen_h - 100))


def border():
    pygame.draw.rect(screen, (255, 255, 255), [screen_w / 2 - 700 / 2, screen_h / 2 - 50, 700, 200])
    pygame.draw.rect(screen, (0, 0, 0), [(screen_w / 2 - 350 + 25), screen_h / 2 - 25, 650, 150])


# All Characters
def show_all_char():
    redchar()
    orangechar()
    yellowchar()
    bluechar()
    purplechar()
    pinkchar()


def redchar():
    red_char = pygame.image.load('images/john.png')
    screen.blit(red_char, (255, 325))


def orangechar():
    orange_char = pygame.image.load('images/swift.png')
    screen.blit(orange_char, (355, 325))


def yellowchar():
    yellow_char = pygame.image.load('images/john.png')
    screen.blit(yellow_char, (455, 325))


def bluechar():
    blue_char = pygame.image.load('images/swift.png')
    screen.blit(blue_char, (555, 325))


def purplechar():
    purple_char = pygame.image.load('images/john.png')
    screen.blit(purple_char, (655, 325))


def pinkchar():
    pink_char = pygame.image.load('images/swift.png')
    screen.blit(pink_char, (755, 325))
