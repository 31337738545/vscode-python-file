# Get user input for the number
user_input = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if user_input > 0:
    print("The entered number is positive.")
elif user_input < 0:
    print("The entered number is negative.")
else:
    print("The entered number is zero.")
