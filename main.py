print('Let`s play TicTacToe!')
game_field = list(range(1, 10))


def draw_game_field():
    print("-" * 13)
    for i in range(3):
        print("", "|", game_field[0 + i * 3], "|", game_field[1 + i * 3], "|", game_field[2 + i * 3])
        print("-" * 13)


def player_input(game_label):
    value = False
    while not value:
        player_answer = input("What`s your move " + game_label + "?")
        try:
            player_answer = int(player_answer)
        except:
            print("Incorrect move. Please, insert the number")
            continue
        if 1 <= player_answer <= 9:
            if str(game_field[player_answer - 1]) not in "XO":
                game_field[player_answer - 1] = game_label
                value = True
            else:
                print("This cell is not free")
        else:
            print("Please, insert the number 1-9")


def check_win():
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if game_field[each[0]] == game_field[each[1]] == game_field[each[2]]:
            return game_field[each[0]]
    return False


def mainloop():
    counter = 0
    while True:
        draw_game_field()
        if counter % 2 == 0:
            player_input("X")
        else:
            player_input("O")
        counter += 1
        if counter > 4:
            winner = check_win()
            if winner:
                print("The ", winner, "win!", "Congratulate!")
                break
        if counter == 9:
            print("Piece!")
            break
    draw_game_field()


mainloop()

input("Press ENTER for exit")