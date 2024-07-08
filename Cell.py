class Cell:
    def __init__(self):
        self.character = '-'

    def __getitem__(self, item):
        return self.character

    def __setitem__(self, key, value):
        self.character = value
