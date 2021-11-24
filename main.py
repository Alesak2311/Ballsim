import pygame
from tools import quit_game, draw_screen
from ball import Ball
from wall import Wall, Hoop
from physics import gravity, push_ball

WIDTH = 800
HEIGHT = 800

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

wall_list = [Wall((20, 20), (WIDTH - 20, 20)), Wall((WIDTH - 20, 20), (WIDTH - 20, HEIGHT - 20)),
             Wall((WIDTH - 20, HEIGHT - 20), (20, HEIGHT - 20)), Wall((20, HEIGHT - 20), (20, 20)),
             Wall((WIDTH - 50, 300), (WIDTH - 20, 300)), Wall((WIDTH - 50, 200), (WIDTH - 50, 350)),
             Wall((WIDTH - 70, 290), (WIDTH - 50, 290))]

ball = Ball()
hoop = Hoop((WIDTH - 120, 300), (WIDTH - 70, 300), wall_list)

while True:
    clock.tick(60)

    gravity(ball)
    ball.update_position(wall_list)

    draw_screen(window, wall_list, hoop, ball)

    if ball.detect_hoop(hoop) is not None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                push_ball(ball)
