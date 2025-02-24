import os.path

file = os.path.join('C:\\Users\\User\\Downloads\\dataset_3363_2.txt')
with open(file, 'r') as fr:
    raw_str = fr.read()+' '
#raw_str = 'a3b4c2e10b1 ' # тестовая строчка
full_str = ''
n_str = ''
key=''
for i in raw_str:
    if not i.isdigit():
        if n_str:
            full_str += key * int(n_str)
            n_str = ''
        key = i
    else:
        n_str += i
print(full_str)