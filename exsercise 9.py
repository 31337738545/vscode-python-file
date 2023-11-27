# Function to check if a number is a palindrome
def is_palindrome(number):
    original_number = number
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10
    return original_number == reversed_number

# Get user input for the number to be checked
user_input = int(input("Enter a number to check if it's a palindrome: "))

# Check if the number is a palindrome using the function
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
