#  Основной код
from random import randint
from dot import Dot
from exclusion import BoardShipOutException
from messages import Greeting, ClrScr
from player import AI, User
from ship import Ship
from board import Boards
import time

board_size = 7  # выбор размера доски


class Game:
    def __init__(self, size=6):
        self.size = size
        co = self.random_board()
        co.show = False
        pl = self.random_board()  # это для сучайной расстановки кораблей игроку
        # pl = self.manual_board()  # это для ручной расстановки кораблей игроком
        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Boards(size=self.size)
        attempts = 0
        for i in lens:
            while True:
                attempts += 1
                if attempts > 3000:
                    return None
                ship = Ship(i, randint(0, 1), Dot(randint(0, self.size), randint(0, self.size)))
                try:
                    board.add_ship(ship)
                    break
                except BoardShipOutException:
                    pass
        board.begin()
        return board

    def manual_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]  # для длинны 1 убрать запрос направления
        board = Boards(size=self.size)
        for j, i in enumerate(lens):
            while True:
                print(board)  # напечать доску перед каждым кораблём
                print(f'Введите координаты первой клетки корабля номер {j + 1} из {len(lens)} длинной {i} и направление,'
                      f'где "1" - горизонтально, а "0" - вертикально')
                while True:
                    x_y_d = input('Введите: ').split()
                    if len(x_y_d) != 3:
                        print(' Введите три числа через пробел! ')
                        continue
                    x, y, d = x_y_d
                    if not (x.isdigit()) or not (y.isdigit()) or not (d.isdigit()):
                        print(' Введите числа! ')
                        continue
                    if d != '0' and d != '1':
                        print(' Введите направление "0" или "1"! ')
                        continue
                    break
                # x_y_d = input('?: ').split()  # через функцию не стал делать, так как используется 1 раз
                # x, y, d = x_y_d
                x, y, d = int(x), int(y), int(d)
                ship = Ship(i, d, Dot(x - 1, y - 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardShipOutException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def loop(self):
        q = None
        while q != 'Y' and q != 'y' and q != 'N' and q != 'n':
            q = input('Хотите использовать случайную расстановку кораблей? Введите "Y" или "N": ')
        if q == 'N' or q == 'n':
            pl = self.manual_board()  # для ручной расстановки кораблей игроком
            co = self.random_board()
            co.show = False
            self.ai = AI(co, pl)
            self.us = User(pl, co)
        num = 0
        while True:
            print('-' * 20)
            print('Доска пользователя:')
            print(self.us.board)
            print('-' * 20)
            print('Доска компьютера:')
            print(self.ai.board)
            print('-' * 20)
            time.sleep(5)
            if num % 2 == 0:
                print(' Ход пользователя! ')
                repeat = self.us.move()
            else:
                print(' Ход компьютера! ')
                repeat = self.ai.move()
            if repeat:
                num -= 1
            if self.ai.board.dstr_ship == 7:
                print('-' * 20)
                print('Пользователь выиграл!')
                break
            if self.us.board.dstr_ship == 7:
                print('-' * 20)
                print('Выиграл компьютер! :(')
                break
            num += 1

    def start(self):
        print(ClrScr())
        print(Greeting(board_size))
        time.sleep(5)
        self.loop()


g = Game(board_size)
g.start()
