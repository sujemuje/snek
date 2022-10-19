import arcade
from settings import *


class Segment:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.a = BLOCK_SIZE - SEGMENT_GAP
        self.color = (0, 0, 0)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def on_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.a, self.a, self.color)


class Snake:
    def __init__(self, map):
        self.head = Segment()
        self.head.color = (50, 50, 50)
        self.tail: list[Segment] = [self.head]
        self.vel = BLOCK_SIZE
        self.dir = (self.vel, 0)
        self.dir_keys = [arcade.key.W, arcade.key.A, arcade.key.S, arcade.key.D]
        self.dead = False
        self.map = map

        self.counter = 0
        self.counter_lim = [.8, .2, .1]
        self.counter_lim_switch = 0
        self.boost = False

    def move(self):
        """
        Function responsible for moving snake and checking legibility for movement, and reporting a loss if struck
        """

        """New snake's position"""
        new_x = self.head.x + self.dir[0]
        new_y = self.head.y + self.dir[1]
        # repositioning if screen transition occurs
        if not 0 <= new_x <= SCREEN_WIDTH:
            if new_x < 0:
                new_x += SCREEN_WIDTH + self.vel
            else:
                new_x -= SCREEN_WIDTH + self.vel

        elif not 0 <= new_y <= SCREEN_HEIGHT:
            if new_y < 0:
                new_y += SCREEN_HEIGHT + self.vel
            else:
                new_y -= SCREEN_HEIGHT + self.vel

        """Checking collisions"""
        # collision with any blocks on the map
        for obstacle in self.map.obstacles:
            if new_x == obstacle.x and new_y == obstacle.y:
                self.dead = True
                return

        # collision with its own body
        for i in range(1, len(self.tail)):
            if self.tail[i].x == new_x and self.tail[i].y == new_y:
                if i < len(self.tail) - 1:
                    self.dead = True
                    return

        """checking if snake ate an apple"""
        if new_x == self.map.apple.x and new_y == self.map.apple.y:
            self.tail.append(Segment(self.tail[-1].x, self.tail[-1].y))
            self.map.respawn_apple()

        """Moving snake"""
        # tail (backwards)
        for i in range(len(self.tail) - 1, 0, -1):
            self.tail[i].set_position(self.tail[i - 1].x, self.tail[i - 1].y)
        # head
        self.head.set_position(new_x, new_y)

    def on_update(self, dt: float):
        self.counter += dt
        if self.counter >= self.counter_lim[self.counter_lim_switch]:
            self.counter -= self.counter_lim[self.counter_lim_switch]

            self.move()
            if self.dead:
                self.head.color = (150, 0, 0)

    def on_draw(self):
        for segment in self.tail:
            segment.on_draw()

    def on_key_press(self, key, keymod):
        if key == arcade.key.Z:
            self.tail.append(Segment())
        elif key == arcade.key.LSHIFT:
            self.boost = True
            self.counter *= self.counter_lim[self.counter_lim_switch + 1] / self.counter_lim[self.counter_lim_switch]
        elif key in self.dir_keys:
            self.counter = self.counter_lim[1 if not self.boost else 2]

    def on_key_release(self, key, keymod):
        if key == arcade.key.LSHIFT:
            self.boost = False
            self.counter *= self.counter_lim[self.counter_lim_switch - 1] / self.counter_lim[self.counter_lim_switch]

    def key_check(self, key_inputs):
        self.counter_lim_switch = 0

        if self.boost:
            self.counter_lim_switch += 1
        if any(x in key_inputs for x in self.dir_keys):
            self.counter_lim_switch += 1

        for key in key_inputs[::-1]:
            if key == arcade.key.D:
                self.dir = (self.vel, 0)
                break
            elif key == arcade.key.A:
                self.dir = (-self.vel, 0)
                break
            elif key == arcade.key.W:
                self.dir = (0, self.vel)
                break
            elif key == arcade.key.S:
                self.dir = (0, -self.vel)
                break
