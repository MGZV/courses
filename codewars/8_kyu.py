"""Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9."""


# def square_sum(numbers):
#     num_sum = 0
#     for i in numbers:
#         num_sum += i ** 2
#     return num_sum


# best solution

# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)


#################################################

def abbrev_name(name):
    splited_name= name.split()
    print(name.split())
    two_letters = ''
    for i in splited_name:
        two_letters = two_letters + i[0].capitalize() + "."
    return two_letters.strip('.')
    # print(two_letters.strip('.'))
abbrev_name("Sam Harris")