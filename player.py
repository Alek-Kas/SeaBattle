# Класс игрока
from random import randint

from dot import Dot
from exclusion import BoardException


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f'Ход компьютера: {d.x + 1} {d.y + 1}')
        return d


class User(Player):
    def ask(self):
        while True:
            coords = input('Ваш ход, введите координаты через пробел: ').split()
            if len(coords) != 2:
                print(' Введите две координаты! ')
                continue
            x, y = coords
            if not(x.isdigit()) or not(x.isdigit()):
                print(' Введите числа! ')
                continue
            x, y = int(x), int(y)
            return Dot(x-1, y-1)
