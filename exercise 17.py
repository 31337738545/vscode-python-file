# Get user input for the numeric score
numeric_score = float(input("Enter the numeric score: "))

# Determine the grade based on the numeric score
if 90 <= numeric_score <= 100:
    grade = "A"
elif 80 <= numeric_score < 90:
    grade = "B"
elif 70 <= numeric_score < 80:
    grade = "C"
elif 60 <= numeric_score < 70:
    grade = "D"
else:
    grade = "F"

# Print the result
print(f"The corresponding grade for the score {numeric_score} is: {grade}")
