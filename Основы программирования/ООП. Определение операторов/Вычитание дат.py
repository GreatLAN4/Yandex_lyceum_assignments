import datetime as dttm


class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        time1 = dttm.date(2022, self.month, self.day)
        time2 = dttm.date(2022, other.month, other.day)
        answer = str(time1 - time2).split()
        return answer[0] if len(answer) != 1 else 0
