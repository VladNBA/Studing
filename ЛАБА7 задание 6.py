a = input('Введите зашифрованное слово и поставьте в конце #: ')
b = ''
e = ''
for i in range(len(a)):
    if a[-1] == '#':
        if i == 0:
            b += a[i]
        elif i == 1:
            e += a[i]
        elif a[i] == '#':
            continue

        else:
            b += a[i]
    else:
        print('Ошибка! Отсутствует символ #')
        break

b += e
print(b)