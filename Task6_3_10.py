# Задание 6.3.10  - Шашки 2.0

mas = []
col_raw ='ABCDEFGH'
row_raw = '87654321'

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

def move():
    col1 = col_raw.index(input())
    row1 = row_raw.index(input())
    col2 = col_raw.index(input())
    row2 = row_raw.index(input())
    fig1 = mas[row1][col1:col1+1]
    fig2 = mas[row2][col2:col2+1]
    mas[row1] = mas[row1][:col1] + fig2 + mas[row1][col1+1:]
    mas[row2] = mas[row2][:col2] + fig1 + mas[row2][col2+1:]


move()
for i in mas:
    print(i)