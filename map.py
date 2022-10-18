import arcade
from settings import *


class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.a = BLOCK_SIZE - SEGMENT_GAP
        self.color = (0, 50, 0)

    def on_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.a, self.a, self.color)


def draw_grid():
    for x in range(int(BLOCK_SIZE/2), SCREEN_WIDTH, BLOCK_SIZE):
        arcade.draw_line(x, BLOCK_SIZE/2, x, SCREEN_HEIGHT - BLOCK_SIZE/2, (0, 50, 0), 2)
    for y in range(int(BLOCK_SIZE/2), SCREEN_HEIGHT, BLOCK_SIZE):
        arcade.draw_line(BLOCK_SIZE/2, y, SCREEN_WIDTH - BLOCK_SIZE/2, y, (0, 50, 0), 2)


class Map:
    def __init__(self):
        self.obstacles: list[Obstacle] = [Obstacle(5*BLOCK_SIZE, 5*BLOCK_SIZE)]

    def on_draw(self):
        for obstacle in self.obstacles:
            obstacle.on_draw()
        draw_grid()
