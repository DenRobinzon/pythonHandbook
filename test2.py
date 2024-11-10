class Checkers:
    def __init__(self):
        self.board = {}
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
                self.board[col[1] + row[1]] = Cell(state)

    def move(self, f, t):
        self.board[f], self.board[t] = self.board[t], self.board[f]

    def get_cell(self, p):
        return self.board[p]


class Cell:
    def __init__(self, state):
        self.state = state

    def status(self):
        return self.state


checkers = Checkers()
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()

print()

checkers = Checkers()
checkers.move('C3', 'D4')
checkers.move('H6', 'G5')
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()
