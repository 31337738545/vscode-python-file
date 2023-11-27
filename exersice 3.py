# Get user input for the number
num = int(input("Enter a positive integer: "))

# Validate the input to ensure it's a positive integer
while num <= 0:
    print("Please enter a positive integer.")
    num = int(input("Enter a positive integer: "))

# Initialize variables
sum_of_numbers = 0
count = 1

# Use a while loop to find the sum of natural numbers
while count <= num:
    sum_of_numbers += count
    count += 1

# Display the result
print(f"The sum of natural numbers up to {num} is: {sum_of_numbers}")
