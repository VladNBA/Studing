ne_ploxoi = 'не плохой'

ne_ploxa = 'не плоха'

a = input()

if (ne_ploxoi in a.lower()) or (ne_ploxa in a.lower()):
    a = a.replace('неплохой','хороший')
    a = a.replace('неплоха', 'хороша')

print(a)
