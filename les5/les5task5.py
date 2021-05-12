with open(r'C:\Users\Damir\Desktop\Primer_lesson5\text_5.txt', 'w+', encoding='utf-8') as file_2:
    file_2.write('0 10 20 30 40 50 60')
    file_2.seek(0, 0)
    j = 0
    for a in file_2:
        i = a.rsplit()
        sum_i = sum(int(j) for j in i)
    file_2.write(f" Сумма равна:{str(sum_i)}")
