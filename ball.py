import pygame

RED = (255, 0, 0)

BALL_RADIUS = 10
BALL_SPRITE = pygame.image.load("assets/ball.png")


class Ball:
    def __init__(self):
        self.x, self.y = (500, 500)
        self.speed = pygame.math.Vector2(5, 5)
        self.sprite = BALL_SPRITE

    def update_position(self, wall_list):
        new_x = self.x + self.speed.x
        new_y = self.y + self.speed.y

        collision = self.detect_collision(wall_list, new_x, new_y)

        if collision is None:
            self.x = new_x
            self.y = new_y
        else:
            self.speed = self.speed.reflect(collision)
            self.x += self.speed.x
            self.y += self.speed.y

    def detect_collision(self, wall_list, ball_x, ball_y):
        ball_mask = pygame.mask.from_surface(self.sprite)
        for wall in wall_list:
            poi = ball_mask.overlap(wall.mask, (int(wall.x1 - ball_x), int(wall.y1 - ball_y)))
            if poi is not None:
                return wall.normal_vector
        return
