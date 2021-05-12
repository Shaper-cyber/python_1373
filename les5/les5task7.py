import json

with open(r'C:\Users\Damir\Desktop\Primer_lesson5\text_7.txt', 'r', encoding='utf-8') as file_1:
    dict_profit = dict()
    sum_profit = 0
    i = 0
    for line in file_1:
        line1 = line.rstrip('\n').split()
        firm = line1[0]
        profit = int(line1[-2]) - int(line1[-1])
        if profit > 0:
            i += 1
            sum_profit += profit
        dict_profit[firm] = profit
    dict_avr_profit = dict()
    dict_avr_profit['average_profit'] = (sum_profit / i)
    list_summary = []
    list_summary.append(dict_profit)
    list_summary.append(dict_avr_profit)
    print(list_summary)
with open(r'C:\Users\Damir\Desktop\Primer_lesson5\text_77new.json', "w+", encoding='utf-8') as write_f:
    json.dump(list_summary, write_f, indent=4, ensure_ascii=False)
