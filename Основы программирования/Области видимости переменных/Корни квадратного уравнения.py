from math import sqrt


def larger_root(p, q):
    D = p ** 2 - 4 * 1 * q
    x1 = ((p * - 1) + sqrt(D)) / 2 * 1
    x2 = ((p * - 1) - sqrt(D)) / 2 * 1
    if x1 > x2:
        return x1
    else:
        return x2


def smaller_root(p, q):
    D = p ** 2 - 4 * 1 * q
    x1 = ((p * - 1) + sqrt(D)) / 2 * 1
    x2 = ((p * - 1) - sqrt(D)) / 2 * 1
    if x1 < x2:
        return x1
    else:
        return x2


def discriminant(a, b, c):
    D = b ** 2 - 4 * a * c
    return D


def main():
    p = float(input())
    q = float(input())
    D = p ** 2 - 4 * 1 * q
    x1 = ((p * - 1) + sqrt(D)) / 2 * 1
    x2 = ((p * - 1) - sqrt(D)) / 2 * 1
    print(D)
    print(x2, x1)
