second = int(input('Введите время в секундах: '))
hour = second // 3600
minute = (second // 60) % 60
second = (second % 60) % 60
print(f'{hour:02d}:{minute:02d}:{second:02d}')