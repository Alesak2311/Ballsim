import pygame
import sys

GREY = (50, 50, 50)


def quit_game():
    pygame.quit()
    sys.exit()


def draw_screen(window, wall_list, ball):
    window.fill(GREY)

    pygame.display.update()
