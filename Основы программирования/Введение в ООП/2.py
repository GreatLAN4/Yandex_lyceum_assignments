class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def intersection(self, other):
        if ((other.x >= self.x + self.w) or (other.y >= self.y + self.h) or
                (self.x >= other.x + other.w) or (self.y >= other.y + other.h)):
            return None
        else:
            R3 = Rectangle(0, 0, 0, 0)
            R3.x = max(self.x, other.x)
            R3.w = min(self.x + self.w, other.x + other.w) - R3.x
            R3.y = max(self.y, other.y)
            R3.h = min(self.y + self.h, other.y + other.h) - R3.y
            return R3

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h


if __name__ == '__main__':
    rect1 = Rectangle(0.1, 0.2, 10.8, 10.07)
    rect2 = Rectangle(5.4, 5.8, 10.25, 10.45)
    if rect1.intersection(rect2):
        rect3 = rect1.intersection(rect2)
        print((rect3.x, rect3.y, rect3.w, rect3.h))
        print(rect3)
