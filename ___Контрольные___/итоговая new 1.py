import sys

data = list(map(str.strip, sys.stdin))
friendly = []
enemy = []
for i in range(len(data)):
    line = list(map(int, data[i].split()))
    v = i + 1
    # print(line, v)

    if v % 2 != 0:
        for j in line:
            if j % v == 0:
                friendly.append(j)
        friendly = list(map(str, friendly))
        print(". ".join(friendly))

        friendly.clear()
    else:
        for j in line:
            if j % v != 0:
                enemy.append(j)
        enemy = list(map(str, enemy))
        print(". ".join(enemy))

        enemy.clear()
