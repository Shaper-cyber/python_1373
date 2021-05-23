class Cell:
    def __init__(self, count: int):
        self.count = count

    def __str__(self):
        return f"Количество клеток {self.count}"

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count >= other.count:
            return Cell(self.count - other.count)
        else:
            return "нельзя"

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, amount):
        stroke = self.count // amount
        if stroke < 1:
            return ("*" * self.count) + "\n"
        else:
            return '\n'.join(['*' * amount for _ in range(stroke)]) + "\n" + "*" * (self.count % amount) + "\n"


a = Cell(14)
b = Cell(25)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a.make_order(5))
print(b.make_order(4))
