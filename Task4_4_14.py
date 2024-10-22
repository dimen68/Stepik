n = int(input())
all_ =[]
iq_ =[]
for i in range(n):
    iq_pers = int(input())
    all_.append(iq_pers)
    if sum(all_) == iq_pers:
        iq_.append(0)
    elif iq_pers > (sum(all_)/len(all_)):
        iq_.append('>')
    else:
        iq_.append('<')
for j in range(n):
    print(iq_[j])
