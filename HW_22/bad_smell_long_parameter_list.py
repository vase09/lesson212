class Unit:
    def __init__(self, state, speed):
        self.state = state
        self.speed = speed

    def _get_speed(self):
        if self.state == 'fly':
            self.speed = 1.2
            return self.speed

        elif self.state == 'crawl':
            self.speed = 0.5

        else:
            raise ValueError('Что ты за зверь такой... Хм?')

    def move(self, field, x_coord, y_coord, direction):

        if direction == 'UP':
            self.field.set_unit(y=self.y + self.speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - self.speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - self.speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + self.speed, unit=self)
