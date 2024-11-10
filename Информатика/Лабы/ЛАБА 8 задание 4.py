number = input("Vvtdite chiclo, ecli xotite perectat vvoditi nazmite enter: ")

count_number = []
count_number.append(number)

summ = 0

while number != '':
    number = input("Vvtdite chiclo, ecli xotite perectat vvoditi nazmite enter: ")
    
    if number != '':
        count_number.append(int(number))
        summ += int(number)

print(f'{summ / (len(count_number) - 1)}')
