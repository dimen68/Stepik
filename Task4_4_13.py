str_ = input()
matr_pic =[]
for i in range(0,len(str_),2):
    row_ = ''
    bin_ = list(str((bin(int((str_[i] + str_[i+1]), 16))[2:])))
    if len(bin_) < 8:
        bin_.reverse()
        for k in range(8 - len(bin_)):
            bin_.append('0')
        bin_.reverse()
    for j in range(len(bin_)):
        if bin_[j] == '0':
            bin_[j] = ' '
        else:
            bin_[j] = '*'
    for l in bin_:
        row_ += l
    matr_pic.append(row_)
for i in matr_pic:
    print(i)
