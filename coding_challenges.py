from math import * #math module. gives us access to a lot more math functions

# def square_num(n):
#     for i in range(n):
#         print(i**2)

   
# print(square_num(5))

# def is_leap(year):
#     leap = False
#     if year % 400 == 0:
#         leap = True
#     elif year % 4 == 0 and year % 100 != 0:
#         leap = True
       
#     return leap

# print(is_leap(1992))


def print_string(n):
    print(*range(1, n+1), sep='')

print(print_string(5))


