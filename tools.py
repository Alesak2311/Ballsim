import pygame
import sys

BG_COLOR = (50, 50, 50)
WHITE = (255, 255, 255)


def quit_game():
    pygame.quit()
    sys.exit()


def draw_screen(window, wall_list, hoop, ball):
    window.fill(BG_COLOR)

    for wall in wall_list:
        window.blit(wall.surface, (wall.x1, wall.y1))

    window.blit(hoop.surface, (hoop.x1 + 5, hoop.y1 - 10))

    window.blit(ball.sprite, (ball.x, ball.y))

    pygame.display.update()
