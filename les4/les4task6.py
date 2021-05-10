from itertools import islice, cycle, count


def number_int():
    try:
        num_start = int(input('Введите начало итератора'))
        num_stop = int(input('Введите конец итератора'))
    except ValueError:
        return "Вы ввели не числа"
    try:
        num_step = int(input('Введите шаг итератора'))
    except ZeroDivisionError:
        return "Вы ввели не праильный шаг"
    num_sum = ((num_stop + 1 - num_start) // num_step)
    int_compreh = [el for el in islice(count(num_start, num_step), num_sum)]
    return int_compreh


def list_cicle(x):
    try:
        a = int(input('Введите сколько раз надо повторить список'))
    except ValueError:
        return 'Вы ввели не число'
    b = a*len(x)
    elem_cycle = [el for el in islice(cycle(x), b)]
    return elem_cycle


list1 = [1, 2, 3, 4, 5, 6]
print(list_cicle(list1))
print((number_int()))
