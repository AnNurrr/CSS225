# Ainur
# 11/21/2023


def count_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    num_vowels = sum(1 for char in input_string if char in vowels)
    num_consonants = sum(1 for char in input_string if char in consonants)

    return num_vowels, num_consonants

# Get input from the user
user_input = input("Enter a string: ")

# Call the function and display the result
vowels, consonants = count_vowels_and_consonants(user_input)
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
