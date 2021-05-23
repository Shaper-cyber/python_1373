class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print("Машина остановилась")

    def turn(self, dir):
        if dir == 'l':
            print('Влево')
        elif dir == 'r':
            print('Вправо')
        else:
            print('Нет такого направления')

    def show_speed(self):
        # super().__init__()
        # self.speed = speed
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(TownCar, self).__init__(speed, color, name, is_police)
        # self.speed = speed
        # self.color = color
        # self.name = name
        # self.is_police = is_police

    def show_speed(self, speed):
        if speed > 60:
            print('Превышение скорости для городского транспорта')
        else:
            self.speed = speed
            Car.show_speed(self)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(SportCar, self).__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(WorkCar, self).__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        if speed > 40:
            print('Превышение скорости для грузoвого транспорта')
        else:
            self.speed = speed
            Car.show_speed(self)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(PoliceCar, self).__init__(speed, color, name, is_police)


a = TownCar(70, "green", "bus", False)
b = SportCar(100, "blue", "racing", False)
c = WorkCar(60, "red", "truck", False)
d = PoliceCar(60, "white", "police", True)
print(a.speed)
print(b.speed)
print(c.speed)
print(d.speed)
a.go()
a.stop()
a.turn('l')
a.turn('r')
a.show_speed(40)
a.show_speed(60)
a.show_speed(75)
c.go()
c.turn('l')
c.turn('r')
c.show_speed(30)
c.show_speed(45)
c.stop()