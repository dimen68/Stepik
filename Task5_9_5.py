# Задание 5.9.5  - Шашки

mas = []
for i in range(8):
    row = str()
    for j in range(8):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2  and j % 2 ):
            row += '.'
        elif i <= 2:
            row += 'B'
        elif i >= 5:
            row += 'W'
        else:
            row += '.'
    mas.append(row)

for i in mas:
    print(i)
