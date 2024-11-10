a = input('Введите предложение: ').split(' ')
s = []
print(a)
for i in range(len(a)-1):
    if s.count (a[i]) == 0:
        s.append(a[i])
print(*s)
