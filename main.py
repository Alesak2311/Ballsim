import pygame
from tools import quit_game, draw_screen, blit_text_center, draw_angle_indicator
from ball import Ball
from wall import Wall, Hoop
from physics import gravity, push_ball

WIDTH = 800
HEIGHT = 800

clock = pygame.time.Clock()


def choose_angle(window, wall_list, hoop, ball):
    angle = 360
    ascending = False

    done = False
    while not done:
        clock.tick(60)

        draw_screen(window, wall_list, hoop, ball)
        draw_angle_indicator(window, ball, angle)

        if ascending:
            angle += 1
            if angle >= 360:
                ascending = False
        else:
            angle -= 1
            if angle <= 270:
                ascending = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    done = True
                    break

    return angle


def check_hoop(window, hoop, ball):
    if ball.detect_hoop(hoop) is not None:
        while True:
            blit_text_center(window, "Score!")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()


def simulation(window, wall_list, hoop, ball):
    while True:
        clock.tick(60)

        gravity(ball)
        ball.update_position(wall_list)

        check_hoop(window, hoop, ball)

        draw_screen(window, wall_list, hoop, ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    push_ball(ball)


def main():
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    wall_list = [Wall((20, 20), (WIDTH - 20, 20)), Wall((WIDTH - 20, 20), (WIDTH - 20, HEIGHT - 20)),
                 Wall((WIDTH - 20, HEIGHT - 20), (20, HEIGHT - 20)), Wall((20, HEIGHT - 20), (20, 20)),
                 Wall((WIDTH - 50, 300), (WIDTH - 20, 300)), Wall((WIDTH - 50, 200), (WIDTH - 50, 350)),
                 Wall((WIDTH - 70, 290), (WIDTH - 50, 290))]

    ball = Ball()
    hoop = Hoop((WIDTH - 120, 300), (WIDTH - 70, 300), wall_list)

    choose_angle(window, wall_list, hoop, ball)

    while True:
        simulation(window, wall_list, hoop, ball)


if __name__ == "__main__":
    main()
