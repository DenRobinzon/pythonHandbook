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


# E.
# F.
# G.
# H.
# I.
# J.
# K.
# L.
# M.
# N.
# O.
# P.
# Q.
# R.
# S.
# T.