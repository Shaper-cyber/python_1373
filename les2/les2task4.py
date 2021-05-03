lines = input('Введите несколько строк через пробел')
i = 1
for line in lines.split():
    print(f'{i} {line[:10]}')
    i += 1
