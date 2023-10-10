# Import libraries and character code
import pygame
import sys
import characters

# Screen Settings - Setting size of screen and setting variables to access width and height of screen
screen = pygame.display.set_mode((1080, 620))  # resizable not added
screen_w, screen_h = pygame.display.get_surface().get_size()

# Default character position - center of screen
charX = screen_w / 2 - 30
charY = screen_h / 2 - 30
charX_change = 0
charY_change = 0

# Function to play the game
def play(char):
    global charX, charY, charX_change, charY_change
    screen.blit(characters.John.bg_img, (0, 0))
    if char == 'John':
        # screen.blit(characters.John.bg_img, (0, 0))
        # Monitors events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # sets the variable to False, which breaks the while loop
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    print("Left arrow is pressed")
                    charX_change = -1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print("Right arrow is pressed")
                    charX_change = 1
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    print("Up arrow is pressed")
                    charY_change = -1
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print("Down arrow is pressed")
                    charY_change = 1
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
        screen.blit(characters.Tony.char_img, (screen_w / 2 - characters.Tony.char_img.get_width() / 2, 450))
    pygame.display.update()


def health_bar():
    pygame.draw.rect(screen, (41, 237, 255), [20, 20, 200, 30])
