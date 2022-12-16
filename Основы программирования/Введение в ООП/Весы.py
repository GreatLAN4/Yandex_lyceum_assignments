class Balance:
    def __init__(self):
        self.weight_right, self.weight_left = 0, 0

    def add_right(self, right):

        self.weight_right += right

    def add_left(self, left):
        self.weight_left += left

    def result(self):
        if self.weight_left > self.weight_right:
            return "L"
        elif self.weight_right > self.weight_left:
            return "R"
        else:
            return "="
