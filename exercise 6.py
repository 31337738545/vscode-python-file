# Function to generate Fibonacci series
def generate_fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series

# Get user input for the number of terms
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

# Check if the input is a positive integer
if num_terms <= 0:
    print("Please enter a positive integer for the number of terms.")
else:
    # Generate and print the Fibonacci series
    fibonacci_series = generate_fibonacci(num_terms)
    print(f"The Fibonacci series up to {num_terms} terms is: {fibonacci_series}")
