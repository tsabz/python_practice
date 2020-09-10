      # 012345678901234
food = "Fries and shake"

print(food[-4:-2]) #ha
print(food[0:5]) #Fries
print(food[2:4]) #ie start at the sencond index and slice the fourth
print(food[0:6:2]) #Fis
print(food[0:6]) #Fries 

number = "0123456789"

print(number[1::2]) #13579 every two starting from 1


#lets say we want to slice all the commans and colons from number

numbers = "100,982,302"

print(numbers[3::4]) #,, slice the commas out if you only want to return a number
