error = "error"


def Brackets(numb):
    if (numb.count("(") < 2) and (numb.count(")") < 2) \
            & numb.count("(") == numb.count(")"):
        return True
    raise Exception("Brackets")


def SideDashes(numb):
    if numb[0] == "-" or numb[-1] == "-":
        raise Exception("SideDashes")
    else:
        return True


def DashesInNumber(numb):
    if SideDashes(numb):
        for i in range(len(numb)):
            if numb[i] == "-" and numb[i + 1] == "-":
                raise Exception("DashesInNumber")


def DigitCount(numb, mode=0):
    box = [i for i in numb if i.isdigit()]
    if len(box) != 11 and mode == 0:
        raise Exception("DigitCount")
    elif mode == 1:
        return "".join(box)[1::]


def Transform(number):
    try:
        DigitCount(number)
        try:
            Brackets(number)
            try:
                DashesInNumber(number)
                if number[0] == "8":
                    print(f"+7{DigitCount(number, 1)}")
            except Exception:
                print(error)
        except Exception:
            print(error)
    except Exception:
        print(error)


Transform("".join(input().split()))
