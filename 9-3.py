﻿import csv
file = open('data.csv', 'r',encoding='utf8')
data = list(csv.reader(file, delimiter=';'))
print("Нужно купить:")
for i in data:
    print(f'{i[0]} - {i[1]} шт. за {i[2]} руб.')
print(f"итоговая сумма: {sum([int(i[1]) * int(i[2]) for i in data])} руб.")
