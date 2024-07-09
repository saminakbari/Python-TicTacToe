import Cell

DIMENSION = 3


class Board:
    def __init__(self):
        self.board = [[Cell.Cell() for _ in range(DIMENSION)] for _ in range(DIMENSION)]

    def __getitem__(self, pos):
        return self.board[pos]
