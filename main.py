import pygame
from tools import quit_game, draw_screen
from ball import Ball
from wall import Wall
from physics import gravity

WIDTH = 800
HEIGHT = 800

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ball = Ball()

wall_list = [Wall((20, 20), (WIDTH - 20, 20)), Wall((WIDTH - 20, 20), (WIDTH - 20, HEIGHT - 20)),
             Wall((WIDTH - 20, HEIGHT - 20), (20, HEIGHT - 20)), Wall((20, HEIGHT - 20), (20, 20))]

while True:
    clock.tick(30)

    gravity(ball)
    ball.update_position(wall_list)

    draw_screen(window, wall_list, ball)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
