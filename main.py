import sys
import arcade
import settings as stg
from snake import Snake
from map import Map


class Game(arcade.Window):
    def __init__(self, w, h, title):
        super().__init__(w, h, title)

        self.snake: Snake = None
        self.map: Map = None
        self.key_inputs = []

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.map = Map()
        self.snake = Snake(self.map)

    def on_update(self, dt: float):
        self.snake.on_update(dt)

    def on_draw(self):
        self.clear()
        self.map.on_draw()
        self.snake.on_draw()

    def on_key_press(self, key, keymod):
        self.key_inputs.append(key)

        if key == arcade.key.ESCAPE:
            arcade.exit()
        self.snake.on_key_press(key, keymod)
        self.key_check()

    def on_key_release(self, key, keymod):
        self.key_inputs.remove(key)

        self.snake.on_key_release(key, keymod)
        self.key_check()

    def key_check(self):
        self.snake.key_check(self.key_inputs)



def main():
    """ Main function """
    game = Game(stg.SCREEN_WIDTH, stg.SCREEN_HEIGHT, stg.SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
