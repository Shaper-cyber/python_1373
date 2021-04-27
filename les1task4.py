numbers = int(input('Введите целое положительное число'))
imaginary_number = -1
while numbers > 0:
    remainder = numbers % 10
    numbers //= 10
    if remainder > imaginary_number:
        imaginary_number = remainder
print(f'Самое большая цифра в числе {imaginary_number}')