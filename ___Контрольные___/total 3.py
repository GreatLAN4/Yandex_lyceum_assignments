import math

class WaitingLounge:
    def __init__(self, weight, distance, transmitter_class):
        self.weight = weight
        self.distance = distance
        self.transmitter_class = transmitter_class

    def sol(self, a, b):
        if a > b:
            return 1, 0
        elif a == b:
            return 0, 0
        else:
            return 0, 1

    def prior_search(self, other):
        a1, b1 = self.sol(len(self.weight), len(other.weight))
        a2, b2 = self.sol(self.distance, other.distance)
        a3, b3 = self.sol(self.transmitter_class, other.transmitter_class)
        return a1 * 10 + a2 * 5 + a3, b1 * 10 + b2 * 5 + b3

    def __gt__(self, other):
        self_size, other_size = self.prior_search(other)
        return self_size > other_size

    def __lt__(self, other):
        self_size, other_size = self.prior_search(other)
        return self_size < other_size

    def __eq__(self, other):
        self_size, other_size = self.prior_search(other)
        return self_size == other_size

    def __ne__(self, other):
        self_size, other_size = self.prior_search(other)
        return self_size != other_size

    def __le__(self, other):
        self_size, other_size = self.prior_search(other)
        return self_size <= other_size

    def __ge__(self, other):
        self_size, other_size = self.prior_search(other)
        return self_size >= other_size

    def __add__(self, other):
        return WaitingLounge(max(self.weight, other.weight),
                             math.floor(sum(self.distance, other.distance) / 2),
                             chr(max(ord(self.transmitter_class), ord(other.transmitter_class))))

    def __isub__(self, other):
        return WaitingLounge(math.floor(self.weight / other.weight),
                             self.distance - other.distance,
                             self.transmitter_class)


    def __floordiv__(self, other):
        

