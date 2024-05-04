class MyClass:
    # Class variables
    class_variable = 10

    # Constructor
    def __init__(self, name):
        self.name = name

    # Instance method
    def say_hello(self):
        return f"Hello, {self.name}!"

# Creating an instance of MyClass
obj = MyClass("Alice")

# Accessing instance variables and calling instance methods
print(obj.name)         # Output: Alice
print(obj.say_hello())  # Output: Hello, Alice!

# Accessing class variable
print(MyClass.class_variable)  # Output: 10
