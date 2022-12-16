f = open("prices.txt", mode="r", encoding="utf8")


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


f_lines = f.readlines()
f_lines = [i.rstrip("\n").split("\t") for i in f_lines]
summ = [float(i[1]) * float(i[2]) for i in f_lines]

print(toFixed(sum(summ), 2))
