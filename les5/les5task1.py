file_obj = open("les5task01.txt", 'w', encoding="UTF-8")

for i in range(4):
    text = input("Введите о себе данные через Enter: Имя, Фамилия, дата рождения, город проживания")
    file_obj.write(f'{text}\n')

file_obj.close()
