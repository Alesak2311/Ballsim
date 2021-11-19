import pygame

RED = (255, 0, 0)

BALL_RADIUS = 10
BALL_SPRITE = pygame.image.load("assets/ball.png")


class Ball:
    def __init__(self):
        self.position = (400, 400)
        self.speed = pygame.math.Vector2(0, 0)
        self.sprite = BALL_SPRITE
