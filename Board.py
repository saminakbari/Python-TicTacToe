import Cell


class Board:
    def __init__(self):
        self.board = [Cell.Cell() for _ in range(3) for _ in range(3)]

    def __getitem__(self, pos):
        return self.board[pos]
