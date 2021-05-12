with open(r'C:\Users\Damir\Desktop\Primer_lesson5\text_6.txt', 'r', encoding='utf-8') as file_1:
    dict_lesson = dict()
    for line in file_1:
        line1 = line.replace('(', " ").replace(')', " ").replace(':', " ").split()
        a = line1[0]
        b = 0
        for num in line1:
            if num.isdigit():
                b += int(num)
        dict_lesson[a] = b
print(dict_lesson)