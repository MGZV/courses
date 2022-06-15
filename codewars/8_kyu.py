"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.
For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
"""


# def square_sum(numbers):
#     num_sum = 0
#     for i in numbers:
#         num_sum += i ** 2
#     return num_sum


# best solution

# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)


#################################################

# def abbrev_name(name):
#     splited_name= name.split()
#     print(name.split())
#     two_letters = ''
#     for i in splited_name:
#         two_letters = two_letters + i[0].capitalize() + "."
#     return two_letters.strip('.')
#     # print(two_letters.strip('.'))
# abbrev_name("Sam Harris")


#################################################
"""
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
"""
def litres(time):
    print(int(time//2))
    return int(time//2)

litres(2)
litres(12.3)
litres(1.4)

# best solution

# def litres(time):
#     return time // 2
#################################################
