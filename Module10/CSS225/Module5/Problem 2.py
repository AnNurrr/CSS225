# Ainur
# 10/25/2023
# Prints each number on a new line, prints each number and its square on a new line
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

print("Numbers are: ")
for number in numbers:
    print(number)


print("\n Numbers with their squares: ")
for number in numbers:
    square = number ** 2
    print(f"{number}: {square}")