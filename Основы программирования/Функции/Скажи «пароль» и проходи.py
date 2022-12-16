def ask_password():
    password = "password"

    input_password = input()  # 1
    if input_password != password:

        input_password = input()  # 2
        if input_password != password:

            input_password = input()  # 3
            if input_password != password:
                print("В доступе отказано")
            else:
                print("Пароль принят")
        else:
            print("Пароль принят")
    else:
        print("Пароль принят")
    while True:
        input_password = input()
