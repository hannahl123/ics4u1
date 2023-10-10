# Import libraries and pages of code used in game
import pygame
import sys
import startpage
import game
import tutorial

# Initialize the screen
pygame.init()

# Screen Settings - Setting size of screen and setting variables to access width and height of screen
screen = pygame.display.set_mode((1080, 620))  # resizable not added
screen_w, screen_h = pygame.display.get_surface().get_size()

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
        # checks if the game state is start menu and mouse is clicked
        # if the mouse is clicked in the start menu, check where the cursor is
        if game_state == 'start_menu' and event.type == pygame.MOUSEBUTTONDOWN:
                # checks which character the mouse cursor is on
                if 260 <= mouse[0] <= 260+40 and 325 <= mouse[1] <= 325 + 60:
                    # if John is clicked, state in the console and set the character to John
                    character = "John"
                    print('John is picked')
                if 360 <= mouse[0] <= 360+40 and 325 <= mouse[1] <= 325 + 60:
                    # if Tony is clicked, state in the console and set the character to Tony
                    character = "Tony"
                    print('Tony is picked')
                if 460 <= mouse[0] <= 460+40 and 325 <= mouse[1] <= 325 + 60:
                    # if Swift is clicked, state in the console and set the character to Swift
                    character = "Swift"
                    print('Swift is picked')
                if 560 <= mouse[0] <= 560+40 and 325 <= mouse[1] <= 325 + 60:
                    # if Quinn is clicked, state in the console and set the character to Quinn
                    character = "Quinn"
                    print('Quinn is picked')
                if 660 <= mouse[0] <= 660+40 and 325 <= mouse[1] <= 325 + 60:
                    # if Theresa is clicked, state in the console and set the character to Theresa
                    character = "Theresa"
                    print('Theresa is picked')
                if 760 <= mouse[0] <= 760+40 and 325 <= mouse[1] <= 325 + 60:
                    # if Jekyll is clicked, state in the console and set the character to Jekyll
                    character = "Jekyll"
                    print('Jekyll is picked')
                # checks if the mouse cursor is on the start button
                if 460 <= mouse[0] <= 610 and 500 <= mouse[1] <= 550:
                    # if the start button was pressed, set the game state to game_play, which executes the next part of the game
                    game_state = "game_play"
    # checks game state and executes the part of the game according to the variable
    if game_state == "start_menu":
        # executes start menu screen
        startpage.display_start_menu()
    if game_state == 'game_play':
        # executes game play screen
        game.play(character)
    if game_state == 'tutorial':
        # executes tutorial screen
        tutorial.intro()
    pygame.display.update()
