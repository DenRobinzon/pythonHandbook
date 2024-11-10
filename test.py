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

    def turn(self):
        self.pos = self.pos[0] + self.width / 2 - self.height / 2, self.pos[1] - self.height / 2 + self.width / 2
        self.width, self.height = self.height, self.width

    def scale(self, multiplicator):
        self.pos = self.pos[0] + self.width / 2 - self.width * multiplicator / 2, self.pos[
            1] - self.height / 2 + self.height * multiplicator / 2
        self.width, self.height = self.width * multiplicator, self.height * multiplicator


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')

rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')
