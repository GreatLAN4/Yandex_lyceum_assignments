axis = []
select = []

for _ in range(int(input())):
    cord = input().split()
    cord = list(map(int, cord))

    if abs(cord[0]) > abs(cord[1]):
        axis.append(cord)
    select.append(cord)

s = [select[i][0] for i in range(len(select))]
w = [select[i][1] for i in range(len(select))]

for i in axis:
    print(f"({i[0]}, {i[1]})")

print("left:", tuple(select[s.index(min(s))]))
print("right:", tuple(select[s.index(max(s))]))
print("top:", tuple(select[w.index(max(w))]))
print("bottom:", tuple(select[w.index(min(w))]))
