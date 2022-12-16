PI = 3.14159


def circle_length(radius):
    length = 2 * PI * radius
    return length


def circle_area(radius):
    area = PI * (radius ** 2)
    return area


def main():
    radius = float(input())
    return print(circle_length(radius), circle_area(radius))
