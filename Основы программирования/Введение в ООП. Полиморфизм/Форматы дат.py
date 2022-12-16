class just_Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class AmericanDate(just_Date):

    # Установки

    def set_year(self, new_year):
        self.year = new_year

    def set_month(self, new_month):
        self.month = new_month

    def set_day(self, new_day):
        self.day = new_day

    # Возвраты

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        if self.get_day() > 9 and self.get_month() > 9:
            return f"{self.get_month()}.{self.get_day()}.{self.get_year()}"
        elif self.get_day() < 10 and self.get_month() > 9:
            return f"{self.get_month()}.0{self.get_day()}.{self.get_year()}"
        elif self.get_day() < 10 and self.get_month() < 10:
            return f"0{self.get_month()}.0{self.get_day()}.{self.get_year()}"
        elif self.get_day() > 9 and self.get_month() < 10:
            return f"0{self.get_month()}.{self.get_day()}.{self.get_year()}"


class EuropeanDate(just_Date):

    # Установки

    def set_year(self, new_year):
        self.year = new_year

    def set_month(self, new_month):
        self.month = new_month

    def set_day(self, new_day):
        self.day = new_day

    # Возвраты

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        if self.get_day() > 9 and self.get_month() > 9:
            return f"{self.get_day()}.{self.get_month()}.{self.get_year()}"
        elif self.get_day() < 10 and self.get_month() > 9:
            return f"0{self.get_day()}.{self.get_month()}.{self.get_year()}"
        elif self.get_day() < 10 and self.get_month() < 10:
            return f"0{self.get_day()}.0{self.get_month()}.{self.get_year()}"
        elif self.get_day() > 9 and self.get_month() < 10:
            return f"{self.get_day()}.0{self.get_month()}.{self.get_year()}"
