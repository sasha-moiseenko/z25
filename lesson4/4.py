# Перевести число, введенное пользователем,
# в байты или килобайты в зависимости от его выбора.

# add code here
try:
    number = int(input('Number ? >'))
except ValueError:
    print('Invalid number')
else:
    choice = input('Bytes(b) or kBytes(k)? > ')
    value = None
    if choice == 'b':
        value = number * 1024
    elif choice == 'k':
        value = number / 1024
    else:
        print('Invalid choice')
