import os.path

file = os.path.join('C:\\Users\\User\\Downloads\\dataset_3363_3.txt')
with open(file, 'r') as fr:
    raw_str = fr.read().lower().split(' ')
    print(raw_str)
#raw_str = 'a3b4c2e10b1 ' # тестовая строчка
dic={}
for i in raw_str:
    if i in dic.keys():
        dic[i]+=1
    else:
        dic[i]=1
for key,value in dic.items():
    print(key, value)
max_n=max(dic.values())
max_keys=[]
for key, value in dic.items():
    if value==max_n:
        max_keys+=key
max_key=max(max_keys)
print(max_key, max_n)