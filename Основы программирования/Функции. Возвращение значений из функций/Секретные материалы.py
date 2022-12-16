def print_document(pages):
    secret = False
    for i in pages:
        if "Секретно" not in i:
            print(i)
        else:
            secret = True
            break
    if secret:
        print("Дальнейшие материалы засекречены")
    else:
        print("Напечатано без купюр")

