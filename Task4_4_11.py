str_ = list(input())
answ_ = 'YES'
for i in range(len(str_)-1):
    if str_[i] < str_[i + 1]:
        answ_ = 'NO'
        break
print(answ_)