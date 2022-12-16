password = False


def check_password(n=input("введите пароль\n")):
    global password
    if n == "1":
        password = True
    else:
        return "В доступе отказано"

    def fb(x):
        if password:

            if x in (1, 2):
                return 1
            return fb(x - 1) + fb(x - 2)

    return fb(int(input()))


# print(check_password())
