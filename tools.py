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
        pygame.draw.line(window, WHITE, wall.point_a, wall.point_b, 5)

    window.blit(ball.sprite, ball.position)

    pygame.display.update()
