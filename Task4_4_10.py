str_ = input()
s = 0
for i in range(len(str_)):
    if str_[i].isdigit:
        if i != len(str_) and str_[i+1].isdigit():
            n = int(str_[i] + str_[i+1])
            s += n
        else:
            s += int(str_[i])
    else:
        continue
print(s)