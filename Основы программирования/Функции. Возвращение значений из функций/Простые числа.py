def prime(number):
    for i in range(2, number):
        return "Составное число" if number % i == 0\
            else "Простое число"
