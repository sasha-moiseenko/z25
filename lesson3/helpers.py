__all__ = (
    'my_sum',
    'get_user_input_list'
)


def my_sum(a, b):
    return a + b


def get_user_input_list():
    _list = []
    while True:
        number = input('Number ? >')
        if not number:
            break
        try:
            number = float(number)
        except ValueError:
            pass
        else:
            _list.append(number)
    return _list


if __name__ == '__main__':
    print('HERE' * 20)
    print(get_user_input_list())
