class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):

    def __init__(self, a):
        self.a = a
        self.b = a
        self.c = a

    def perimeter(self):
        return Triangle.perimeter(self)


print(Triangle(1, 2, 3).perimeter())
