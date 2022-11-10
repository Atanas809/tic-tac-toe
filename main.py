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
