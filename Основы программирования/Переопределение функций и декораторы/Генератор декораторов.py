password = False


def check_password(n=input("введите пароль\n")):
    global password
    if n == "1":
        password = True
        return password


@check_password
def fb(x):
    check_password("1")

    if password:
        x1, x2 = 0, 1
        if x == x1:
            return x1

        for i in range(x - 2):
            x1, x2 = x2, x1 + x2
        return x2

    else:
        return "В доступе отказано"
