# Заполнить список вещественных чисел вводом с клавиатуры.
# Найте элементы списка, которые меньше среднего арифметического.

# add code here
_list = []

while True:
    user_number = input('Number ? > ')
    if not user_number:
        break
    try:
        _list.append(float(user_number))
    except ValueError:
        print('Wrong number')

if _list:
    avg = sum(_list) / len(_list)

    count = 0
    for number in _list:
        if number < avg:
            count += 1

    print(count)
else:
    print('Empty list')
