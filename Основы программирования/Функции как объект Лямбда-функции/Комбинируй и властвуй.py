Numbers = sum(list(map(lambda x: x ** 2, filter(lambda I: I % 9 == 0, range(10, 100)))))
print(Numbers)
