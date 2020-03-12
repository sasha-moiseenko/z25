# def introduce_on_debug(debug=True):
#     def inner(func):
#         def decorator(*args, **kwargs):
#             if debug:
#                 return func(*args, **kwargs)
#             else:
#                 return func.__name__
#             return decorator
#         return inner
#
# @introduce_on_debug
# def identity(x):
#     return x
#
# print(identity(57))


# a = (1, 2, 3)
# b = a[::-1]
# print(b)

# def flip(func):
#     def decorator(*args, **kwargs):
#         reversed_args = args[::-1]
#         return func(*reversed_args, **kwargs)
#     return decorator
#
#
# # def flip(func):
# #     def decorator(*args, **kwargs):
# #         args = args[::-1]
# #         return func(*args, **kwargs)
# #     return decorator
#
#
# @flip
# def div(x, y, show=False):
#     res = x / y
#     if show:
#         print(res)
#     return res


# def introduce_on_debug(debug):
#     def inner(func):
#         def decorator(*args, **kwargs):
#             if debug:
#                 return func(*args, **kwargs)
#             else:
#                 return func.__name__
#         return decorator
#     return inner
#
#
# @introduce_on_debug(debug=False)
# def identity(x):
#     return x
#
#
# print(identity(57))


# def print_given(*args, **kwargs):
#     result = ''
#     print(kwargs)
#     for arg in args:
#         _type = type(arg)
#         result += f'{arg} {_type}\n'
#     for key in kwargs:
#         result += f'{key} {kwargs[key]} {type(kwargs[key])}\n'
#     return result
#
#
# print(print_given(1, 2, [1, 2], 'str', two = 2))

import time
def timer(func):
    def decorator(*args, **kwargs):
        start_time = time.time()
        return func.__name__, time.time() - start_time
    return decorator


@timer
def identity(x):
    time.sleep(100)
    return x


print(identity(57))

def counter(func):
    def decorator(*args, **kwargs):
        if not hasattr(counter, '_counter'):
            counter._counter = {}
        counter_key = func.__name__
        result = counter._counter.get(counter_key, 1)
        if counter_key:
            result = counter._counter.get(counter_key, 0) + 1
        counter._counter[counter_key] = result
        return result
    return decorator