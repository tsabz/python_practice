# from math import * #math module. gives us access to a lot more math functions

num1 = float(input("Enter first number: "))
op = input("Enter second operator: ")
num2 = float(input("Enter second number: "))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")