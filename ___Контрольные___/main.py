with open('boat_suits.txt', encoding='Windows-1251', mode='r+') as file:
    list = file.readlines()
color = input()
col, persons, sum = 0, [], 0
for pp in list:
    if color in pp:
        a, b, c = pp.rstrip('\n').split()
        if a not in persons:
            persons.append(a)
            col += 1
        sum += int(c)
with open('colored_dress.txt', encoding='Windows-1251', mode='w+') as file:
    file.writelines(f'{col}\n{sorted(persons, key=lambda w: -len(w))[0]}\n{sum}')