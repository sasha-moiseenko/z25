# Заполнить список вещественных чисел вводом с клавиатуры.
# Найте элементы списка, которые меньше среднего арифметического.

_list = []
_sum = 0
_avg = 0
small_list = []
try:
    while True:
        number = input('> ')
        if not number:
            break
        number = int(number)
        _list.append(number)
except ValueError:
    print('Введите корректное число')
try:
    for i in _list:
        _sum += i
    _avg = _sum / len(_list)
except ZeroDivisionError:
    print('Деление на ноль запрещено: проверьте вводные данные')
    for i in _list:
        if i < _avg:
            small_list.append(i)
print('среднее арифметическое > ', _avg, small_list)


