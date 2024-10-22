n = int(input())
del_ = [1]
i = 2
j = 0
while i <= n:
    if n % i == 0:
        del_.append(i)
        if i != n:
            j = 1
    i += 1
if j == 1:
    answ_ = 'НЕТ'
else:
    answ_ = 'ПРОСТОЕ'
print(*del_)
print(answ_)