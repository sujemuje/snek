import arcade
import random
from settings import *


class MapEntity:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.a = BLOCK_SIZE - SEGMENT_GAP

    def on_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.a, self.a, self.color)


def draw_grid():
    line_color_main = (0, 50, 0)
    line_color_shadow = (120, 200, 120)

    for x in range(int(BLOCK_SIZE/2) + 2, SCREEN_WIDTH, BLOCK_SIZE):
        arcade.draw_line(x, 0, x, SCREEN_HEIGHT, line_color_shadow, 1)
    for y in range(int(BLOCK_SIZE/2) + 1, SCREEN_HEIGHT, BLOCK_SIZE):
        arcade.draw_line(0, y, SCREEN_WIDTH, y, line_color_shadow, 1)

    for x in range(int(BLOCK_SIZE/2), SCREEN_WIDTH, BLOCK_SIZE):
        arcade.draw_line(x, 0, x, SCREEN_HEIGHT, line_color_main, 2)
    for y in range(int(BLOCK_SIZE/2), SCREEN_HEIGHT, BLOCK_SIZE):
        arcade.draw_line(0, y, SCREEN_WIDTH, y, line_color_main, 2)

    for x in range(int(BLOCK_SIZE/2), SCREEN_WIDTH, BLOCK_SIZE):
        for y in range(int(BLOCK_SIZE/2), SCREEN_HEIGHT, BLOCK_SIZE):
            arcade.draw_rectangle_filled(x + .5, y + .5, 3, 3, arcade.color.AMAZON)


class Map:
    def __init__(self):
        self.obstacles: list[MapEntity] = [MapEntity(5*BLOCK_SIZE, 5*BLOCK_SIZE, (0, 50, 0))]
        self.apple = MapEntity(17*BLOCK_SIZE, 12*BLOCK_SIZE, (150, 0, 0))

    def on_draw(self):
        for obstacle in self.obstacles:
            obstacle.on_draw()
        self.apple.on_draw()
        draw_grid()

    def respawn_apple(self):
        self.apple.x = random.randint(0,SCREEN_WIDTH//BLOCK_SIZE) * BLOCK_SIZE
        self.apple.y = random.randint(0, SCREEN_HEIGHT//BLOCK_SIZE) * BLOCK_SIZE
