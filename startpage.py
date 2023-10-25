import pygame
import sys
import ctypes
import characters

# Screen Settings - Setting size of screen and setting variables to access width and height of screen
true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
screen = pygame.display.set_mode(true_res, pygame.FULLSCREEN)
screen_w, screen_h = true_res[0], true_res[1]

# Large logo of title and background of start menu
big_logo = pygame.image.load('images/UNDEAD UPRISING.png')
bg = pygame.image.load('images/backgrounds/bg_earth.png')
bg = pygame.transform.scale(bg, (screen_w, screen_h))

# Executes the start menu page
def display_start_menu():
    screen.blit(bg, (0, 0)) # displays the background
    mouse = pygame.mouse.get_pos()
    font = pygame.font.SysFont('consolas', 25) # sets the font family and font size
    screen.blit(big_logo, ((screen_w - 800) / 2, 125)) # displays the big title
    text = font.render('Pick your character', True, (255, 255, 255)) # sets the instructions text
    screen.blit(text, (screen_w / 2 - text.get_width() / 2, 250)) # displays the instructions text
    border() # displays the border to showcase characters
    show_all_char() # displays all 6 characters
    buttons() # displays the start button
    pygame.display.update() # updates the screen


# Displays the start button
def buttons():
    tutorial_b = pygame.image.load('images/tutorial_button_test.png')
    tutorial_b = pygame.transform.scale(tutorial_b, (75, 75))
    start_b = pygame.image.load('images/START_button.png')
    start_b = pygame.transform.scale(start_b, (150, 60))
    quit_b = pygame.image.load('images/QUIT_button.png')
    quit_b = pygame.transform.scale(quit_b, (150, 60))
    screen.blit(start_b, (screen_w / 2 - 200, screen_h - 140))
    screen.blit(quit_b, (screen_w / 2 + 50, screen_h - 140))
    screen.blit(tutorial_b, (30, screen_h - 105))

# Displays the border
def border():
    border_image = pygame.image.load('images/border.png')
    screen.blit(border_image, (screen_w / 2 - 350, screen_h / 2 - 50))
    # pygame.draw.rect(screen, (255, 255, 255), [screen_w / 2 - 700 / 2, screen_h / 2 - 50, 700, 200])
    # pygame.draw.rect(screen, (0, 0, 0), [screen_w / 2 - 350 + 25, screen_h / 2 - 25, 650, 150])


# Displays all characters on the start menu
def show_all_char():
    characters.John.show()
    characters.Tony.show()
    characters.Swift.show()
    characters.Quinn.show()
    characters.Theresa.show()
    characters.Jekyll.show()
