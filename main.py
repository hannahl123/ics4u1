import pygame
import sys
import startpage
import game

pygame.init()

# Screen Settings
screen = pygame.display.set_mode((1080, 620))  # resizable not added
screen_w, screen_h = pygame.display.get_surface().get_size()

# Game Details
pygame.display.set_caption("Undead Uprising")
icon = pygame.image.load('images/test_char.png')
pygame.display.set_icon(icon)
big_logo = pygame.image.load('images/UNDEAD UPRISING.png')

game_state = "start_menu"
running = True
while running:
    character = "john" # default
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            running = False
        if game_state == 'start_menu':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 470 <= mouse[0] <= 620 and screen_h - 120 <= mouse[1] <= screen_h - 120 + 66:
                    character = ""
                    game_state = "game_play"
                if 470 <= mouse[0] <= 620 and screen_h - 120 <= mouse[1] <= screen_h - 120 + 66:
                    game_state = "game_play"
    screen.fill((0, 0, 0))
    if game_state == "start_menu":
        startpage.display_start_menu()
    if game_state == 'game_play':
        game.play()
    if game_state == 'tutorial':
        print()
        # tutorial
    pygame.display.update()
