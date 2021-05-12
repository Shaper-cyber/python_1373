with open(r'C:\Users\Damir\Desktop\Primer_lesson5\text_4.txt', 'r', encoding='utf-8') as file_1:
    b = ["Один", "Два", "Три", "Четыре"]
    j = 0
    with open(r'C:\Users\Damir\Desktop\Primer_lesson5\text_4_new.txt', 'w', encoding='utf-8') as file_2:
        for i in file_1:
            i = i.rsplit()
            i[0] = b[j]
            j += 1
            i= " ".join(i)
            file_2.write(i + '\n')
