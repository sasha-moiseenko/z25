# Перевести число, введенное пользователем,
# в байты или килобайты в зависимости от его выбора.

try:
    number = int(input('enter the number > '))
except ValueError:
    print('введите число')
else:
    measure = input('choose: if kilobytes type kb, if megabytes type mb > ')
    if measure == 'kb':
        print(number / 1024, 'mbytes')
    elif measure == 'mb':
        print(number * 1024, 'kbytes')
    else:
        print('введите единицу измерения в корректном формате')
