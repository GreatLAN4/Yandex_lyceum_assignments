def matrix(n=None, m=None, a=0):
    if n is None and m is None:
        n = 1
        m = 1
    elif m is None:
        m = n
    return [[a for i in range(m)] for j in range(n)]
