from Board import Board


class Game:
    def __init__(self):
        self.board = Board()
        for i in range(3):
            for j in range(3):
                self.board[i][j].character = '-'
        self.player_names = ['', '']
        self.player_chars = ['', '']
        self.current_player = 0

    def get_player_names(self):
        while True:
            print("Please enter the first player's name: ")
            i = input()
            if i != '':
                self.player_names[0] = i
                break

        while True:
            print("Please enter the second player's name: ")
            i = input()
            if i != '':
                self.player_names[1] = i
                break

    def specify_chars(self):
        print("Please enter the first player's character (x/o): ")
        while True:
            char = input()
            if char == 'x' or char == 'X':
                self.player_chars[0] = 'x'
                self.player_chars[1] = 'o'
                break
            elif char == 'o' or char == 'O':
                self.player_chars[0] = 'o'
                self.player_chars[1] = 'x'
                break
            else:
                print("Please enter either 'x' or 'o'")

    def next_move(self):
        print(self.player_names[self.current_player] + " is now playing.")
        while True:
            print("row:", end=' ')
            while True:
                i = input()
                try:
                    entered_row = int(i)
                except:
                    print("Please enter an integer:")
                    continue
                if 1 <= entered_row <= 3:
                    break
                print("The row number must be between 1 and 3.\nEnter the row again:", end='')

            print("column:", end='')
            while True:
                i = input()
                try:
                    entered_col = int(i)
                except:
                    print("Please enter an integer:")
                    continue
                if 1 <= entered_col <= 3:
                    break
                print("The column number must be between 1 and 3.\nEnter the column again:", end='')

            if self.board[entered_row - 1][entered_col - 1].character == '-':
                self.board[entered_row - 1][entered_col - 1].character = self.player_chars[self.current_player]
                break
            print("This place is not empty. Enter the row and column again.")

    def change_turn(self):
        if self.current_player == 0:
            self.current_player = 1
        else:
            self.current_player = 0

    def show_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j].character, end=" ")
            print()

    def find_winner(self):

        for i in range(3):
            cur_player_wins = True
            for j in range(3):
                if self.board[i][j].character != self.player_chars[self.current_player]:
                    cur_player_wins = False
                    break
            if cur_player_wins:
                return self.current_player

        for i in range(3):
            cur_player_wins = True
            for j in range(3):
                if self.board[j][i].character != self.player_chars[self.current_player]:
                    cur_player_wins = False
                    break
            if cur_player_wins:
                return self.current_player

        cur_player_wins = True
        for i in range(3):
            if self.board[i][i].character != self.player_chars[self.current_player]:
                cur_player_wins = False
                break
        if cur_player_wins:
            return self.current_player

        cur_player_wins = True
        for i in range(3):
            if self.board[i][2 - i].character != self.player_chars[self.current_player]:
                cur_player_wins = False
                break
        if cur_player_wins:
            return self.current_player

        for i in range(3):
            for j in range(3):
                if self.board[i][j].character == '-':
                    return -1  # Not finished.
        return 2  # No one wins.



