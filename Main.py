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
    content = "Player 1: " + given_game.player_names[0]
    content += "\nPlayer 2: " + given_game.player_names[1]
    content += "\nResult: " + str(result)
    content += "\n------------------------------------\n"
    write_to_file("history.txt", content)


def show_history(username):
    pattern = "^Player [12]: " + username + "\n$"
    content = ""
    lines = read_from_file("history.txt")
    for game_number in range(len(lines) // 4):
        if re.search(pattern, lines[game_number]) or re.search(pattern, lines[game_number + 1]):
            content += lines[game_number] + lines[game_number + 1] + lines[game_number + 2] + lines[game_number + 3]

    print("Your history:\n" + content)


with open("history.txt", "w") as f:
    f.write("")

print("Welcome to Tic Tac Toe game!")
while True:
    print("Press Enter key to start a game. You can enter 'e' to exit the game.")
    print("If you want to see the history, press 'h'.")
    i = input()
    if i == 'e':
        break
    elif i == 'h':
        while True:
            print("Enter your name:", end=' ')
            i = input()
            if i != '':
                show_history(i)
                break

    else:
        game = Game()
        game.get_player_names()
        game.specify_chars()
        while True:
            game.show_board()
            game.next_move()
            winner = game.find_winner()
            if winner == -1:
                game.change_turn()
                continue

            if winner == 2:
                game.show_board()
                print("Draw!")
                write_game_result(game, "Draw.")
            else:
                game.show_board()
                print(game.player_names[winner] + " wins!")
                write_game_result(game, game.player_names[winner] + " won.")
            break
