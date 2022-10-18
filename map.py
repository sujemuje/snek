import arcade
from settings import *


class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 100, 0)

    def on_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.a, self.a, self.color)


class Map:
    def __init__(self):
        self.obstacles: list[Obstacle] = []

    def on_draw(self):
        for obstacle in self.obstacles:
            obstacle.on_draw()
        self.draw_grid()

    def draw_grid(self):
        for x in range(BLOCK_SIZE, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE):
            arcade