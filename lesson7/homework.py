"""1. Написать кэширующий декоратор,
который принимает время (в секундах, сколько необюходимо хранить результат)
"""
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

@cache(60)  # значит что результат функции foo будет хранится 60 секунд
def foo():
    pass


"""
2.
Написать декоратор, который считает сколько раз была вызвана функция и выводит
эту информации на экран.
В качестве аргумента(необязательного) декоратор может принимать
текст(форматированный), который
будет выводиться вместе с количеством вызовов. Если данный аргумент не передан,
то выводить текст по умолучанию(любой)
@counter():
def foo():
    return 1
foo(123)
>>> 'Count - 1'
>>> 1
foo("asd")
>>> 'Count - 2'
>>> 1
@counter("Text {}"):
def foo1():
    return 1
>>> 'Text 1'
>>> 1
"""


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


"""3.
Написать функцию, которая извлекает даты из строки.'
Допускаем что во всех месяцах 31 день
get_datetimes('Lorem Ipsum is simply 12-01-2018 dummy text of
the printing 10-13-2018 and typesetting industry.
10-02-2018 Lorem Ipsum has been the industry a s x')
>>> ['12-01-2018', '10-02-2018']"""



def find_time(string):
    pattern = re.compile(r'((?:0?[1-9]|[12][0-9]|3[01])-(?:(?:[0-1]\d)|(?:2[0-3]))-[0-5]\d[0-5]\d)')
    return tuple(pattern.findall(string))

""4.
Написать функцию, которая извлекает все слова,
начинающиеся на гласную(согласную). Какие слова извлекать - аргумент функции
get_words('Lorem Ipsum is simply', sym=('consonants', 'vowels'))
>>> ['Lorem', 'Ipsum', 'is', 'sumply']
get_words('Lorem Ipsum is simply', sym=('consonants',))
>>> ['Lorem', 'sumply']
get_words('Lorem Ipsum is simply', sym=('vowels',))
>>> ['Ipsum', 'is']



def get_words(str, sym):
    if sym[0] == ('consonants',):
        pattern = re.compile(r'(?<=/^|\s)(?i:[aeiouy])[\w\-]*')
        return tuple(pattern.findall(str))
    elif sym[0] == ('vowels',):
        pattern = re.compile(r'(?<=/^|\s)(?i:[qwrtplkjhgfdszxcvbnm])[\w\-]*')
        return tuple(pattern.findall(str))
    else:
        pattern = re.compile(r'\b[a-zA-Z]\w*')
        return tuple(pattern.findall(str))


"""5. Написать функцию, которая группирует результат команды ping
((<icmp_seq>, <ttl>), ...)
s = "64 bytes from 216.58.215.110: icmp_seq=0 ttl=54 time=30.391 ms
64 bytes from 216.58.215.110: icmp_seq=1 ttl=54 time=30.667 ms
64 bytes from 216.58.215.110: icmp_seq=2 ttl=54 time=33.201 ms
64 bytes from 216.58.215.110: icmp_seq=3 ttl=54 time=30.140 ms
64 bytes from 216.58.215.110: icmp_seq=4 ttl=54 time=31.822 ms"
get_result(s)
>>> ((0, 30.391), (1, 30.667), (2, 33.201), (3, 30.140), (4, 31.822))
"""


def get_ping_info(*args, **kwargs):
    pattern = re.compile(r'(?<=\=)(\d{1,}\.?)*')
    return tuple(pattern.findall(ping))
if __name__ == "__main__":
    pass
