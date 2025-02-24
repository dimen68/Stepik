raw = input().lower().split()
d = {}
for i in raw:
    n = raw.count(i)
    d[i] = n
for key, value in d.items():
    print(f'{key} {value}')