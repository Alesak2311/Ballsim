import pygame
import sys

BG_COLOR = (50, 50, 50)
WHITE = (255, 255, 255)

pygame.font.init()
MAIN_FONT = pygame.font.SysFont("consolas", 22)


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


def draw_angle_indicator(window, ball, angle):
    start_pos = (ball.x + 10, ball.y + 10)
    angle_vector = pygame.math.Vector2(0, 0)
    angle_vector.from_polar((100, angle))
    end_pos = (start_pos[0] + angle_vector.x, start_pos[1] + angle_vector.y)

    pygame.draw.line(window, WHITE, start_pos, end_pos, 5)
    pygame.display.update()


def blit_text_center(window, string, font=MAIN_FONT):
    text = font.render(string, True, WHITE)

    text_pos = ((window.get_width() - text.get_width()) / 2,
                (window.get_height() - text.get_height()) / 2)

    window.blit(text, text_pos)
    pygame.display.update()


def power_indicator(window, power):
    window_w = window.get_width()
    window_h = window.get_height()

    text = MAIN_FONT.render("POWER INDICATOR", True, WHITE)
    window.blit(text, (window_w - 340, window_h - 70))

    pygame.draw.rect(window, WHITE, pygame.Rect(window_w - 340, window_h - 50, 300, 10), 1)
    pygame.draw.rect(window, WHITE, pygame.Rect(window_w - 340, window_h - 50, power * 7.5, 10))

    pygame.display.update()
