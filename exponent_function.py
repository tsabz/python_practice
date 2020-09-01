print(2**3)

def raise_to_power(base_num, pow_num):
    result = 1 # store the result of doing the math
    for index in range(pow_num): #if pow num is 2 loop through twice
        result = result * base_num
    return result

print(raise_to_power(2, 3))
