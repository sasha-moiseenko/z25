# Вводятся два целых числа.
# Проверить делится ли первое на второе.
# Вывести на экран сообщение об этом, а также остаток (если он есть)
# и частное (в любом случае).

try:
    a = int(input('enter the number > '))
    b = int(input('enter the number > '))
    if a % b == 0:
        print('a делится на b, ', 'a / b =', a / b)
    else:
        print('a не делится на b,', 'a / b =', a / b, ',остаток = ', a % b)
except ZeroDivisionError as exc:
    print(exc, '> введите корректное число в делитель')
