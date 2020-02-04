# Заполнить список вещественных чисел вводом с клавиатуры.
# Сколько элементов списка больше по модулю максимального числа.

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

max_number = max(_list)

count = 0
for number in _list:
    if abs(number) > max_number:
        count += 1

print(count)
