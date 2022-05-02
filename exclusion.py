class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return 'Shot out of board'

class BoardShipOutException(BoardException):
    pass

class BoardUsedException(BoardException):
    def __str__(self):
        return 'The shot in this cell has already been'
