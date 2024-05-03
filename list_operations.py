my_list = [1, 2, 3, 4, 5]

print(my_list[0])
print(my_list[-1])

print(my_list[1:3])
my_list.append(6)    # Appends 6 to the end of the list
my_list.extend([7, 8]) # Extends the list with elements from another list
my_list.insert(2, 'a')  # Inserts 'a' at index 2

my_list.remove(3)
del my_list[0]

print(len(my_list))
print(5 in my_list)

new_list = my_list.copy()