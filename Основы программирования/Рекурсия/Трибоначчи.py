def tribonacci(n, c=1, p=0, pp=0):
    if n == 0:
        return pp
    if n == 1:
        return p
    if n == 0:
        return c
    else:
        return tribonacci(n - 1, c + p + pp, c, p)
