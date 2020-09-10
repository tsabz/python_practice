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


# def print_string(n):
#     print(*range(1, n+1), sep='')

# print(print_string(5))



# numbers = [1,2,3,4]
# multiply = [i*i for i in numbers]

# print(multiply)


# def paperwork(n,m):
#     if (n < 0):
#         return 0
#     elif(m < 0):
#         return 0
#     elif n or m > 0:
#         return n * m
        
# print(paperwork(-5,-5))
    

# def paperwork(n, m):
#     return n * m if n > 0 and m > 0 else 0

# def is_divide_by(number, a, b):
#     return False if a and b  number != 0 else True

# print(is_divide_by(45,5,15))

      # 012345678901234
food = "Fries and shake"

print(food[-4:-2]) #ha
print(food[0:5]) #Fries
print(food[2:4]) #ie start at the sencond index and slice the fourth
print(food[0:6:2]) #Fis
print(food[0:6]) #Fries 