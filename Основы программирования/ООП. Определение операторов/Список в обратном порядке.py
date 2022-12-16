class ReversedList:
    def __init__(self, lst):
        self.lst_reverse = lst[::-1]

    def __len__(self):
        return len(self.lst_reverse)

    def __getitem__(self, key):
        return self.lst_reverse[key]
