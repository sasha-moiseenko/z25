# Заполнить список вещественных чисел вводом с клавиатуры.
# Сколько элементов списка больше по модулю максимального числа.

_list = []
_max = 0
_count = 0
try:
    while True:
        number = input('> ')
        if not number:
            break
        number = int(number)
        _list.append(number)
except ValueError:
    print('Введите корректное число')
for i in _list:
    if i > _max:
        _max = i
    if abs(i) > _max:
        _count += 1
print(_count, _max)
