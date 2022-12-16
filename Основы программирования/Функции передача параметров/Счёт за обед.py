asw = []


def count_food(days):
    for i in days:
        asw.append(daily_food[i - 1])
    return sum(asw)


daily_food = [0, 150, 150]
print(count_food([1]))
