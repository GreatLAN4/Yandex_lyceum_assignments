class Stat:
    def __init__(self):
        self.the_numbers = []

    def add_number(self, number):
        self.the_numbers.append(number)


class MinStat(Stat):

    def result(self):
        if self.the_numbers:
            return min(self.the_numbers)
        elif not self.the_numbers:
            return "None"


class MaxStat(Stat):

    def result(self):
        if self.the_numbers:
            return max(self.the_numbers)
        elif not self.the_numbers:
            return "None"


class AverageStat(Stat):

    def result(self):
        if self.the_numbers:
            return float(sum(self.the_numbers) / len(self.the_numbers))
        elif not self.the_numbers:
            return "None"
