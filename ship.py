#  Класс кораблей
from dot import Dot


class Ship:

    def __init__(self, lenght, direction, x_y):
        self.lenght = lenght
        self.direction = direction
        self.x_y = x_y
#        self.y = y
        self.hp = lenght

    @property
    def dots(self):
        ship_dots = []
        point_x = self.x_y.x
        point_y = self.x_y.y
        for i in range(self.lenght):
            ship_dots.append(Dot(point_x, point_y))
            # point_x = self.x_y.x
            # point_y = self.x_y.y
            if self.direction == 0:
                point_x += 1
            elif self.direction == 1:
                point_y += 1
            # ship_dots.append(Dot(point_x, point_y))
        # print(ship_dots)
        return ship_dots

    def hitten(self, shot):
        return shot in self.dots
