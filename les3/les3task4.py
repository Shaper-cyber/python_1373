# def my_func():
#     try:
#         x = float(input('Введите любое число: '))
#         y = int(input('Введите отрицательное целое число'))
#     except ValueError:
#         return "Вы ввели не числа"
#     if y > 0: return 1/(x**y)
#     else: return x**y
#
#
# print(my_func())


def my_func():
    try:
        x = float(input('Введите любое число: '))
        y = int(input('Введите отрицательное целое число: '))
    except ValueError:
        return "Вы ввели не числа"
    a = 1
    if y > 0:
        for i in range(1, y):
            a *= x*x
        return 1 / a
    else:
        for i in range(1, abs(y)):
            a *= x*x
        return 1 / a


print(my_func())
