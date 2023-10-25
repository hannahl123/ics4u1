# Import libraries and character code
import pygame
import sys
import ctypes
import characters

# Screen Settings - Setting size of screen and setting variables to access width and height of screen
true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
screen = pygame.display.set_mode(true_res, pygame.FULLSCREEN)
screen_w, screen_h = true_res[0], true_res[1]

# Default character position - center of screen
charX = screen_w / 2 - 30
charY = screen_h / 2 - 30
charX_change = 0
charY_change = 0

# Function to play the game
def play(char):
    global charX, charY, charX_change, charY_change
    # border code
    if charX <= 0:
        charX = 0
    if charX >= screen_w - 50:
        charX = screen_w - 50
    if charY <= 0:
        charY = 0
    if charY >= screen_h - 60:
        charY = screen_h - 60
    if char == 'John':
        screen.blit(characters.John.bg_img, (0, 0))
        # Monitors events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # sets the variable to False, which breaks the while loop
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    print("Left arrow is pressed")
                    charX_change = -3
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print("Right arrow is pressed")
                    charX_change = 3
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    print("Up arrow is pressed")
                    charY_change = -3
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print("Down arrow is pressed")
                    charY_change = 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print("Keystroke has been released")
                    charX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print("Keystroke has been released")
                    charY_change = 0
                if event.key == pygame.K_c:
                    print("Keystroke has been released")
        charX += charX_change
        charY += charY_change
        screen.blit(characters.John.char_img, (charX, charY))
    elif char == 'Tony':
        screen.blit(characters.Tony.bg_img, (0, 0))
        # Monitors events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # sets the variable to False, which breaks the while loop
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    print("Left arrow is pressed")
                    charX_change = -3
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print("Right arrow is pressed")
                    charX_change = 3
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    print("Up arrow is pressed")
                    charY_change = -3
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print("Down arrow is pressed")
                    charY_change = 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print("Keystroke has been released")
                    charX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print("Keystroke has been released")
                    charY_change = 0
                if event.key == pygame.K_c:
                    print("Keystroke has been released")
        charX += charX_change
        charY += charY_change
        screen.blit(characters.Tony.char_img, (charX, charY))
    elif char == 'Swift':
        screen.blit(characters.Swift.bg_img, (0, 0))
        # Monitors events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # sets the variable to False, which breaks the while loop
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    print("Left arrow is pressed")
                    charX_change = -3
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print("Right arrow is pressed")
                    charX_change = 3
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    print("Up arrow is pressed")
                    charY_change = -3
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print("Down arrow is pressed")
                    charY_change = 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print("Keystroke has been released")
                    charX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print("Keystroke has been released")
                    charY_change = 0
                if event.key == pygame.K_c:
                    print("Keystroke has been released")
        charX += charX_change
        charY += charY_change
        screen.blit(characters.Swift.char_img, (charX, charY))
    elif char == 'Quinn':
        screen.blit(characters.Quinn.bg_img, (0, 0))
        # Monitors events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # sets the variable to False, which breaks the while loop
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    print("Left arrow is pressed")
                    charX_change = -3
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print("Right arrow is pressed")
                    charX_change = 3
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    print("Up arrow is pressed")
                    charY_change = -3
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print("Down arrow is pressed")
                    charY_change = 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print("Keystroke has been released")
                    charX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print("Keystroke has been released")
                    charY_change = 0
                if event.key == pygame.K_c:
                    print("Keystroke has been released")
        charX += charX_change
        charY += charY_change
        screen.blit(characters.Quinn.char_img, (charX, charY))
    elif char == 'Theresa':
        screen.blit(characters.Theresa.bg_img, (0, 0))
        # Monitors events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # sets the variable to False, which breaks the while loop
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    print("Left arrow is pressed")
                    charX_change = -3
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print("Right arrow is pressed")
                    charX_change = 3
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    print("Up arrow is pressed")
                    charY_change = -3
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print("Down arrow is pressed")
                    charY_change = 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print("Keystroke has been released")
                    charX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print("Keystroke has been released")
                    charY_change = 0
                if event.key == pygame.K_c:
                    print("Keystroke has been released")
        charX += charX_change
        charY += charY_change
        screen.blit(characters.Theresa.char_img, (charX, charY))
    elif char == 'Jekyll':
        screen.blit(characters.Jekyll.bg_img, (0, 0))
        # Monitors events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # sets the variable to False, which breaks the while loop
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    print("Left arrow is pressed")
                    charX_change = -3
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print("Right arrow is pressed")
                    charX_change = 3
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    print("Up arrow is pressed")
                    charY_change = -3
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print("Down arrow is pressed")
                    charY_change = 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print("Keystroke has been released")
                    charX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print("Keystroke has been released")
                    charY_change = 0
                if event.key == pygame.K_c:
                    print("Keystroke has been released")
        charX += charX_change
        charY += charY_change
        screen.blit(characters.Jekyll.char_img, (charX, charY))
    pygame.display.update()


def health_bar():
    pygame.draw.rect(screen, (41, 237, 255), [20, 20, 200, 30])
