import random

big_buk = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

small_buk = 'abcdefghijklmnopqrstuvwxyz'

number ='0123456789'

sim = '!@#$%^&*()-_=+[]{};:,.<>?'

sim_from_passwd = ''

passwd = ''

length = int(input("ведите желаемую длину пароля: "))

use_big = input("Нужны ли заглавные буквы? (да/нет): ").lower()

if use_big == 'да':
    sim_from_passwd += big_buk

use_small = input("Нужны ли строчные буквы? (да/нет): ").lower()

if use_small == 'да':
    sim_from_passwd += small_buk
use_number = input("Нужны ли цифры? (да/нет): ").lower()

if use_number == 'да':
    sim_from_passwd += number

use_sim = input("Нужны ли специальные символы? (да/нет): ").lower()

if use_sim == 'да':
   sim_from_passwd += sim

for i in range(length):
    passwd += ''.join(random.choice(sim_from_passwd))
print(passwd)