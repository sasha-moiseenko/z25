import time

#
# def cache(func):
#     def decorator(*args, **kwargs):
#         if not hasattr(cache, '_cache'):
#             cache._cache = {}
#         cache_key = (args, tuple(sorted(kwargs.items(), key=lambda item: item[0])))
#         result = cache._cache.get(cache_key)
#         if not result:
#             result = func(*args, **kwargs)
#             cache._cache[cache_key] = result
#         return result
#     return decorator


def cache(sec):
    def inner(func):
        def decorator(*args, **kwargs):

            if not hasattr(cache, '_cache'):
                cache._cache = {}
            print(cache._cache)
            cache_key = func.__name__
            value = cache._cache.get(cache_key)
            if not value:
                value = {'result': func(*args, **kwargs), 'created_time': time.time()}
                cache._cache[cache_key] = value
            else:
                now = time.time()
                if now - value['created_time'] > sec:
                    del value[func.__name__]
            return value
        return decorator
    return inner

import random

@cache(5)
def func():
    return random.randint(1, 100)
x = 0
while x < 10:
    time.sleep(func)
    x += 1
