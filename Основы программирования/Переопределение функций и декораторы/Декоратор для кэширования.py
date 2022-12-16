def cached(func):
    count = 0

    def decorated_func(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        result = func(*args, **kwargs)
        return result

    return decorated_func


@cached
def fib(n):
    f1, f2 = 0, 1
    for i in range(n - 2):
        f1, f2 = f2, f2 + f1
    print(f2)
    return f2


fib(int(input()))
fib(int(input()))
fib(int(input()))
fib(int(input()))
