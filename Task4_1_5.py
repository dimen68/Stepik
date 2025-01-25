a = int(input())
b = int(input())
if a < b:
    n1, n2, s = a, b+1, 1
else:
    n1, n2, s = a, b-1, -1
for i in range(n1, n2, s):
    print(i)