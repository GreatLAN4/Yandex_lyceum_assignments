import random
from random import sample
numpers = range(1, 76)


def make_bingo():
    line = []
    table = []

    for i in range(25):
        new_number = random.choice(numpers)
        while new_number in line:
            new_number = random.choice(numpers)
        line.append(new_number)
    line[12] = 0

    for i in range(5):
        table.append(tuple(line[i * 5:i * 5 + 5]))

    return tuple(table)

print(make_bingo())