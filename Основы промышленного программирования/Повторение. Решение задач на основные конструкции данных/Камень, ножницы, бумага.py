pirat_1, pirat_2 = input(), input()

if pirat_1 == pirat_2:
    print("ничья")


elif pirat_1 == "бумага" and pirat_2 == "камень":
    print("первый")

elif pirat_1 == "ножницы" and pirat_2 == "бумага":
    print("первый")

elif pirat_1 == "камень" and pirat_2 == "ножницы":
    print("первый")


elif pirat_1 == "камень" and pirat_2 == "бумага":
    print("второй")

elif pirat_1 == "бумага" and pirat_2 == "ножницы":
    print("второй")

elif pirat_1 == "ножницы" and pirat_2 == "камень":
    print("второй")



