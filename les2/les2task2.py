elements = input('Введите список')
elements = list(elements)
empty_list = []
if len(elements) % 2 == 0:
    i = 0
    j = 1
    while len(elements) > len(empty_list):
        empty_list.insert(j, elements[i])
        empty_list.insert(i, elements[j])
        i += 2
        j += 2
else:
    i = 0
    j = 1
    x = elements.pop(len(elements) - 1)
    while len(elements) > len(empty_list):
        empty_list.insert(j, elements[i])
        empty_list.insert(i, elements[j])
        i += 2
        j += 2
    empty_list.append(x)
elements = empty_list
print(elements)
