number = input('Введите числа через пробел: ').split(' ')

for i in range(len(number)):
    if i != 0 and int(number[i]) > int(number[i - 1]):
        print(number[i])
