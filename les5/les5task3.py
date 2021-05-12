with open(r'C:\Users\Damir\Desktop\Primer_lesson5\text_3.txt', 'r', encoding='utf-8') as file_1:
    a = 0
    for i in file_1:
        i = i.rstrip('\n').rsplit()
        a = float(i[-1])
        if a <= 20000:
            print(i[0])
    file_1.seek(0, 0)
    b = 0
    for i, k in enumerate(file_1, 1):
        k = k.rstrip('\n').rsplit()
        b += float(k[-1])
    print(b / i)
