def line(s, t):
    t = t.split(";")
    x = float(t[0])
    y = float(t[1])

    formula = [_ for _ in s]
    k = float("".join(formula[:formula.index("x")]))
    b = float("".join(formula[formula.index("x") + 1:]))
    print(k * x + b == y)
