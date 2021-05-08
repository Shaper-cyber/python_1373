# number = int(input("Введите число: "))
# print(number+2)
#number = int(input("Введите число: "))
#while number <= 0 or number >= 10:
  #  print("Число не верное, введите больше 0 и меньше 10")
  #  number = int(input("Введите число: "))
#number = number ** 2
#print("Верно " + str(number))
name = input("Введите имя: ")
familia = input("Введите фамилию: ")
age = int(input("Введите возраст: "))
ves = int (input("Свой вес: "))
if age <= 30 and (ves >= 50 and ves <= 120):
    print( name, familia, age,'год,', 'вес -', ves,'хорошее состояние', sep=" ")
elif (age >= 30 and age <= 40) and (ves <= 50 or ves >= 120):
    print(name, familia, age, 'год', 'вес -', ves, 'занятся собой.', sep=" ")
else:
    print( name, familia, age,'год', 'вес -', ves,'обратится к врачу', sep=" ")