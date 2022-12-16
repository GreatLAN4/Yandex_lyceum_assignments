def LengthPassword(password):
    if len(password) > 8:
        return True
    raise Exception("PasswordLength")


def AreThereNumbers(password):
    [i for i in password if i.isdigit()]


def AlphabetIsUpper(password):
    eng = [chr(i) for i in range(ord("a"), ord("z") + 1)] \
          + [chr(i).upper() for i in range(ord("a"), ord("z") + 1)] + ["ё"]

    rus = [chr(i) for i in range(ord("а"), ord("я") + 1)] \
          + [chr(i).upper() for i in range(ord("а"), ord("я") + 1)]

    if [i for i in password if i in eng and i in rus]:
        return True
    raise Exception("AlphabetIsUpper")


def CheckPassword(password):
    try:
        LengthPassword(password)
        try:
            AlphabetIsUpper(password)

        except Exception as e:
            print(e)

    except Exception as e:
        print(e)


print(CheckPassword(input()))
