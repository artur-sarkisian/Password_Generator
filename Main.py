# Генератор безопасных паролей
# Описание проекта: программа генерирует заданное количество паролей и включает
# в себя умную настройку на длину пароля,
# а также на то, какие символы требуется в него включить, а какие исключить.
# Программа должна запрашивать у пользователя следующую информацию:
# Количество паролей для генерации;
# Длину одного пароля;
# Включать ли цифры 0123456789?
# Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
# Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
# Включать ли символы !#$%&*+-=?@^_?
# Исключать ли неоднозначные символы il1Lo0O?

from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuations = '!#$%&*+-=?@^_'
chars = ''


numb_of_pass = input('Укажите количество паролей: ')
len_pass = input('Укажите длину пароля: ')
pass_digit = input('Включать ли в пароль цифры от 0 до 9? (y/n)\n')
pass_lowercase = input('Включать ли в пароль прописные буквы? (y/n)\n')
pass_uppercase = input('Включать ли в пароль строчные буквы? (y/n)\n')
pass_punctuations = input('Включать ли в пароль символы: "!#$%&*+-=?@^_"? (y/n)\n')
pass_exclude = input('Исключать ли неоднозначные символы: "il1Lo0O"? (y/n)\n')

def generate_password(length, chars):
    password = ''
    for _ in range(int(length)):
        password += choice(chars)
    return password


if pass_digit == 'y':
    chars += digits
if pass_lowercase == 'y':
    chars += lowercase_letters
if pass_uppercase == 'y':
    chars += uppercase_letters
if pass_punctuations == 'y':
    chars += punctuations
if pass_exclude == 'y':
    for i in chars:
        if i in "il1Lo0O":
            chars = chars.replace(i, '')


for j in range(int(numb_of_pass)):
    print(generate_password(len_pass, chars))



