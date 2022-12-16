first, second, third, forth = 0, 0, 0, 0
axis = []
for _ in range(int(input())):
    cord = input().split()

    cord[0], cord[1] = int(cord[0]), int(cord[1])

    if cord[0] > 0 and cord[1] > 0:
        first += 1
    elif cord[0] < 0 and cord[1] > 0:
        second += 1
    elif cord[0] < 0 and cord[1] < 0:
        third += 1
    elif cord[0] > 0 and cord[1] < 0:
        forth += 1
    if 0 in cord:
        axis.append(cord)

for _ in axis:
    print(f"({_[0]}, {_[1]})")
print(f"I: {first}, II: {second}, III: {third}, IV: {forth}.")