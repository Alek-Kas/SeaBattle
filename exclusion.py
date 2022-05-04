class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return 'Выстрел за пределы доски'


class BoardShipOutException(BoardException):
    pass


class BoardUsedException(BoardException):
    def __str__(self):
        return 'В эту клетку уже нельзя стрелять'
