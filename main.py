import pygame
from tools import quit_game
from ball import Ball

WIDTH = 800
HEIGHT = 800

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
