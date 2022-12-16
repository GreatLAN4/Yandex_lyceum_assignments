def rec_linear_sum(x, i=0):
    if i >= len(x):
        return 0
    return x[i] + rec_linear_sum(x, i + 1)
