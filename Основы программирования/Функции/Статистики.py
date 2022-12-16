def print_statistics(arr):
    if arr:
        length = len(arr)
        index = length // 2
        arithmetic_mean = sum(arr) / length
        minimum = min(arr)
        maximum = max(arr)
        if length % 2:
            middle = sorted(arr)[index]
        else:
            middle = sum(sorted(arr)[index - 1:index + 1]) / 2
    else:
        length, arithmetic_mean, minimum, maximum, middle = 0, 0, 0, 0, 0
    print(f"{length}\n{arithmetic_mean}\n{minimum}\n{maximum}\n{middle}")
