# Import libraries and pages of code used in game
import pygame
import sys
import ctypes
import startpage
import game
import tutorial

# Initialize the screen
pygame.init()

# Screen Settings - Setting size of screen and setting variables to access width and height of screen
true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
screen = pygame.display.set_mode(true_res, pygame.FULLSCREEN)
screen_w, screen_h = true_res[0], true_res[1]

# Game Details - Loading and Setting the Name and Logos of the Game
pygame.display.set_caption("Undead Uprising")
logo = pygame.image.load('images/test_char.png')
pygame.display.set_icon(logo)
big_logo = pygame.image.load('images/UNDEAD UPRISING.png')

# Keeping track of the state of the game - start_menu, game_play, or tutorial
game_state = "start_menu"
character = "John"  # default character

# Variable to keep the game on, when changed to False then exit
running = True
# Forever Loop of Game until user exits
while running:
    screen.fill((0, 0, 0)) # default black background
    mouse = pygame.mouse.get_pos() # gets the location of the mouse cursor
    for event in pygame.event.get(): # detect when an event is happening in the game (e.g. mouse click, key pressed, etc.)
        # detects if the exit button is clicked or the [Q] key is clicked
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            # sets the variable to False, which breaks the while loop
            running = False
        # if the mouse is clicked in the start menu, check where the cursor is
        if game_state == 'start_menu' and event.type == pygame.MOUSEBUTTONDOWN:
            # checks which character the mouse cursor is on
            if screen_w * 2 / 7 <= mouse[0] <= screen_w * 2 / 7 + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
                # if John is clicked, state in the console and set the character to John
                character = "John"
                print('John is picked')
            elif screen_w * 2.5 / 7 <= mouse[0] <= screen_w * 2.5 / 7 + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
                # if Tony is clicked, state in the console and set the character to Tony
                character = "Tony"
                print('Tony is picked')
            elif screen_w * 3 / 7 <= mouse[0] <= screen_w * 3 / 7 + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
                # if Swift is clicked, state in the console and set the character to Swift
                character = "Swift"
                print('Swift is picked')
            elif screen_w * 3.5 / 7 <= mouse[0] <= screen_w * 3.5 / 7 + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
                # if Quinn is clicked, state in the console and set the character to Quinn
                character = "Quinn"
                print('Quinn is picked')
            elif screen_w * 4 / 7 <= mouse[0] <= screen_w * 4 / 7 + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
                # if Theresa is clicked, state in the console and set the character to Theresa
                character = "Theresa"
                print('Theresa is picked')
            elif screen_w * 4.5 / 7 <= mouse[0] <= screen_w * 4.5 / 7 + 50 and screen_h / 2 + 20 <= mouse[1] <= screen_h / 2 + 80:
                # if Jekyll is clicked, state in the console and set the character to Jekyll
                character = "Jekyll"
                print('Jekyll is picked')
            # checks if the start button is clicked
            elif screen_w / 2 - 200 <= mouse[0] <= screen_w / 2 - 50 and screen_h - 140 <= mouse[1] <= screen_h - 80:
                # if the start button was pressed, set the game state to game_play, which executes the next part of the game
                game_state = "game_play"
            # checks if the tutorial button is clicked
            # if 200 <= mouse[0] <= 400 and screen_h - 120 <= mouse[1] <= screen_h - 120 + 66:
                # game_state = "tutorial" # For the tutorial button when pressed by the mouse            
    # checks game state and executes the part of the game according to the variable
    if game_state == "start_menu":
        # executes start menu screen
        startpage.display_start_menu()
    elif game_state == 'game_play':
        # executes game play screen
        game.play(character)
    elif game_state == 'tutorial':
        # executes tutorial screen
        tutorial.intro()
    pygame.display.flip()
