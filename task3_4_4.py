import os.path

file = os.path.join('C:\\Users\\User\\Downloads\\dataset_3363_4.txt')
file_answer = os.path.join('C:\\Users\\User\\Downloads\\answer.txt')
abit = 0
ans_ = ''
mat = 0
fiz = 0
rus = 0
with open(file, 'r') as fr:
    while True:
        raw_line = fr.readline().split(';')
        if raw_line==['']:
            break
        print(raw_line)
        ans_ += str(round(
            (int(raw_line[1])+int(raw_line[2])+int(raw_line[3]))
            / 3 ,9)) + '\n'
        abit += 1
        mat += int(raw_line[1])
        fiz += int(raw_line[2])
        rus += int(raw_line[3])
ans_ += str(round(mat / abit ,9))+' '
ans_ += str(round(fiz / abit ,9))+' '
ans_ += str(round(rus / abit ,9))+' '
print(ans_)
with open(file_answer, 'w') as new:
    new.write(ans_)

