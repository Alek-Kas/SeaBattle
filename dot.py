#  Класс точек на поле
class Dot:

    def __init__(self, x, y):  #координаты и состояние точки
        self.x = x
        self.y = y
        # self.cond = cond

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Dot({self.x}, {self.y})'
