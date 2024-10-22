n_str = input('Введите число: ')
n = int(n_str)
answ_ = 'НЕТ'
for i in range(len(n_str)):
    if (n%10) == 5:
        answ_ = 'ДА'
        break
    else:
        n = n//10
        continue
print(answ_)