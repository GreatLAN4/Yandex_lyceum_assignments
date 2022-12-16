def stubbornness(args):
    for i in args:
        if len(i) < 3:
            raise Exception("NotEnoughError: Not enough values")

    try:
        stub = list(set([k[0] for k in args if k[0] % max(k) == 0 and k[0] % min(k) == 0]))
        if not stub:
            return "IndexError: Empty Return Error"
        return stub

    except ZeroDivisionError:
        return "ZeroDivisionError: Cannot be divided by zero"


data = [(2, 3, 7)]

print(stubbornness(data))
