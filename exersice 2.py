# Get user input for the number
number = int(input("Enter a number to print its multiplication table: "))

# Define the range for the multiplication table (e.g., up to 10)
table_range = 10

# Use a for loop to print the multiplication table
print(f"Multiplication Table for {number}:")
for i in range(1, table_range + 1):
    result = number * i
    print(f"{number} x {i} = {result}")
