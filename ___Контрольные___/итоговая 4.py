class WaitingLounge:
    def __init__(self, name_planet, list_points, volume):
        self.name_planet = name_planet
        self.list_points = list_points
        self.volume = volume

    def get_destinations(self):
        return self.list_points

    def __str__(self):
        return f"The waiting lounge on the planet {self.name_planet}" \
               f" accommodates {self.volume} passengers."

    def __repr__(self):
        return f"WaitingLounge('{self.name_planet}', " \
               f"{sorted(self.list_points)}, {self.volume})"

    def sol(self, a, b):
        if a > b:
            return 1, 0
        elif a == b:
            return 0, 0
        else:
            return 0, 1

    def prior_search(self, other):
        a1, b1 = self.sol(len(self.list_points), len(other.list_points))
        a2, b2 = self.sol(self.volume, other.volume)
        a3, b3 = self.sol(self.name_planet, other.name_planet)
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
        return WaitingLounge(min(self.name_planet, other.name_planet),
                              sorted(set(self.list_points) & set(other.list_points)),
                              self.volume + other.volume)


wl = WaitingLounge("Tau", ["Centauri", "Eridanus"], 500)
wl1 = WaitingLounge("Epsilon", ["Vega", "Eridanus"], 500)
print(wl > wl1, wl != wl1, wl <= wl1)
wl2 = wl + wl1
print(wl, wl1, wl2, *wl2.get_destinations(), sep="\n")
