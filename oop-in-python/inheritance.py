from math import pi


class Shape(object):
    def area(self):
        raise NotImplemented

    def circumference(self):
        raise NotImplemented


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r ** 2

    def circumference(self):
        return 2 * pi * self.r


if __name__ == '__main__':
    shape = Circle(10)

    print(f'{shape.area()}')
    print(f'{shape.circumference()}')
