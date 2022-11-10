def is_draw(board):

    counter = 0

    for x in board:
        counter += x.count(None)

    if counter == 0:
        return True
    else:
        return False



def is_win(board, sign):

    possible_wins = {
        "horizontal": [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
        ],
        "vertical": [
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
        ],
        "diagonal": [
            [board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]],
        ]
    }

    win = sign * 3

    for key, value in possible_wins.items():
        for x in value:
            result = ''.join(str(i) for i in x)
            if result == win:
                return True

    return False


def print_table(board, size):
    index = 1
    for row in range(size):
        current_row = ""
        for col in range(size):
            if board[row][col] == None:
                if index % 3 != 0:
                    current_row += f"|     "
                else:
                    current_row += f"|     |"
            else:
                sign = board[row][col]
                if index % 3 != 0:
                    current_row += f"|  {sign}  "
                else:
                    current_row += f"|  {sign}  |"
            index += 1
        print(current_row)


def apply_move(position, board, sign):

    possible_moves = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
    }

    row, col = possible_moves[position]

    if board[row][col] != None:
        return board, False
    else:
        board[row][col] = sign
        return board, True

def valid_position(position):
    if 1 <= position <= 9:
        return True

    return False


def read_board(size):

    matrix = []

    for _ in range(size):
        matrix.append([None for _ in range(size)])

    return matrix


def numeration_of_the_board(size):

    print("This is the numeration of the board:")

    matrix = []
    index = 1

    for row in range(size):
        current_row = []
        for col in range(size):
            if index % 3 == 0:
                current_row.append(f"|  {index}  |")
            else:
                current_row.append(f"|  {index} ")
            index += 1
        matrix.append(current_row)

    for r in matrix:
        print(' '.join(str(x) for x in r))


def play(players, board):
    player_one, player_one_sign = players[0][0], players[0][1]
    player_two, player_two_sign = players[1][0], players[1][1]
    print(f"{player_one} starts first!")

    index = 1
    current_player = ""
    current_sign = ""

    while True:
        is_free_space = True
        if index == 1:
            current_player, current_sign = player_one, player_one_sign
        else:
            current_player, current_sign = player_two, player_two_sign

        position = int(input(f"{current_player} choose a free position [1-9]: "))

        if valid_position(position):
            board, is_free_space = apply_move(position, board, current_sign)
            if not is_free_space:
                continue
            else:
                print_table(board, size_board)

            if is_win(board, current_sign):
                print(f"{current_player} won!")
                break
            if is_draw(board):
                print("It's a draw!")
                break
        else:
            print("Please choose a valid position!")
            continue

        if index == 2:
            index = 1
            continue

        index += 1


def read_players_data():
    player_one = input("Player one name: ")
    player_two = input("Player two name: ")

    valid_signs = ['X', 'O']

    player_one_sign = input(f"{player_one} would you like to play with 'X' or 'O'?: ").upper()

    if player_one_sign not in valid_signs:
        player_one_sign = input(f"{player_one} would you like to play with 'X' or 'O'?: ").upper()

    player_two_sign = 'O' if player_one_sign == "X" else "X"

    players_data = (player_one, player_one_sign), (player_two, player_two_sign)

    return players_data


players_info = read_players_data()
size_board = 3
numeration_of_the_board(size_board)

board = read_board(size_board)

play(players_info, board)
