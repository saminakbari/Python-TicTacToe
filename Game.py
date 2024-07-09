import Player
from Board import Board


def get_an_integer(message):
    print(message)
    given_input = input()
    try:
        return int(given_input)
    except:
        return get_an_integer("Please enter an integer:")


def get_int_in_range(message, minimum, maximum, axis):
    given_input = get_an_integer(message)
    if minimum <= given_input <= maximum:
        return given_input
    return get_int_in_range("The " + axis + " number must be between 1 and 3."
                                            " Enter the " + axis + " again:", minimum, maximum, axis)


def get_coordinates(given_game):
    entered_row = get_int_in_range("row: ", 1, 3, "row")
    entered_col = get_int_in_range("column: ", 1, 3, "column")

    if given_game.board[entered_row - 1][entered_col - 1].character == '-':
        return given_game.board[entered_row - 1][entered_col - 1]
    print("This place is not empty. Enter the row and column again.")
    return get_coordinates(given_game)


class Game:
    def __init__(self):
        self.board = Board()
        for row in range(3):
            for col in range(3):
                self.board[row][col].character = '-'
        self.players = [Player.Player(), Player.Player()]
        self.player_chars = ['', '']
        self.current_player = 0

    def get_player_names(self, index):
        if index == 0:
            message = "Please enter the first player's name: "
        else:
            message = "Please enter the first player's name: "

        print(message)
        given_input = input()
        if given_input != '':
            self.players[index].name = given_input
        else:
            self.get_player_names(index)

    def specify_chars(self, message):
        print(message)
        char = input()
        if char == 'x' or char == 'X':
            self.player_chars[0] = 'x'
            self.player_chars[1] = 'o'
        elif char == 'o' or char == 'O':
            self.player_chars[0] = 'o'
            self.player_chars[1] = 'x'
        else:
            self.specify_chars("Please enter either 'x' or 'o'")

    def next_move(self):
        print(self.players[self.current_player].name + " is now playing.")
        specified_cell = get_coordinates(self)
        specified_cell.character = self.player_chars[self.current_player]

    def change_turn(self):
        if self.current_player == 0:
            self.current_player = 1
        else:
            self.current_player = 0

    def show_board(self):
        for row in range(3):
            for col in range(3):
                print(self.board[row][col].character, end=" ")
            print()

    def find_winner(self):
        
        # specifying the winning states
        lines = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6))

        for line in lines:
            if (self.board[line[0] // 3][line[0] % 3].character == self.player_chars[self.current_player]
                    and self.board[line[1] // 3][line[1] % 3].character == self.player_chars[self.current_player]
                    and self.board[line[2] // 3][line[2] % 3].character == self.player_chars[self.current_player]):
                return self.current_player

        for row in range(3):
            for col in range(3):
                if self.board[row][col].character == '-':
                    return -1  # Not finished.
        return 2  # No one wins.
