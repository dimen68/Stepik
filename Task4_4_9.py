str_ = input()
new_str = ''
n = 1
for i in range(len(str_)-1):
    if str_[i] == str_[i+1]:
        n += 1
        if i == (len(str_)-2):
            new_str += str_[i] + str(n)
            break
    else:
        new_str += str_[i] + str(n)
        n = 1
        if i == (len(str_)-2):
            new_str += str_[i+1] + str(n)
print(new_str)