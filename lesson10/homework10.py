# class MyStr(str):
#     def __lt__(self, other):
#         print(self, other)
#         print(type(self))
#         return self + other > other + self
#
#
# def max_number(_list):
#
#     return int(''.join(sorted(map(MyStr, _list)))) if _list else None
#     # print(sorted(map(MyStr, _list)))
#
# print(max_number([234, 123, 98, 467, 99]))


'''1.
Напишите менеджер контекста MultiFileOpen, который позволяет работать с
несколькими файлами:
MultiFileOpen(('file1.txt', 'r'), ('file2.txt', 'w'), ..., ('fileN.txt', 'rb'))
'''


# with open('newfile.txt', 'w', encoding='utf-8') as g:
#     d = int(input())
#     print('1 / {} = {}'.format(d, 1 / d), file=g)


class MultiFileOpen:
    def __init__(self, *args):
        self.args = args

    def __enter__(self):
        n = 0
        for i in range(len(self.args)):
            self.file = self.args[n][0]
            self.flag = self.args[n][1]
            self.fp = open(self.file, self.flag)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()


"""
2.
Напишите менеджер контекста Timer, который позволяет получать текущее время
выполнения кода (отсчет начинается с конструкции with):
with Timer("Time: {}") as timer:
    do_some_logic()
    print(timer.now())  # Time: 3.4123 sec
    do_some_other_logic()
    print(timer.now())  # Time: 5.71 sec
"""

import time


class Timer:
    def __init__(self):
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def time_now(self):
        return f' time: {time.time() - self._start_time}'

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
