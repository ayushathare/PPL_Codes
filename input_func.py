
# Accepting a string input
name = input("Enter your name: ")
print("Hello,", name)

# Accepting an integer input
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Accepting a float input
weight = float(input("Enter your weight (in kg): "))
print("Your weight is", weight, "kg.")

# Accepting a boolean input
is_student = input("Are you a student? (yes/no): ").lower()
if is_student == "yes":
    print("You are a student.")
else:
    print("You are not a student.")
