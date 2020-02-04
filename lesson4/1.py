# Вводятся два целых числа.
# Проверить делится ли первое на второе.
# Вывести на экран сообщение об этом, а также остаток (если он есть)
# и частное (в любом случае).

try:
    num_1 = int(input("Number 1 ? >"))
    num_2 = int(input("Number 2 ? >"))
except ValueError:
    print('Error, not a number')
else:
    if not num_2:
        print('Zero division')
    else:
        mod = num_1 % num_2
        div = num_1 // num_2
        print('Делится' if mod else 'Не делится')
        print(div, mod)
