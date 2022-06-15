# Объект генератора
import sys
from datetime import datetime


def func(n):
    res = []
    count = 0
    while count < n:
        res.append(count)
        count += 1
    return res

# print(func(10))
# func(100_000_000)


def func_2():
    print("пришли")
    yield 1
    print("дай ещё")
    yield 2
    print("ушли")


def func_3(n):
    count = 0
    while count < n:
        yield count
        count += 1



# print(func(10))
# print(func_2())
# c = func_2()
#
# print(next(c))
# print("разделитель между обращениями")
# print(next(c))

# d = func_3(10)
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))


# start = datetime.now()
# print(f"Start working at {start}")
# d = func_3(100_000_000)
# l = func(100_000_000)
# r = range(100_000_000)
#
# print(f"size of object: {sys.getsizeof(r)}")
# print(f"Finish at: {datetime.now()}. Working time: {datetime.now() - start}")

# d = func_3(10)
# print(3 in d)
# print(list(d))


# def gen_f():
#     yield 1
#     yield 2
#
# gen_o = gen_f()
# print(gen_o)
#
# iterator = iter(gen_o)
# print(iterator)


l = [1, 2, 3, 4]
# print(next(l))
# list_it = iter(l)
# print(next(list_it))
# print(next(list_it))
# print(next(list_it))
# print(next(list_it))
# print(next(list_it))

# Что такое for
try:
    iterator = iter(l)
    while True:
        print(next(iterator))
except StopIteration:
    pass





# for el in l:
#     print(el)










