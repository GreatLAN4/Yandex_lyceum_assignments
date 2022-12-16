from random import choice

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'm', 'n', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

letters_b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
             'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'L']

digits = ['2', '3', '4', '5', '6', '7', '8', '9']
big_list = []
big_list.extend(letters)
big_list.extend(letters_b)
big_list.extend(digits)


def generate_password(m):
    password = ''.join([choice(big_list) for _ in range(m)])
    print(password.isdigit())
    print(password.isupper())
    print(password.islower())
    print(password)
    # while
    return password


def main(n, m):
    pass_list = []
    while len(pass_list) != n:
        just_pass = generate_password(m)
        if just_pass not in pass_list:
            pass_list.append(just_pass)
    return pass_list


generate_password(16)
