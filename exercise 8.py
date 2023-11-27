# Function to count vowels in a string
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

# Get user input for the string
user_input = input("Enter a string: ")

# Count vowels using the function
vowel_count_result = count_vowels(user_input)

# Print the result
print(f"The number of vowels in the string is: {vowel_count_result}")
