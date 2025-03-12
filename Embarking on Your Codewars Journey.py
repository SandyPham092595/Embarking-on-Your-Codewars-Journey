# Embarking on Your Codewars Journey

# Even or Odd
# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# Convert a Number to a String
# We need a function that can transform a number (integer) into a string.
def number_to_string(num):
    return str(num)

# Remove String Spaces
# Write a function that removes the spaces from the string, then return the resultant string.
def no_space(x):
    return x.replace(" ", "")

# Vowel Count
# Return the number (count) of vowels in the given string.
def get_count(sentence):
    return sum(1 for char in sentence if char in "aeiou")

# https://github.com/SandyPham092595/Embarking-on-Your-Codewars-Journey.git