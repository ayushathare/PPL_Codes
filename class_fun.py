class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

# Creating an instance of the Calculator class
calc = Calculator()

# Calling class functions
result_add = calc.add(5, 3)
result_subtract = calc.subtract(10, 4)
result_multiply = calc.multiply(6, 7)
result_divide = calc.divide(8, 2)

# Displaying results
print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
