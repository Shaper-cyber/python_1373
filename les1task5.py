profit = float(input('Введите прибыль фирмы'))
costs = float(input('Введите издержки фирмы'))
if profit >= costs:
    financial_result = profit - costs
    print(f'Фирма работает с прибылью {financial_result:.2f}')
    revenue = financial_result / profit
    workers = int(input('Введите численность рабочих'))
    work_result = financial_result / workers
    print(f'Прибыль на одного работника {work_result:.2f}, а рентабелность продаж  равна {revenue:.2%}')
else:
    financial_result = costs - profit
    print(f'Фирма работает с убытком {financial_result:.2f}')
