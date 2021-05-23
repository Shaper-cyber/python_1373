import time


class TrafficLight():
    __color = ''

    def running(self):
        print('Красный')
        time.sleep(7)
        print('Желтый')
        time.sleep(2)
        print('Зеленый')
        time.sleep(8)


a = TrafficLight()
a.running()
