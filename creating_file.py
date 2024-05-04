file_path = "E:\MIT\PPL Codes\example.txt"

# Open the file in write mode
with open(file_path, 'w') as file:
    # Write content to the file
    file.write("Hello, world!\n")
    file.write("This is a new file created with Python.\n")

# Accessing a File

file_path = "E:\MIT\PPL Codes\example.txt"

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read content from the file
    content = file.read()
    print(content)


# Reading Line by line

file_path = "example.txt"

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read and print each line
    for line in file:
        print(line.strip())  # strip() removes trailing newline characters

