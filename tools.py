import pygame
import sys

GREY = (50, 50, 50)
WHITE = (255, 255, 255)


def quit_game():
    pygame.quit()
    sys.exit()


def draw_screen(window, wall_list, ball):
    window.fill(GREY)

    for wall in wall_list:
        window.blit(wall.surface, (wall.x1, wall.y1))

    window.blit(ball.sprite, (ball.x, ball.y))

    pygame.display.update()
