class Fibonacci:
    def __init__(self, number):
        self.number = number
        self.first_num = 0
        self.second_num = 1

    def __iter__(self):
        return self

    def __next__(self, final_num=None):
        while final_num <= self.number:
            final_num = self.first_num
            self.first_num = self.second_num
            self.second_num = self.first_num + self.second_num
            raise StopIteration


'''Напишите класс, объектом которого будет итератор производящий только
чётные числа до n включительно.'''


class Iterator:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.number):
            while i <= self.number:
                if i % 2 == 0:
                    return i
            raise StopIteration

"""
3.
Напишите итератор factorials(n), генерирующий последовательность
факториалов натуральных чисел.
"""


class Factorials:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        factorial = 1
        for i in range(2, self.number + 1):
            factorial *= i
            return factorial

        postgres =  # with tt as(select * from questions left join tests_questions on questions.id = tests_questions.question_id) select text from tests left join tt on tests.id = tt.id
