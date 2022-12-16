class Selector:
    def __init__(self, values):
        self.values = values
        self.odds = list(filter(lambda x: x % 2 != 0, self.values))
        self.evens = list(filter(lambda x: x % 2 == 0, self.values))

    def get_odds(self):
        return self.odds

    def get_evens(self):
        return self.evens
