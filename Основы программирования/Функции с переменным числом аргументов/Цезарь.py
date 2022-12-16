SMALL_alf = [chr(i) for i in range(ord('а'), ord('я') + 1)]
BIG_alf = [chr(i) for i in range(ord('А'), ord('Я') + 1)]


def encrypt_caesar(msg, shift=3):
    new_msg = []
    for i in msg:
        if 1039 < ord(i) < 1104:
            if i.isupper():
                index = BIG_alf.index(i) + shift
                new_i = BIG_alf[index % 32]
                new_msg.append(new_i)
            else:
                index = SMALL_alf.index(i) + shift
                new_i = SMALL_alf[index % 32]
                new_msg.append(new_i)
        else:
            new_msg.append(i)
    return ''.join(new_msg)


def decrypt_caesar(msg, shift=3):
    new_msg = []
    for i in msg:
        if 1039 < ord(i) < 1104:
            if i.isupper():
                index = BIG_alf.index(i) - shift
                new_i = BIG_alf[index % 32]
                new_msg.append(new_i)
            else:
                index = SMALL_alf.index(i) - shift
                new_i = SMALL_alf[index % 32]
                new_msg.append(new_i)
        else:
            new_msg.append(i)
    return ''.join(new_msg)


print(encrypt_caesar("Вова", 1))
