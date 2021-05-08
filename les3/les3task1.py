def divide():
    try:
        a = int(input('введите первое число'))
        b = int(input('введите второе число'))
        c = a / b
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    except ValueError:
        return 'Вы ввели символы, а не цифры'
    else:
        return c

print(divide())
print('конец')

