# A.Классная точка

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# B.Классная точка 2.0

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        length = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        length = round(length, 2)
        return length

# C.Не нажимай красную кнопку!

class RedButton:
    def __init__(self):
        self.push_times = 0

    def click(self):
        self.push_times += 1
        print('Тревога')

    def count(self):
        return self.push_times

# D.Работа не волк

class Programmer:
    __wages = {'Junior': 10, 'Middle': 15, 'Senior': 20}

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.time = 0
        self.wage = self.__wages[position]
        self.salary = 0

    def work(self, time):
        self.salary += time * self.wage
        self.time += time

    def rise(self):
        if self.position == 'Junior':
            self.position = 'Middle'
            self.wage = self.__wages[self.position]

        elif self.position == 'Middle':
            self.position = 'Senior'
            self.wage = self.__wages[self.position]

        else:
            self.wage += 1

    def info(self):
        return f'{self.name} {self.time}ч. {self.salary}тгр.'


# E. Классный прямоугольник

class Rectangle:

    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
        self.length_1 = abs(self.point_1[0] - self.point_2[0])
        self.length_2 = abs(self.point_1[1] - self.point_2[1])

    def perimeter(self):
        return round((self.length_1 + self.length_2) * 2, 2)

    def area(self):
        return round(self.length_1 * self.length_2, 2)

# F.Классный прямоугольник 2.0
class Rectangle:

    def __init__(self, point_1, point_2):
        self.pos = (min(point_1[0], point_2[0]), max(point_1[1], point_2[1]))
        self.width = abs(point_1[0] - point_2[0])
        self.height = abs(point_1[1] - point_2[1])

    def perimeter(self):
        return round((self.width + self.height) * 2, 2)

    def area(self):
        return round(self.width * self.height, 2)

    def get_pos(self):
        return round(self.pos[0], 2), round(self.pos[1], 2)

    def get_size(self):
        return round(self.width, 2), round(self.height, 2)

    def move(self, dx, dy):
        self.pos = self.pos[0] + dx, self.pos[1] + dy

    def resize(self, width, height):
        self.width = width
        self.height = height

# G.Классный прямоугольник 3.0 тесты не все проходит но решение вроде норм

class Rectangle:

    def __init__(self, point_1, point_2):
        self.pos = (min(point_1[0], point_2[0]), max(point_1[1], point_2[1]))
        self.width = abs(point_1[0] - point_2[0])
        self.height = abs(point_1[1] - point_2[1])

    def perimeter(self):
        return round((self.width + self.height) * 2, 2)

    def area(self):
        return round(self.width * self.height, 2)

    def get_pos(self):
        return round(self.pos[0], 2), round(self.pos[1], 2)

    def get_size(self):
        return round(self.width, 2), round(self.height, 2)

    def move(self, dx, dy):
        self.pos = round(self.pos[0] + dx, 2), round(self.pos[1] + dy, 2)

    def resize(self, width, height):
        self.width = width
        self.height = height

    def turn(self):
        self.pos = round(self.pos[0] + self.width / 2 - self.height / 2, 2), round(
            self.pos[1] - self.height / 2 + self.width / 2, 2)
        self.width, self.height = self.height, self.width

    def scale(self, multiplicator):
        self.pos = (
            round(self.pos[0] + self.width / 2 - self.width * multiplicator / 2, 2),
            round(self.pos[1] - self.height / 2 + self.height * multiplicator / 2, 2)
        )
        self.width, self.height = self.width * multiplicator, self.height * multiplicator


# H.Шашки
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

# I.Очередь
class Queue:

    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)

    def is_empty(self):
        return not bool(self.queue)


# J.Стек
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return not bool(self.stack)



