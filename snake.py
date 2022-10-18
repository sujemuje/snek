import arcade


class Segment:
    def __init__(self):
        self.x = 0
        self.y = 0

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def on_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, 20, 20, (0, 0, 0))


class Snake:
    def __init__(self):
        self.head = Segment()
        self.tail: list[Segment] = [self.head]
        self.vel = 24
        self.dir = (self.vel, 0)

        self.counter = 0
        self.counter_lim = .8

    def move(self):
        for i in range(1, len(self.tail)):
            if self.tail[i].x == self.head.x + self.dir[0] and self.tail[i].y == self.head.y + self.dir[1]:
                if i < len(self.tail) - 1:
                    break
        else:
            for i in range(len(self.tail) - 1, 0, -1):
                self.tail[i].set_position(self.tail[i - 1].x, self.tail[i - 1].y)

            self.head.set_position(self.head.x + self.dir[0], self.head.y + self.dir[1])

    def on_update(self, dt: float):
        self.counter += dt
        if self.counter >= self.counter_lim:
            self.counter -= self.counter_lim

            self.move()

    def on_draw(self):
        for segment in self.tail:
            segment.on_draw()

    def on_key_press(self, key, keymod):
        if key == arcade.key.Z:
            self.tail.append(Segment())

    def key_check(self, key_inputs):
        for key in key_inputs[::-1]:
            if key == arcade.key.S or key == arcade.key.W or key == arcade.key.A or key == arcade.key.D:
                if self.counter_lim != .15:
                    self.counter_lim = .15
                    self.counter = .15

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
        else:
            if self.counter_lim != .8:
                self.counter_lim = .8
