import random

money = ['O', 'P']

rez_ = []

rez = random.choice(money)

rez_.append(rez)

helper = rez

count = 0

count_two = 0

while count != 3:

    count_two += 1

#    print(helper, rez, count)

    if helper == rez:
        
        helper = rez
        count += 1

    else:
        count = 1
        helper = rez
        
    if count != 3:
        rez = random.choice(money)
        rez_.append(rez)

print(*rez, end=' ')

print(f'(Попытok: {count_two})')
