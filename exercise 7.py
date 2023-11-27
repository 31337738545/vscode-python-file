# Function to reverse a number
def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number = number // 10
    return reversed_num

# Get user input for the number to be reversed
user_input = int(input("Enter a number to reverse: "))

# Reverse the number using the function
reversed_result = reverse_number(user_input)

# Print the reversed number
print(f"The reversed number is: {reversed_result}")
