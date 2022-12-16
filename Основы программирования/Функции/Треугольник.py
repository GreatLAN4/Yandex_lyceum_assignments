def triangle(a, b, c):
    if a + b > c:
        if b + c > a:
            if c + a > b:
                print("Это треугольник")
            else:
                print("Это не треугольник")
        else:
            print("Это не треугольник")

    elif b + c > a:
        if a + b > c:
            if c + a > b:
                print("Это треугольник")
            else:
                print("Это не треугольник")
        else:
            print("Это не треугольник")

    elif c + a > b:
        if a + b > c:
            if b + c > a:
                print("Это треугольник")
            else:
                print("Это не треугольник")
        else:
            print("Это не треугольник")
    else:
        print("Это не треугольник")
