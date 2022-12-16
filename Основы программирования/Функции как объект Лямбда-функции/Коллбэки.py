alf_s = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z',
         'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
alf_g = ['i', 'a', 'y', 'e', 'u', 'o']


def ask_password(login, password, success, failure):
    list_g = list()
    login_S = []
    password_S = []
    error1, error2 = False, False

    for symbol in password:
        if symbol in alf_g:
            list_g.append(symbol)
    if len(list_g) != 3:
        error1 = True

    for symbol in login:
        if symbol in alf_s:
            login_S.append(symbol)

    for symbol in password:
        if symbol in alf_s:
            password_S.append(symbol)

    if login_S != password_S:
        error2 = True

    if error1 & error2:
        failure(login.lower(), "Everything is wrong")
    elif error1:
        failure(login.lower(), "Wrong number of vowels")
    elif error2:
        failure(login.lower(), "Wrong consonants")
    else:
        success(login.lower())


def main(login, password):
    ask_password(login, password, lambda name: print(f"Привет, {name}!"),
                 lambda name, err: print(f"Кто-то пытался притвориться пользователем {name}, "
                                         f"но в пароле допустил ошибку: {err.upper()}."))
