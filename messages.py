#  Приветственное сообщение
# from main import Game

class Greeting:
    def __init__(self, size):
        self.size = size


    def __str__(self):
        # self.size = str(size)
        # size = str(.size())
        return f'*' * 22 + '\n' \
               '*  ИГРА МОРСКОЙ БОЙ  *\n' \
               + '*' * 22 + '\n' \
               '\n' \
               'Эта игра в "морской бой с копьютером"\n' \
               'Игра проходит на поле размером ' \
               + str(self.size) + 'x' + str(self.size) +\
               ' клеток\n' \
               'В начале игрок должен раставить корабли на поле. ' \
               'Между кораблями должна быть хотя бы одна клетка и корабли должны целиком помещаться на поле.\n' \
               '' \
               'Координаты выстрела X Y вводятся через пробел, где X - номер строки, Y - номер столбца' \
               '\n\n'


class ClrScr:
    def __str__(self):
        strings = 40
        return '\n' * strings


# print(Greeting())
