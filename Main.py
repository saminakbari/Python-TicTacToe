from Game import Game
import re


def read_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        return lines


def write_to_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)


def write_game_result(given_game, result):
    content = "Player 1: " + given_game.players[0].name
    content += "\nPlayer 2: " + given_game.players[1].name
    content += "\nResult: " + str(result)
    content += "\n------------------------------------\n"
    write_to_file("history.txt", content)


def show_history(username):
    pattern = "^Player [12]: " + username + "\n$"
    content = ""
    lines = read_from_file("history.txt")
    for game_number in range(len(lines) // 4):
        line_number = game_number * 4
        if re.search(pattern, lines[line_number]) or re.search(pattern, lines[line_number + 1]):
            content += lines[line_number] + lines[line_number + 1] + lines[line_number + 2] + lines[line_number + 3]

    print("Your history:\n" + content)





def get_name():
    name = input("Enter your name: ")
    if name != '':
        return name
    return get_name()


def execute_the_game(game):
    game.show_board()
    game.next_move()
    winner = game.find_winner()
    if winner == -1:
        game.change_turn()
        execute_the_game(game)
        return

    if winner == 2:
        game.show_board()
        print("Draw!")
        write_game_result(game, "Draw.")

    else:
        game.show_board()
        print(game.players[winner].name + " wins!")
        write_game_result(game, game.players[winner].name + " won.")


def run_program():
    print("Press Enter key to start a game. You can enter 'e' to exit the game.\n"
          "If you want to see the history, press 'h'.")
    entered_char = input()
    if entered_char == 'e':
        return
    elif entered_char == 'h':
        show_history(get_name())

    else:
        game = Game()
        game.get_player_names(0)
        game.get_player_names(1)
        game.specify_chars("Please enter the first player's character (x/o): ")
        execute_the_game(game)
    run_program()


with open("history.txt", "w") as f:
    f.write("")
print("Welcome to Tic Tac Toe game!")
run_program()
