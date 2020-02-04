# import helpers

# from helpers import get_user_input_list, my_sum

from helpers import get_user_input_list
from utils import my_sum as utils_my_sum  # noqa


def main():
    items = []

    _sum = 0
    _mul = 1

    for number in get_user_input_list():
        _sum += number
        _mul *= number

    print(items)
    print(_sum, _mul)


if __name__ == '__main__':
    main()
