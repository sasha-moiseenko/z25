# Вводятся два целых числа.
# Проверить делится ли первое на второе.
# Вывести на экран сообщение об этом, а также остаток (если он есть)
# и частное (в любом случае).
try:
    a = int(input('enter the number > '))
    b = int(input('enter the number > '))
except ValueError:
    print('введите число')
else:
    try:
        if a % b == 0:
            print('a делится на b, ', 'a / b =', a / b)
    except ZeroDivisionError:
        print('error')
    else:
        if a % b != 0:
            print('a не делится на b,', 'a / b =', a / b, ',остаток = ', a % b)
