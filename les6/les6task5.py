class Stationery:
    """Канцелярская принадлежность"""

    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки.')


class Pen(Stationery):
    """Ручка, род класс Канцелярской принадлежности"""

    def draw(self):
        print(f'Рисует ручка {self.title}')


class Pencil(Stationery):
    """Карандаш, род класс Канцелярской принадлежности"""

    def draw(self):
        print(f'Рисует карандаш {self.title}')


class Handle(Stationery):
    """Маркер, род класс Канцелярской принадлежности"""

    def draw(self):
        print(f'Рисует маркер {self.title}')


a = Stationery('All')
a.draw()
b = Pen("Pen")
b.draw()
c = Pencil("Pencil")
c.draw()
d = Handle("Handle")
d.draw()
