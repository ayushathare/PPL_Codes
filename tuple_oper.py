tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

print(1 in tuple2) # check weather 1 is present in it or not
print(len(tuple1))

for i in tuple1:
    print(i)

concatenated_tuple = tuple1 + tuple2

print(concatenated_tuple)

repeated_tuple = (1, 2) * 3

print(repeated_tuple)