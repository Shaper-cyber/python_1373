'''Тему ооп 8 не понял'''


class Storage:
    def __init__(self, count=0, all_cost=0):
        self.count = count
        self.all_cost = all_cost

    def accept(self):
        pass


class OfficeEquip:
    count = 0
    all_cost = 0


class Printer(OfficeEquip):
    def __init__(self, name: str, count: int, printing: str, price: float):
        self.name = name
        self.count = count
        self.printing = printing
        self.price = price
        OfficeEquip.count += self.count
        OfficeEquip.all_cost += self.price * self.count

    def __str__(self):
        return f"Прибыл {self.printing} принтер фирмы {self.name} в количестве {self.count} шт." \
               f" Общее количество оргтехники {OfficeEquip.count}"


class Scanner(OfficeEquip):
    def __init__(self, name: str, count: int, formating: str, price: float):
        self.name = name
        self.count = count
        self.formating = formating
        self.price = price
        OfficeEquip.count += self.count
        OfficeEquip.all_cost += self.price * self.count

    def __str__(self):
        return f"Прибыл {self.formating} сканер фирмы {self.name} в количестве {self.count} шт." \
               f" Общее количество оргтехники {OfficeEquip.count}"


class Xerox(OfficeEquip):
    def __init__(self, name: str, count: int, speed: int, price: float):
        self.name = name
        self.count = count
        self.speed = speed
        self.price = price
        OfficeEquip.count += self.count
        OfficeEquip.all_cost += self.price * self.count

    def __str__(self):
        return f"Прибыл ксерокс фирмы {self.name} со скоростью копирования {self.speed}  " \
               f"в количестве {self.count} шт." \
               f" Общее количество оргтехники {OfficeEquip.count}"
