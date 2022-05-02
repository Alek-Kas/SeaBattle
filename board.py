#  Класс доски для каждого из игроков
class Boards():
    def __init__(self, show = False, size = 6):
        self.show = show
        self.size = size

        self.dstr_ship = 0
        self.field = [['.'] * size for i in range(size)]

        self.cond = []
        self.ship = []

    def __str__(self):
        res_board = ''
        res_board += '__| 1 | 2 | 3 | 4 | 5 | 6 |'
        for i, row in enumerate(self.field):
            res_board += f'\n{i + 1} | ' + ' | ' .join(row) + ' |'
        if self.show:
            res_board = res_board.replace('.', 'O')
        return res_board

b = Boards()
print(b)
