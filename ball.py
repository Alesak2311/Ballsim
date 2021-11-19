import pygame

RED = (255, 0, 0)

BALL_SPRITE = pygame.draw.circle(pygame.Surface((10, 10)), RED, (5, 5), 5)


class Ball:
    def __init__(self):
        self.position = (400, 400)
        self.speed = pygame.math.Vector2(0, 0)
        self.sprite = BALL_SPRITE
