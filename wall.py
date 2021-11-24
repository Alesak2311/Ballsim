import pygame

WHITE = (255, 255, 255)
GREY = (100, 100, 100)
RED = (255, 0, 0)


class Wall:
    def __init__(self, point_a, point_b, color=WHITE):
        self.x1, self.y1 = min(point_a, point_b)
        self.x2, self.y2 = max(point_a, point_b)

        self.normal_vector = pygame.Vector2(self.x2 - self.x1, self.y2 - self.y1).rotate(90)

        self.surface = pygame.Surface((max(5, self.x2 - self.x1), max(5, self.y2 - self.y1)))
        self.surface.fill(color)

        self.mask = pygame.mask.from_surface(self.surface)


class Hoop:
    def __init__(self, point_a, point_b, wall_list):
        self.x1, self.y1 = min(point_a, point_b)
        self.x2, self.y2 = max(point_a, point_b)

        wall_list.append(Wall(point_a, (point_a[0], point_a[1] - 10), RED))
        wall_list.append(Wall(point_b, (point_b[0], point_b[1] - 10), RED))

        self.surface = pygame.Surface((max(5, self.x2 - self.x1 - 5), max(5, self.y2 - self.y1)))
        self.surface.fill(GREY)
