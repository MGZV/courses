#  Пример декоратора

import time


# def decorator(function):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = function(*args, **kwargs)
#         end_time = time.time()
#         print(f'Time: {end_time - start_time}')
#         return result
#     return wrapper
#
#
# @ decorator
# def func_1():
#     return 1

# добавим сообщение


# def decorator(message):
#     def printer(function):
#         def wrapper(*args, **kwargs):
#             start_time = time.time()
#             print(message)
#             result = function(*args, **kwargs)
#             end_time = time.time()
#             print(f'Time: {end_time - start_time}')
#             return result
#         return wrapper
#     return printer
#
#
# @ decorator("Hello")
# def func_1():
#     return 1
#
#
# print(func_1())


# Проверка на анаграмму
from collections import Counter

s1 = "asd"
s2 = "dsa"


def is_anagram(a, b):
    a_count = Counter(a)
    b_count = Counter(b)
    if a_count == b_count:
        return True
    return False


assert is_anagram(s1, s2) is True
# assert is_anagram('a', 'b') is True