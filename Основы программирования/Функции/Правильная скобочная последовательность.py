def bracket_check(test_string):
    if test_string == "":
        return print("YES")
    elif test_string[0] == ")":
        return print("NO")

    asw = []
    for i in test_string:
        if i == "(":
            asw.append(i)

        elif i == ")":
            if len(asw) != 0 and asw[-1] == "(":
                asw.pop(-1)
            else:
                return print("NO")

    if len(asw) == 0:
        return print("YES")

    return print("NO")
