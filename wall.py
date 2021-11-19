import pygame

WHITE = (255, 255, 255)


class Wall:
    def __init__(self, point_a, point_b):
        self.x1, self.y1 = min(point_a, point_b)
        self.x2, self.y2 = max(point_a, point_b)
        self.vector = pygame.Vector2(self.x2 - self.x1, self.y2 - self.y1)
        self.surface = pygame.Surface((max(5, self.x2 - self.x1), max(5, self.y2 - self.y1)))
        self.surface.fill(WHITE)
        self.mask = pygame.mask.from_surface(self.surface)
