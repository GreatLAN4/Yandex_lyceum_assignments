class Profile:
    def __init__(self, vocation):
        self.vocation = vocation

    def info(self):
        return ''

    def describe(self):
        print(self.vocation, self.info())


class Vacancy(Profile):
    def __init__(self, profile, salary):
        super().__init__(profile)
        self.salary = salary

    def info(self):
        return f'Предлагаемая зарплата: {self.salary}'


class Resume(Profile):
    def __init__(self, profile, salary):
        super().__init__(profile)
        self.salary = salary

    def info(self):
        return f'Стаж работы: {self.salary}'