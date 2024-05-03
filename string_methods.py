s = "Hello world"
su = s.upper()
print(su)

sl = s.lower()
print(sl)

print(s.replace("Hello", "Hi"))
print(s.capitalize())
print(s.endswith("World"))

fruits = ['apple', 'banana', 'orange']
print(','.join(fruits))

if s.startswith("Hello"):
    print("String starts with 'hello'")