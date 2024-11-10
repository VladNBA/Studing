a = list(input('Введите текст: '))

print('.'.join(a))
b = input('Введите текст: ')
c = ''

for i in range(len(b)):
    if b[i] != b[-1]:
        c += b[i] + '.'
    else:
        c += b[i]


print(c)