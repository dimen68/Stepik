n=int(input())
mat=[[0 for i in range(n)] for j in range(n)]
t=n
j_n=0
i_n=0
s=1
nap_gor=1
nap_vert=-1
for i in range(i_n,t,nap_gor):
  mat[j_n][i]=s
  s+=1
  i_n=i
t-=1
while t>0:
  nap_vert=-(nap_vert)
  nap_gor=-(nap_gor)
  j_n+=nap_vert
  for j in range(j_n,(j_n+nap_vert*t),nap_vert):
    mat[j][i_n]=s
    s+=1
    j_n=j
  i_n+=nap_gor
  for i in range(i_n,(i_n+nap_gor*t),nap_gor):
    mat[j_n][i]=s
    s+=1
    i_n=i
  t-=1
for j in range(len(mat)):
    for i in range(len(mat[0])):
        print(mat[j][i], end=' ')
    print()
