#  Класс доски для каждого из игроков
import time

from dot import Dot
from exclusion import BoardOutException, BoardShipOutException, BoardUsedException

PAUSE = 1


class Boards:
    def __init__(self, show=True, size=6):
        self.show = show
        self.size = size

        self.dstr_ship = 0
        self.field = [['.'] * size for _ in range(size)]

        self.cond = []
        self.ships = []

    def __str__(self):
        # first_str = ' 1 | 2 | 3 | 4 | 5 | 6 |'
        # res_board = '\t|'
        res_board = ''
        first_str = '\t|'
        for i in range(1, self.size + 1):
            if i < 10:
                first_str += f' {i} |'
            else:
                first_str += f' {i}|'
        res_board += first_str
        for i, row in enumerate(self.field):
            res_board += f'\n{i + 1}\t| ' + ' | ' .join(row) + ' |'
        if not self.show:
            res_board = res_board.replace('O', '.')
        return res_board

    def out_board(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not(self.out_board(cur)) and cur not in self.cond:
                    if verb:
                        self.field[cur.x][cur.y] = '+'
                    self.cond.append(cur)

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out_board(d) or d in self.cond:
                raise BoardShipOutException()
        for d in ship.dots:  # отрисовка корабля символом "O"
            self.field[d.x][d.y] = 'O'
            self.cond.append(d)
        self.ships.append(ship)
        self.contour(ship)

    def shot(self, d):
        if self.out_board(d):
            raise BoardOutException
        if d in self.cond:
            raise BoardUsedException
        self.cond.append(d)
        for ship in self.ships:
            if ship.hitten(d):
                ship.hp -= 1
                self.field[d.x][d.y] = 'X'
                if ship.hp == 0:
                    self.dstr_ship += 1
                    self.contour(ship, verb=True)
                    print('Корабль потоплен!')
                    time.sleep(PAUSE)
                    return False
                else:
                    print('Корабль ранен!')
                    time.sleep(PAUSE)
                    return True
        self.field[d.x][d.y] = '*'
        print('Промах!')
        time.sleep(PAUSE)
        return False

    def begin(self):
        self.cond = []
