month = int(input('Введите месяц целым числом от 1 до 12'))
year = ['зима', 'весна', 'лето', 'осень']
if month == 12 or month <= 2:
    print(f'Сейчас время года: {year[0]}')
elif month >= 3 and month <= 5:
    print(f'Сейчас время года: {year[1]}')
elif month <= 8 and month >= 6:
    print(f'Сейчас время года: {year[2]}')
elif month <= 11 and month >= 9:
    print(f'Сейчас время года: {year[3]}')

year_dict = {12: 'зима', 1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето',
             8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень'}
print(f'Сейчас время года: {year_dict.get(month)}')
