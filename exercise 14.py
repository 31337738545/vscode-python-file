# Get user input for username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the entered username and password are correct
if username == "admin" and password == "12345":
    print("Login successful.")
else:
    print("Login failed.")
