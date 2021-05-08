def int_func(str_):
    a = str_[0]
    a = ord(a)
    return str_.replace(str_[0], chr(a-32), 1)


strokes = input('Введите несколько строк через пробел: ')
a = strokes.split(" ")
b = []
for i in a:
    b.append(int_func(i))
print(" ".join(b))
