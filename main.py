import sys

import arcade
from snake import Snake


SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE = 800, 600, 'snek'


class Game(arcade.Window):
    def __init__(self, w, h, title):
        super().__init__(w, h, title)

        self.snake: Snake() = None
        self.key_inputs = []

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.snake = Snake()

    def on_update(self, dt: float):
        self.clear()
        self.snake.on_update(dt)

    def on_draw(self):
        self.snake.on_draw()

    def on_key_press(self, key, keymod):
        self.key_inputs.append(key)

        if key == arcade.key.ESCAPE:
            arcade.exit()
        self.snake.on_key_press(key, keymod)
        self.key_check()

    def on_key_release(self, key, keymod):
        self.key_inputs.remove(key)

        self.key_check()

    def key_check(self):
        self.snake.key_check(self.key_inputs)


def main():
    """ Main function """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
