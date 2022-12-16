def Encryption():
    global encrypt_alphabet, decrypted_alphabet
    encrypt_alphabet = stock_alphabet[shift:] + stock_alphabet[:shift]
    decrypted_alphabet = stock_alphabet[-shift:] + stock_alphabet[:-shift]
    print("".join(encrypt_alphabet), stock_alphabet, "".join(decrypted_alphabet), sep="\n")


stock_alphabet = input()
shift = int(input())

if len(stock_alphabet) < abs(shift) and shift < 0:
    shift = shift % len(stock_alphabet)

elif len(stock_alphabet) < shift:
    shift = shift % len(stock_alphabet)

Encryption()
