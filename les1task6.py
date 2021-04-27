distance = float(input('Введите начальную дистанцию: '))
marathon = float(input('Введите сколько хотите пробежать:'))
day = 1
while marathon > distance:
    print(f'{day}-й день : {distance:.3f}')
    day+=1
    distance*=1.1
print(f'{day}-й день : {distance:.3f}')
print(f'На {day}-й день спорсмен достиг результата - не менее {distance:.3f} км')