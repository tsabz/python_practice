def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else: 
        return num3 


print(max_num(7, 4, 5))



def is_weird(n): 
     if n % 2 != 0:
        print("Weird")
     else:
        if (n >= 2 and n <= 5):
            print("Not Weird")
        elif (n >= 6 and n <= 20):
            print("Weird")
        elif (n > 20): 
            print("Not Weird")

print(is_weird(4))


# if __name__ == '__main__':
#     n = int(input().strip())
#     if n % 2 != 0:
#         print("Weird")
#     elif n % 2 == 0 and n in range(2,5):
#         print("Not weird")
#     elif n % 2 == 0 and n in range(6,20):
#         print("Weird")
#     else: 
#         print("Not Weird")