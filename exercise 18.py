# Function to check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Get user input for the number
user_input = int(input("Enter a number to check if it's a prime number: "))

# Check if the number is prime using the function
if is_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")
