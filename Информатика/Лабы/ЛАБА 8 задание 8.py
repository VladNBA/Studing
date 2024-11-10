i = int(input('Сколько слов: '))

for x in range(i):
    word = input('Введите слово: ')

    if len(word) < 10:
        print(word)

    else:
        print(f'{word[0]}{len(word) - 2}{word[-1]}')
