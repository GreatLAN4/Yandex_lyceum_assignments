stage = input().split(" -> ")

for _ in range(int(input())):
    queue = []
    unit = input()
    if stage.index(unit) == 0:
        queue.append(unit)
        queue.append(stage[stage.index(unit) + 1])
        print(" -> ".join(queue))

    elif stage.index(unit) == len(stage) - 1:
        queue.append(stage[stage.index(unit) - 1])
        queue.append(unit)
        print(" -> ".join(queue))

    elif stage.index(unit) != 0 and stage.index(unit) != -1:
        queue.append(stage[stage.index(unit) - 1])
        queue.append(unit)
        queue.append(stage[stage.index(unit) + 1])
        print(" -> ".join(queue))
