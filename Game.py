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
        for i in range(3):
            for j in range(3):
                self.board[i][j].character = '-'
        self.players = [Player.Player(), Player.Player()]
        self.current_player = 0

    def get_player_names(self, ):
        while True:
            print("Please enter the first player's name: ")
            i = input()
            if i != '':
                self.players[0].name = i
                break

        while True:
            print("Please enter the second player's name: ")
            i = input()
            if i != '':
                self.players[1].name = i
                break

    def specify_chars(self):
        print("Please enter the first player's character (x/o): ")
        while True:
            char = input()
            if char == 'x' or char == 'X':
                self.players[0].character = 'x'
                self.players[1].character = 'o'
                break
            elif char == 'o' or char == 'O':
                self.players[0].character = 'o'
                self.players[1].character = 'x'
                break
            else:
                print("Please enter either 'x' or 'o'")

    def next_move(self):
        print(self.players[self.current_player].name + " is now playing.")
        specified_cell = get_coordinates(self)
        specified_cell.character = self.players[self.current_player].character

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
        for row in range(3):
            cur_player_wins = True
            for col in range(3):
                if self.board[row][col].character != self.players[self.current_player].character:
                    cur_player_wins = False
                    break
            if cur_player_wins:
                return self.current_player

        for col in range(3):
            cur_player_wins = True
            for row in range(3):
                if self.board[row][col].character != self.players[self.current_player].character:
                    cur_player_wins = False
                    break
            if cur_player_wins:
                return self.current_player

        cur_player_wins = True
        for row in range(3):
            if self.board[row][row].character != self.players[self.current_player].character:
                cur_player_wins = False
                break
        if cur_player_wins:
            return self.current_player

        cur_player_wins = True
        for row in range(3):
            if self.board[row][2 - row].character != self.players[self.current_player].character:
                cur_player_wins = False
                break
        if cur_player_wins:
            return self.current_player

        for row in range(3):
            for col in range(3):
                if self.board[row][col].character == '-':
                    return -1  # Not finished.
        return 2  # No one wins.
