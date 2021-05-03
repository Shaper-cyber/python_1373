list_of_products = []
i = 1
for _ in range(3):
    title = input('Введите название товара: ')
    price = float(input('Введите стоимость товара: '))
    quantity = int(input('Введите количество товара: '))
    unit_of_measurement = input('Введите единицу измерения: ')
    dictionsry = {'название' : title, 'цена' : price, 'Количество' : quantity, 'ед.' : unit_of_measurement}
    print(dictionsry)
    product = (i, dictionsry)
    print(product)
    list_of_products.append(product)
    print(list_of_products)
    print(type(list_of_products))
    i+=1
print(list_of_products)