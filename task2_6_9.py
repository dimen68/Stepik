mat1 = []
mat2 = []
rez_i = 0
rez_j = 0
while True:
    x = input()
    if x == 'end':
        break
    else:
        mat1.append([int(k) for k in x.split()])
        rez_i = len(x.split())
        rez_j += 1
print(mat1[0])
print(mat1[1])
print(mat1[2])
for j in range(rez_j):
    new_row=[]
    for i in range(rez_i):
        t = j - 1
        if j == 0:
            t = rez_j - 1
        b = j + 1
        if j == rez_j - 1:
            b = 0
        l = i - 1
        if i == 0:
            l = rez_i - 1
        r = i + 1
        if i == rez_i - 1:
            r = 0
        print(mat1[l][j], mat1[r][j],
                              mat1[i][t], mat1[i][b])
        new_row.append(mat1[l][j] + mat1[r][j] + mat1[i][t] + mat1[i][b])
    mat2.append(new_row)
for j in range(len(mat2)):
    for i in range(len(mat2[0])):
        print(mat2[j][i], end=' ')
    print()


