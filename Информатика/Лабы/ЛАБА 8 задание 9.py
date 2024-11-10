number = int(input('Сколько комнат: '))

i = 0

count = 0

while i < number:
    kom = input('Введите количество людей, которые уже живут в комнате, и максимальное допустимое количество людей через пробел:').split(' ')

    if int(kom[-1]) - int(kom[0]) >= 2:
        count += 1

    i += 1

print(count)
