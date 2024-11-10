height = int(input("Vvtdite rost ludei cheloveka: "))
obch_height = input("Vvtdite rost ludei cherez probel: ").split(' ')

count = 0

for i in range(len(obch_height)):
    if int(obch_height[i]) >= height:
        count += 1

print(count + 1)
