import pygame
from tools import quit_game, draw_screen
from ball import Ball

WIDTH = 800
HEIGHT = 800

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ball = Ball()

while True:
    clock.tick(30)

    draw_screen(window, None, ball)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
