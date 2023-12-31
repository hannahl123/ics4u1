'''
Code for old start button - DO NOT REMOVE
# font = pygame.font.SysFont('Retro', 25, bold=True)
# pygame.draw.rect(screen, (255, 0, 255), [screen_w / 2 - 150 / 2 - 5, 515 - 5, 160, 50])
# pygame.draw.rect(screen, (0, 255, 255), [screen_w / 2 - 150 / 2, 515, 150, 40])
# start_text = font.render('START', True, (0, 0, 0))
# screen.blit(start_text, (screen_w / 2 - 150 / 2 + start_text.get_width() / 2, 515 + start_text.get_height() / 2, 150, 40))

Code for re-centreing - DO NOT REMOVE

# Re-centres the character to the middle of the screen
if event.key == pygame.K_c:
    print("Character is re-centred")
    charX = screen_w / 2 - 30
    charY = screen_h / 2 - 30

'''
import os
import pygame as pg
from random import *
# It is used as a library

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")


def show(image): # Shows surface
    screen = pg.display.get_surface()
    screen.fill((255, 255, 255))

    screen.blit(image, (0, 0))
    pg.display.flip()


def main(): # Reacts on window closing.
    pg.init()

    pg.display.set_mode((255, 255))
    surface = pg.Surface((255, 255))

    pg.display.flip()
    while 1:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                brk = 0
                pg.display.quit()
def animate(pixels): # Animation function.pixels is array of arrays as [x, y, (r,g,b)]
    global surface
    ar = pg.PixelArray(surface)
    for x, y, color in pixels:
        ar[x, y] = color
    del ar
    show(STR.jpg)
main()
