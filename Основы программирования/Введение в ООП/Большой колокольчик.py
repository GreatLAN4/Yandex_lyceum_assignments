class BigBell:
    def __init__(self):
        self.ding = True
        self.dong = False

    def sound(self):
        if self.ding:
            print("ding")
            self.ding = False
            self.dong = True

        elif self.dong:
            print("dong")
            self.ding = True
            self.dong = False
