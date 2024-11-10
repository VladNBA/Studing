import random

number = []

for i in range(6):
    number.append(random.randint(1, 49))

print(*number)
