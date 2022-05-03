#  Основной код
from random import randint
from dot import Dot
from messages import Greeting, Clr_Scr
from ship import Ship
from board import Boards


class Game:
    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Boards(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(l, randint(0, 1), Dot(randint(0, sefl.size), (0, sefl.size)))
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