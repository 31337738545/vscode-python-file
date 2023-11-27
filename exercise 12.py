# Get user input for the year
user_input_year = int(input("Enter a year: "))

# Check if the year is a leap year
if (user_input_year % 4 == 0 and user_input_year % 100 != 0) or (user_input_year % 400 == 0):
    print(f"{user_input_year} is a Leap Year.")
else:
    print(f"{user_input_year} is not a Leap Year.")
