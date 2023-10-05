import pygame
import sys
import characters

screen = pygame.display.set_mode((1080, 620))  # resizable not added
screen_w, screen_h = pygame.display.get_surface().get_size()
big_logo = pygame.image.load('images/UNDEAD UPRISING.png')
bg = pygame.image.load('images/bg_earth.png')

def display_start_menu():
    screen.blit(bg, (0, 0))
    font = pygame.font.SysFont('consolas', 25)
    screen.blit(big_logo, ((screen_w - 800) / 2, screen_h - 550))
    instructions = font.render('Pick your character', True, (255, 255, 255))
    screen.blit(instructions, (screen_w / 2 - instructions.get_width() / 2, screen_h / 2 - instructions.get_height() / 2 - 100))
    mouse = pygame.mouse.get_pos()
    border()
    show_all_char()
    start_button()
    pygame.display.update()


def start_button():
    start_text = pygame.image.load('images/START.png')
    font = pygame.font.SysFont('Retro', 25, bold=True)
    # pygame.draw.rect(screen, (255, 0, 255), [screen_w / 2 - 150 / 2 - 5, 515 - 5, 160, 50])
    # pygame.draw.rect(screen, (0, 255, 255), [screen_w / 2 - 150 / 2, 515, 150, 40])
    # start_text = font.render('START', True, (0, 0, 0))
    # screen.blit(start_text, (screen_w / 2 - 150 / 2 + start_text.get_width() / 2, 515 + start_text.get_height() / 2, 150, 40))
    screen.blit(start_text, (screen_w / 2 - 100 / 2 - 20, screen_h - 120))



def border():
    pygame.draw.rect(screen, (255, 255, 255), [screen_w / 2 - 700 / 2, screen_h / 2 - 50, 700, 200])
    pygame.draw.rect(screen, (0, 0, 0), [(screen_w / 2 - 350 + 25), screen_h / 2 - 25, 650, 150])


# All Characters
def show_all_char():
    screen.blit(characters.John.char_img, (255, 325))
    screen.blit(characters.Tony.char_img, (355, 325))
    screen.blit(characters.Swift.char_img, (455, 325))
    screen.blit(characters.Quinn.char_img, (555, 325))
    screen.blit(characters.Theresa.char_img, (655, 325))
    screen.blit(characters.Jekyll.char_img, (755, 325))

