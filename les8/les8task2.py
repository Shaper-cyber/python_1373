class Zero(Exception):
    def __init__(self, *args):
        if args:
            self.txt = args[0]

    def __str__(self):
        if self.txt:
            return f"Ошибка деления на ноль"


a = int(input('Введите делимое: '))
b = int(input("Введите делитель: "))
try:
    if b == 0:
        raise Zero('Ноль b')
except Zero as zer:
    print(zer)
else: print("Все норм")


