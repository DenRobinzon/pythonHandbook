board = {}
for row in enumerate('87654321'):
    for col in enumerate('ABCDEFGH'):
        if (row[0] + col[0]) % 2 == 0:
            state = 'X'
        elif row[1] in '876':
            state = 'B'
        elif row[1] in '123':
            state = 'W'
        else:
            state = 'X'
        board[col[1] + row[1]] = state

for row in '87654321':
    for col in 'ABCDEFGH':
        print(board[col + row], end='')
    print()

