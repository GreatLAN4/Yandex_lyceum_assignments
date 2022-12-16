from random import choice

file = open('lines.txt', mode='r', encoding='utf8')
try:
    print(choice(file.readlines()))
except IndexError:
    pass
file.close()
