# to write a function start with def

def say_hi(name):
    print("hello " + name)

# print("Top")
say_hi("tonia")
# print("Bottom")

# list = [5, 2, 3, 1, 4]

def order_list(arr):
    arr.sort()
    arr.append(2)
    # arr.count(2)
    print(arr)


order_list([5, 2, 3, 1, 4])