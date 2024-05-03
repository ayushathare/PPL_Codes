import math


n = int(input("Enter Number to get sqare root"))
def square_root(num):
    if(num>2):
     return math.sqrt(num)
    else:
        print("Number cannot be negative")

print(square_root(n))