# Объект генератора

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

d = func_3(10)
print(next(d))
print(next(d))
print(next(d))
print(next(d))

