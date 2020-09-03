from math import * #math module. gives us access to a lot more math functions



# this function is in linear time
given_array = [1,4,3,2,5,10]

def find_sum(given_array):
    total = 0
    for nums in given_array:
        total += nums
        return total

#time complexity =       
# 
# linear time O(n)
# constant time O(1)
# quadratic time O(n2)  