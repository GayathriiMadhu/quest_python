# 3. Accept N strings and count the number of Palindromes in it.

def is_palindrome(string):
  """Checks if a string is a palindrome."""
  return string == string[::-1]

def count_palindromes(strings):
  """Counts the number of palindromes in a list of strings."""
  count = 0
  for string in strings:
    if is_palindrome(string):
      count += 1
  return count

# Get the number of strings
n = int(input("Enter the number of strings: "))

# Create an empty list to store the strings
strings = []

# Accept N strings from the user
for i in range(n):
  string = input("Enter string {}: ".format(i + 1))
  strings.append(string)

# Count the number of palindromes
num_palindromes = count_palindromes(strings)

print("Number of palindromes:", num_palindromes)