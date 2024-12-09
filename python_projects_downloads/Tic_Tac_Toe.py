def display(board):
    result = ''

    for column in board:
        for row in column:
            result += row
        result += '\n'

    print(result)


def check_winner(game):
    for row in game:
        if len(set(row)) == 1 and '.' not in row:
            print(f"Player {row[0]} wins!")
            quit()

    columns = [list(col) for col in zip(*game)]
    for column in columns:
        if len(set(column)) == 1 and '.' not in column:
            print(f"Player {column[0]} wins!")
            quit()

    diag1 = [game[i][i] for i in range(3)]
    if len(set(diag1)) == 1 and '.' not in diag1:
        print(f"Player {diag1[0]} wins!")
        quit()

    diag2 = [row[-i - 1] for i, row in enumerate(game)]
    if len(set(diag2)) == 1 and '.' not in diag2:
        print(f"Player {diag2[0]} wins!")
        quit()

    if '.' not in game[0] + game[1] + game[2]:
        print("It's a draw!")
        quit()


def play(player, game, x, y):
    while game[x][y] != '.':
        move = input(f"Field occupied! Try again: ")
        x, y = int(move[0]), int(move[1])
    game[x][y] = player


board = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]
display(board)

player = 'O'

while True:
    move = input(f"Player {player}: ")
    x, y = int(move[0]), int(move[1])
    play(player, board, x, y)
    display(board)
    check_winner(board)

    if player == 'O':
        player = 'X'
    elif player == 'X':
        player = 'O'
