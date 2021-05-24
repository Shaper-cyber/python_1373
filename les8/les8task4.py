'''Тему ооп 8 не понял'''


class Storage:
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
               f" Общее количество техники {OfficeEquip.count}"


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
               f" Общее количество техники {OfficeEquip.count}"


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
               f" Общее количество техники {OfficeEquip.count}"


off1 = Printer('Canon', 3, 'черно-белый', 5670)
off2 = Scanner('Xerox', 7, 'A3', 3280.05)
off3 = Xerox('Dell', 10, 50, 15240.5)
print(off1)
print(off2)
print(off3)
print(OfficeEquip.all_cost)
