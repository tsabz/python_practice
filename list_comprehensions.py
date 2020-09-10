numbers = [1,2,3,4]
multiply = [i*i for i in numbers]

print(multiply)

print("-----------------------")


list_a = [1,2,3,4]
list_b = [2,3,4,5]

common_num = [a for a in list_a for b in list_b if a == b]

print(common_num)

print("-----------------------")

list_c = [1, 2, 3]
list_d = [2, 7]

different_num = [(c, d) for c in list_c for d in list_d if c != d]
multiply_num = [(c * d) for c in list_c for d in list_d if c != d]

print(different_num)
print(multiply_num)


print("-----------------------")


# var = [n != sum(x,y,z) for x in i for y in j for z in k ] 

