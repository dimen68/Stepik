a = int(input('Введите число: '))
a_ = a - int(a % 2 == 0)
b = int(input())
for i in range(a_,b-1,-2):
    print(i)