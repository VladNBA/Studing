nomer = input('Vvelite nomer karti: ')

chet = 0
ne_chet = 0

vrem = 0

summ = 0

for i in range(len(nomer)):

    if (i+1) % 2 == 0:
        chet += int(nomer[i])
        print(f'CHETNIE: {int(nomer[i])}')
    else:
        vrem = int(nomer[i]) * 2
        print(f'NECHETNIE: {int(nomer[i])}')

        if vrem > 9:
            vrem -= 9
        ne_chet += vrem

summ = chet + ne_chet

if summ % 10 == 0:
    print('Корректный ноиер')

else:
    print('Некорректный номер')

