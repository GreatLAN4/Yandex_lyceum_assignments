def transform(n):
    if n[0] == "8":
        n = f"+7{n[1:]}"
    if n.find("("):
        n = n.replace('(', '').replace(")", '')
    return ''.join(''.join(n.split()).split("-"))


def isNumber(num):
    ss = "+()-1234567890"
    er = False
    for el in num:
        if el not in ss:
            er = True
            break
    return er


number = ''.join(input().split())
Error = isNumber(number)

if number[0] == "-" or number[-1] == "-":
    Error = True

if (number[0:2] == "+7" or number[0] == "8") and not Error:
    if (number.count("(") == 1 and number.count(")") == 1) or (number.count("(") == 0 and number.count(")") == 0):
        if number.find("(") <= number.find(")"):
            for i in range(len(number) - 1):
                if number[i] == "-" and number[i + 1] == "-":
                    Error = True
                    break

        else:
            Error = True

    else:
        Error = True

else:
    Error = True

if not Error:
    n = transform(number)
    if len(n) == 12:
        print(n)
    else:
        print("error")
else:
    print("error")
