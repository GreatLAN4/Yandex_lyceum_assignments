def Brackets(numb):
    if (numb.count("(") < 2 and numb.count(")") < 2) \
            and numb.count("(") == numb.count(")"):
        return True
    raise Exception("неверный формат")


def SideDashes(numb):
    if numb[0] == "-" or numb[-1] == "-":
        raise Exception("неверный формат")
    else:
        return True


def DashesInNumber(numb):
    if SideDashes(numb):
        for i in range(len(numb)):
            if numb[i] == "-" and numb[i + 1] == "-":
                raise Exception("неверный формат")
        return


def IsDigit(numb, mode=0):
    numb = "".join([i for i in numb if i not in "-()+"])

    if all([i.isdigit() for i in numb]) and mode == 0:
        return True
    elif mode == 1:
        return numb
    raise Exception("неверный формат")


def DigitOperation(numb, mode=0):
    box = [i for i in numb if i.isdigit()]

    if len(box) != 11 and mode == 0:
        raise Exception("неверное количество цифр")
    elif mode == 1:
        return f"+7{IsDigit(numb, 1)[1::]}"


def Transform(number):
    if number[0] == "8" or number[0:2] == "+7":
        try:
            Brackets(number)
            try:
                DashesInNumber(number)
                try:
                    IsDigit(number)
                    try:
                        DigitOperation(number)
                        print(DigitOperation(number, 1))

                    except Exception as e:
                        print(e)
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
    else:
        print("неверный формат")


Transform("".join(input().split()))
