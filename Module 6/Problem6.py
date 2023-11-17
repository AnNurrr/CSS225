import math

# Get user input for non negative integer
user_input = int(input("Enter a non-negative integer: "))

# Calculate factorial using for statement
factorial_calculated = 1
for i in range(1, user_input + 1):
    factorial_calculated *= i

# Calculate factorial using the factorial function module math
factorial_math_module = math.factorial(user_input)

# Print values
print(f"User input value: {user_input}")
print(f"Calculated factorial (using for statement): {factorial_calculated}")
print(f"Calculated factorial (using math.factorial): {factorial_math_module}")
