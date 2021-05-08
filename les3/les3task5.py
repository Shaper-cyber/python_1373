def sum_int():
    global a
    a = 0
    while True:
        list_number = input('Введите строку чисел, разделенную пробелами, чтоб выйти введите q ')
        list_number = list_number.split(" ")
        if list_number[-1] == 'q' or list_number == 'Q':
            list_number.pop(-1)
            list_number = [int(i) for i in list_number]
            a += sum(list_number)
            break
        elif list_number[-1] != 'q' or list_number != 'Q':
            list_number = [int(i) for i in list_number]
            a += sum(list_number)
            print(f'Сумма чисел = {a}')
    return a



print(sum_int())