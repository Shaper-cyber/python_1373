'''Тему ооп 8 не понял'''


class Date:
    def __init__(self, date):
        self.data = date

    @staticmethod
    def valid(day, month, year):
        if day >= 1 and day <= 31:
            return True
        if month >= 1 and month <= 12:
            return True
        if len(year) == 4:
            return True

    @classmethod
    def transform(cls):
        cls.data = data.split("-")
        cls.data1 = [int(j) for j in cls.data]
        cls.valid(cls.data1[0], cls.data1[1], cls.data1[2])
        return f"{cls.data1[0]:2d}.{cls.data1[1]:2d}.{cls.data1[2]:4d}"


data = "31-12-2021"
a = Date(data)
print(a.transform)
