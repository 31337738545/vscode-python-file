# Function to calculate factorial
def calculate_factorial(number):
    factorial = 1
    while number > 0:
        factorial *= number
        number -= 1
    return factorial

# Get user input
user_input = int(input("Enter a number to calculate its factorial: "))

# Check if the input is non-negative
if user_input < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate and print the factorial
    result = calculate_factorial(user_input)
    print(f"The factorial of {user_input} is: {result}")
