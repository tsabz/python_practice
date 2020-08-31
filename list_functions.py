lucky_numbers = [4, 8, 15, 16, 23, 42]

friends = ["Kevin" , "karen", "Jim", "Jim"]

print(friends)
print(lucky_numbers)

#extend function 
# friends.extend(lucky_numbers) #['Kevin', 'karen', 'Jim', 4, 8, 15, 16, 23, 42]
print(friends)

#addes item to end of list
friends.append("Creed")

#add item to middle of list
friends.insert(1, "kelly") #['Kevin', 'kelly', 'karen', 'Jim', 4, 8, 15, 16, 23, 42, 'Creed']

#remove an element
friends.remove("Kevin") #['kelly', 'karen', 'Jim', 4, 8, 15, 16, 23, 42, 'Creed']

#empty the whole list
# friends.clear()#[]

#lets see if a certain elemnt is in this list?
# print(friends.index("Kevin")) #'Kevin' is not in list


# print(friends)
print(friends.count("Jim")) #2

friends.sort()  # alphabetical ['Creed', 'Jim', 'Jim', 'karen', 'kelly']
print(friends)

lucky_numbers.sort()
print(lucky_numbers) #[4, 8, 15, 16, 23, 42]

lucky_numbers.reverse()
print(lucky_numbers) #[42, 23, 16, 15, 8, 4]

friends2 = friends.copy()

print(friends2) #['Creed', 'Jim', 'Jim', 'karen', 'kelly']
