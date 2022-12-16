hours = list(map(str, sorted(list(map(int, input().split())))))
minutes = list(map(str, sorted(list(map(int, input().split())))))
time = []

for i in hours:
    for j in minutes:
        if sum(map(int, list(i))) != sum(map(int, list(j))):
            time.append([i, j])

for i in time:
    if len(i[0]) == 1:
        i[0] = "0" + i[0]
    if len(i[1]) == 1:
        i[1] = "0" + i[1]
    print(f"{i[0]}:{i[1]}")
