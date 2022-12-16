def Deu_convert(mark):
    return 6 - float(mark)


def NumRound(n):
    if 1 <= n < 1.5:
        return 1
    elif 1.5 <= n < 2.5:
        return 2
    elif 2.5 <= n < 3.5:
        return 3
    elif 3.5 <= n < 4.5:
        return 4
    elif n >= 4.5:
        return 5


def Usa_convert(mark):
    Usa_marks = {5: "A",
                 4: "B",
                 3: "C",
                 2: "D",
                 1: "F", }
    return Usa_marks.get(NumRound(mark))


def ComplexCounter(marks):
    letters = {"A": 5, "B": 4, "C": 3,
               "D": 2, "F": 1, "E": 1}
    res = []
    marks = marks.split()

    def Lettonum(letter):
        return letters.get(letter)

    if len(marks) == 1:
        for i in marks[0]:

            if i in letters.keys():
                res.append(Lettonum(i))

            elif int(i) in range(1, 6):
                res.append(int(i))

            else:
                raise Exception("Data error")

    elif len(marks) > 1:
        for i in marks:
            if i in letters.keys():
                res.append(Lettonum(i))

            elif int(i) in range(1, 6):
                res.append(int(i))

            else:
                raise Exception("Data error")

    return sum(res) / len(res)


def SimpleCounter(numbers):
    mark_amount = {1: None, 2: None,
                   3: None, 4: None, 5: None}
    try:
        for i in range(5):
            mark_amount[i + 1] = int(numbers[i])
            numbers[i] = (i + 1) * int(numbers[i])
    except Exception:
        raise Exception("Data error")
    return sum(numbers) / sum(mark_amount.values())
