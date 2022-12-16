class OddEvenSeparator:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def even(self):
        return list(filter(lambda x: x % 2 == 0, self.numbers))

    def odd(self):
        return list(filter(lambda x: x % 2 != 0, self.numbers))
