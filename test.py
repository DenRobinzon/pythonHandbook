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


programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
