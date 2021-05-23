from abc import ABC, abstractmethod


class Clothes(ABC):
    _fabric_consumption = 0

    @property
    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    # cloth_coat = 0

    def __init__(self, clothing_size, quantity_coat):
        self.clothing_size = clothing_size
        self.quantity_coat = quantity_coat
        self.cloth_coat = 0

    @property
    def calculate(self):
        self.cloth_coat += int(self.quantity_coat) * float((self.clothing_size / 6.5) + 0.5)
        Clothes._fabric_consumption += self.cloth_coat
        return f'Количество ткани на пальто - {self.cloth_coat},' \
               f' общее количество ткани {Clothes._fabric_consumption}'


class Overalls(Clothes):
    cloth_over = 0

    def __init__(self, growth, quantity_overalls):
        self.growth = growth
        self.quantity_overalls = quantity_overalls


    @property
    def calculate(self):
        self.cloth_over = int(self.quantity_overalls) * float((2 * self.growth) + 0.3)
        Clothes._fabric_consumption += self.cloth_over
        return f'Количество ткани на комбинезоны - {self.cloth_over}, ' \
               f'общее количество ткани - {Clothes._fabric_consumption}'

    # @property
    # def getcloth(self):
    #     return self.cloth_over


a = Coat(6.5, 1)
b = Overalls(180, 1)
print(a.calculate)
print(b.calculate)
c = Coat(65,5)
print(c.calculate)
d = Overalls(165,5)
print(d.calculate)
