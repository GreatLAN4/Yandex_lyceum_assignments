old_print = print


def print(*args):
    old_print(*map(lambda x: str(x).upper(), args))
