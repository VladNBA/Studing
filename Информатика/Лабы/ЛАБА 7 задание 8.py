general_information = input('Введите результат матча в формате "Название 1-Название 2 A:B": ')

team = ''

scor = ''

number = '1234567890:'

for x in general_information:
    if x not in number:
        team += x
    else:
        scor += x
teams = team.split('-')

score = scor.split(':')

if int(score[0]) > int(score[1]):
    print(teams[0])

elif int(score[0]) < int(score[1]):
    print(teams[1])

else:
    print('Ничья')
