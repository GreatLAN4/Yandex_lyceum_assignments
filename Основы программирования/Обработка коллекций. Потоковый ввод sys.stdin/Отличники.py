mark = []
good_student = 0
group = int(input())

for i in range(group):

    for j in range(int(input())):
        mark.append(input()[-1])

        if any(map(lambda x: x == "5", mark)):
            good_student += 1

    mark.clear()

if good_student >= group:
    print("ДА")
else:
    print("НЕТ")
