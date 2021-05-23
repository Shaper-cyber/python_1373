class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f'Общий доход с учетом премии равен: {sum(self._income.values())}'


a = Position("Damir", 'Araslanov', 'Operator', 50000, 20000)
print(a.name)
print(a.surname)
print(a.position)
print(a._income)
print(a.get_full_name())
print(a.get_total_income())
