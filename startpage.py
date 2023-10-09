import pygame
import sys
import characters

# Screen Settings - Setting size of screen and setting variables to access width and height of screen
screen = pygame.display.set_mode((1080, 620))  # resizable not added
screen_w, screen_h = pygame.display.get_surface().get_size()

# Large logo of title and background of start menu
big_logo = pygame.image.load('images/UNDEAD UPRISING.png')
bg = pygame.image.load('images/backgrounds/bg_earth.png')

# Executes the start menu page
def display_start_menu():
    screen.blit(bg, (0, 0)) # displays the background
    font = pygame.font.SysFont('consolas', 25) # sets the font family and font size
    screen.blit(big_logo, ((screen_w - 800) / 2, screen_h - 550)) # displays the big title
    text = font.render('Pick your character', True, (255, 255, 255)) # sets the instructions text
    screen.blit(text, (screen_w / 2 - text.get_width() / 2, screen_h / 2 - text.get_height() / 2 - 100)) # displays the instructions text
    border() # displays the border to showcase characters
    show_all_char() # displays all 6 characters
    start_button() # displays the start button
    pygame.display.update() # updates the screen


# Displays the start button
def start_button():
    start_text = pygame.image.load('images/start_new.png')
    screen.blit(start_text, (screen_w / 2 - 80, screen_h - 120))

# Displays the border
def border():
    pygame.draw.rect(screen, (255, 255, 255), [screen_w / 2 - 700 / 2, screen_h / 2 - 50, 700, 200])
    pygame.draw.rect(screen, (0, 0, 0), [screen_w / 2 - 350 + 25, screen_h / 2 - 25, 650, 150])


# Displays all characters on the start menu
def show_all_char():
    screen.blit(characters.John.char_img, (255, 325))
    screen.blit(characters.Tony.char_img, (355, 325))
    screen.blit(characters.Swift.char_img, (455, 325))
    screen.blit(characters.Quinn.char_img, (555, 325))
    screen.blit(characters.Theresa.char_img, (655, 325))
    screen.blit(characters.Jekyll.char_img, (755, 325))
